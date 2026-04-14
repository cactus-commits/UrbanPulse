import pandas as pd

# 1. Läs in alla tre filer
df_geo = pd.read_csv('data_files/skolor_with_stadsdel.csv')

# Fil 1: Meritvärden
df_merit = pd.read_csv(
    'data_files/Grundskola - Slutbetyg årskurs 9, samtliga elever 2025 Skolnivå.csv',
    sep=';',
    encoding='utf-8-sig',
    skiprows=5
)

# Fil 2: Elevstatistik (Den du skickade nu)
df_elever = pd.read_csv(
    # Byt till rätt filnamn
    'data_files/Grundskola - Antal elever per årskurs 2025 Skolnivå.csv',
    sep=';',
    encoding='utf-8-sig',
    skiprows=5  # Justera om rubriken ligger på annan rad
)

# Städa kolumnnamn i båda statistikfilerna
df_merit.columns = df_merit.columns.str.strip()
df_elever.columns = df_elever.columns.str.strip()

# 2. Funktion för att tvätta namnen (match_key)


def clean_name(n):
    if pd.isna(n):
        return n
    # ' 1' tas bort ifall "Aroseniusskolan 1" ska matcha "Aroseniusskolan"
    return str(n).lower().split(',')[0].strip().replace(' 1', '')


df_geo['match_key'] = df_geo['namn'].apply(clean_name)
df_merit['match_key'] = df_merit['Skola'].apply(clean_name)
df_elever['match_key'] = df_elever['Skola'].apply(clean_name)

# 3. Slå ihop allt stegvis (Merge)
# Först: Lägg till Meritvärde på Geo
df_final = pd.merge(
    df_geo,
    df_merit[['match_key', 'Genomsnittligt meritvärde (17 ämnen)']],
    on='match_key',
    how='left'
)

# Sedan: Lägg till "Elever, årskurs 1-9" från den nya filen
df_final = pd.merge(
    df_final,
    df_elever[['match_key', 'Elever, årskurs 1-9']],
    on='match_key',
    how='left'
)

# 4. Städa och spara
df_final = df_final.drop(columns=['match_key'])
df_final.to_csv('data_files/skolor_meriter_complete.csv', index=False,
                encoding='utf-8-sig', sep=';')

print("Succé! Filen 'skolor_total_statistik.csv' innehåller nu både adresser, meriter och elevantal.")
