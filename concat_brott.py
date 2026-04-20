import pandas as pd

df_24 = pd.read_csv('data_files/brott_2024.csv', encoding='utf-8')
df_25 = pd.read_csv('data_files/brott_2025.csv', encoding='utf-8')
df_26 = pd.read_csv('data_files/brott_2026.csv', encoding='utf-8')

# Lägg till år-kolumn
df_24['År'] = 2024
df_25['År'] = 2025
df_26['År'] = 2026

# Kombinera ALLA först
df_all = pd.concat([df_24, df_25, df_26], ignore_index=True)

# Filtrera för både Bromma OCH Hägersten-Älvsjö
df_combined = df_all[
    df_all['Stadsdeldsområde'].isin(['Bromma', 'Hägersten-Älvsjö'])
][['Stadsdeldsområde', 'Totalt antal brott', 'År']]

df_combined.to_csv('data_files/combined_brott.csv')
