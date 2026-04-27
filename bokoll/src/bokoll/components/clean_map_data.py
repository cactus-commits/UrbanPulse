import pandas as pd
from bokoll.utils.constants import DATA_PATH

df = pd.read_csv(DATA_PATH / "combined_services_for_map.csv",
                 encoding='utf-8-sig')


valid_coords = (df['lat'].between(55, 62)) & (df['lon'].between(15, 20))
df = df[valid_coords]
df = df[df['stadsdelsomrade'].notna() & (df['stadsdelsomrade'] != '')]
df = df.drop_duplicates()

df.to_csv('combined_services_for_map_cleaned.csv',
          index=False, encoding='utf-8-sig')
