import pandas as pd

mean_age = pd.read_excel(r'data_files\1.3-medelalder-2005-2024.xlsx')

mean_age = mean_age.iloc[[5, 16]]

mean_age.columns = ['Område', '2010', '2015', '2020', '2021', '2022', '2023', '2024']

mean_age.to_csv('mean_age_2010_2024.csv', index=False)