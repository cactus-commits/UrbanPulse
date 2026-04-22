import pandas as pd

from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="my_coord_app")


def get_coordinates(adress):
    try:
        location = geolocator.geocode(adress, timeout=10)
        if not location:
            return None
        return {
            'lat': location.latitude,
            'lon': location.longitude
        }
    except Exception as e:
        print(f"Misslyckades: {e}")
        return None


def apply_coordinates(df):
    df['koordinat_north'] = df['koordinat_north'].astype(float)
    df['koordinat_east'] = df['koordinat_east'].astype(float)
    for index, row in df.iterrows():
        adress = f"{row['gatuadress']} {row['postnummer']}, {row['stad']}, Stockholm"

        coords = get_coordinates(adress)
        if coords:
            df.at[index, 'koordinat_north'] = coords['lat']
            df.at[index, 'koordinat_east'] = coords['lon']

        print(f"Rad {index}: {coords}")
        time.sleep(1.1)  # Nominatim-regel: max 1 anrop/sekund

    df.to_csv('data_files/output_with_coordinates.csv',
              index=False, encoding='utf-8-sig')
    print("Klart!")


if __name__ == "__main__":
    apply_coordinates(pd.read_csv('data_files/skolor.csv'))
