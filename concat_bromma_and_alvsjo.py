import pandas as pd

df1 = pd.read_csv('data_files/combined_services_for_map.csv')
df2 = pd.read_csv('data_files/parker.csv')

df_combined = pd.concat([df1, df2], ignore_index=True)
df_combined.to_csv('data_files/combined_services_for_map.csv',
                   index=False, encoding='utf-8-sig')
