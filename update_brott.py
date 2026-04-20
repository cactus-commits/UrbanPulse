import pandas as pd

df = pd.read_csv('data_files/brottsstatistik_per_capita_cleaned.csv')

df['område'] = df['område'].replace('Älvsjö', 'Hägersten-Älvsjö')

df.to_csv('data_files/brottsstatistik_per_capita_cleaned.csv')
