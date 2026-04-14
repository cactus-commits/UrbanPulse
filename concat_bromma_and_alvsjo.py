import pandas as pd

df1 = pd.read_csv('data_files/bromma_data_with_adress.csv')
df2 = pd.read_csv('data_files/alvsjo_data_with_adress.csv')

df_combined = pd.concat([df1, df2], ignore_index=True)
df_combined.to_csv('data_files/combined_bromma_alvsjo_data_with_adresses.csv',
                   index=False, encoding='utf-8-sig')
