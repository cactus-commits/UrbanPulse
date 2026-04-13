import pandas as pd

# Load all three files
skolor = pd.read_csv('data_files/skolor.csv')
# parkeringar = pd.read_csv('data_files/parkering.csv')
services = pd.read_csv(
    'data_files/combined_bromma_alvsjo_data_with_adresses.csv')

# Standardize columns to: namn, kategori, gata, lat, lon, stadsdel
skolor_clean = pd.DataFrame({
    'namn':      skolor['namn'],
    'kategori':  skolor['kategori'],
    'gata':      skolor['gatuadress'],
    'lat':       skolor['koordinat_north'],
    'lon':       skolor['koordinat_east'],
    'stadsdel':  skolor['stad']
})

# parkeringar_clean = pd.DataFrame({
#     'namn':      parkeringar['adress'],
#     'kategori':  parkeringar['platstyp'],
#     'gata':      parkeringar['gata'],
#     'lat':       parkeringar['latitud'],
#     'lon':       parkeringar['longitud'],
#     'stadsdel':  parkeringar['stadsdel']
# })

services_clean = pd.DataFrame({
    'namn':      services['Namn'],
    'kategori':  services['Kategori'],
    'gata':      services['Gata'],
    'lat':       services['Lat'],
    'lon':       services['Lon'],
    'stadsdel':  services['Stadsdel']
})

# Combine all into one table
combined = pd.concat([skolor_clean,
                     services_clean], ignore_index=True)
combined.to_csv('data_files/combined_school_parking.csv',
                index=False, encoding='utf-8-sig')
print("Klart!")
