import pandas as pd

# 1. Läs in alla tre filer
df_geo = pd.read_csv('data_files/skolor_with_stadsdel.csv')

df_merit = pd.read_csv(
    'data_files/Grundskola - Slutbetyg årskurs 9, samtliga elever 2025 Skolnivå.csv',
    sep=';', encoding='utf-8-sig', skiprows=5
)

df_elever = pd.read_csv(
    'data_files/Grundskola - Antal elever per årskurs 2025 Skolnivå.csv',
    sep=';', encoding='utf-8-sig', skiprows=5
)

df_merit.columns = df_merit.columns.str.strip()
df_elever.columns = df_elever.columns.str.strip()

# 2. Filtrera på Stockholm INNAN clean/merge
df_merit_sthlm = df_merit[df_merit['Skolkommun'] == 'Stockholm'].copy()
df_elever_sthlm = df_elever[df_elever['Skolkommun'] == 'Stockholm'].copy()

# 3. Clean-funktion


def clean_name(n):
    if pd.isna(n):
        return n
    return str(n).lower().split(',')[0].strip().replace(' 1', '')


df_geo['match_key'] = df_geo['namn'].apply(clean_name)
df_merit_sthlm['match_key'] = df_merit_sthlm['Skola'].apply(clean_name)
df_elever_sthlm['match_key'] = df_elever_sthlm['Skola'].apply(clean_name)

# 4. Diagnostik – ska nu vara 0 dubletter
for label, df in [('GEO', df_geo), ('MERIT', df_merit_sthlm), ('ELEVER', df_elever_sthlm)]:
    dups = df[df.duplicated('match_key', keep=False)]
    if not dups.empty:
        print(f"⚠️  Fortfarande dubletter i {label} ({len(dups)} rader):")
        print(dups[['match_key']].value_counts().head(5))
    else:
        print(f"✅ {label}: inga dubletter")

# 5. Merge
df_final = pd.merge(
    df_geo,
    df_merit_sthlm[['match_key', 'Genomsnittligt meritvärde (17 ämnen)']],
    on='match_key', how='left'
)
df_final = pd.merge(
    df_final,
    df_elever_sthlm[['match_key', 'Elever, årskurs 1-9']],
    on='match_key', how='left'
)

# 6. Kontroll
print(f"\nRader i geo-filen:  {len(df_geo)}")
print(f"Rader i slutfilen:  {len(df_final)}  ← ska vara samma som ovan")

# 7. Spara
df_final = df_final.drop(columns=['match_key'])
df_final.to_csv('data_files/skolor_meriter_complete.csv',
                index=False, encoding='utf-8-sig', sep=';')
print("\n✅ Klar! Sparad till skolor_meriter_complete.csv")
