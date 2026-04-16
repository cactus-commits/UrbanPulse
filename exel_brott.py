import pandas as pd

# Månadsordning för sortering
MONTH_ORDER = ['Jan', 'Feb', 'Mar', 'Apr', 'Maj', 'Jun',
               'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']


def parse_xls(path):
    df = pd.read_excel(path, engine='xlrd', header=None)

    # Hitta år från rad 2 (index 2), månader från rad 3 (index 3)
    year_row = df.iloc[2]
    month_row = df.iloc[3]

    # Bygg kolumnmappning: kolumnindex -> (år, månad)
    col_map = {}
    for col_idx in range(1, df.shape[1]):
        yr = year_row.iloc[col_idx]
        mn = month_row.iloc[col_idx]
        if pd.notna(yr) and pd.notna(mn):
            col_map[col_idx] = (str(yr).split('.')[0].strip(), str(mn).strip())

    records = []

    # Identifiera stadsdelssektioner: rader där col 0 innehåller "Stadsdelsområde"
    data_rows = df.iloc[5:]  # hoppa över header-rader

    current_stadsdel = None
    for _, row in data_rows.iterrows():
        cell = str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else ''

        if 'Stadsdelsområde' in cell:
            current_stadsdel = cell
            continue

        # Hoppa tomma rader och fotnadsrader
        if not cell or cell == 'nan' or len(cell) > 200:
            continue

        # Brottstyp-rader: har data i minst en månadskolumn
        values = {col_map[ci]: row.iloc[ci]
                  for ci in col_map if pd.notna(row.iloc[ci])}
        if not values:
            continue

        for (yr, mn), val in values.items():
            try:
                records.append({
                    'Stadsdel': current_stadsdel,
                    'Brottstyp': cell,
                    'År': yr,
                    'Månad': mn,
                    'Antal': int(float(val))
                })
            except (ValueError, TypeError):
                pass

    return pd.DataFrame(records)


def reshape(files):
    frames = []
    for path in files:
        frames.append(parse_xls(path))
    long = pd.concat(frames, ignore_index=True)

    # Pivotera: index = Månad, kolumner = (Stadsdel, Brottstyp, År)
    pivot = long.pivot_table(
        index='Månad',
        columns=['Stadsdel', 'Brottstyp', 'År'],
        values='Antal',
        aggfunc='first'
    )

    # Sortera månader i rätt ordning
    pivot = pivot.reindex([m for m in MONTH_ORDER if m in pivot.index])

    return pivot


if __name__ == '__main__':
    files = [
        'data_files/Brott_2024_Raw.xls',
        'data_files/Brott_2025_raw.xls',
        'data_files/Brott_2026_raw.xls',
    ]

    pivot = reshape(files)

    print(f"Dimensioner: {pivot.shape[0]} månader x {pivot.shape[1]} kolumner")
    print(f"Månader: {list(pivot.index)}")
    print(f"\nExempel (5 kolumner):")
    print(pivot.iloc[:, :5].to_string())

    out = 'brott_pivoterad.csv'
    pivot.to_csv(out)
    print(f"\nSparad till: {out}")
