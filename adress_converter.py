import pandas as pd
from geopy.geocoders import Nominatim
import time


# df = pd.read_csv('data_files/alvsjo_data.csv')

geolocator = Nominatim(user_agent="my_geopy_app")


# Function to get the address from the lon and lat
def get_address(lat, lon, retries=3):
    for attempt in range(retries):
        try:
            location = geolocator.reverse([lat, lon], timeout=10)
            if not location:
                return None
            # Writing the address in raw format, but it just returns the road, house nr and suburb to keep
            addr = location.raw['address']
            return {
                'road':         addr.get('road', 'N/A'),
                'house_number': addr.get('house_number', 'N/A'),
                'suburb': (addr.get('suburb') or
                           addr.get('city_district') or
                           addr.get('quarter') or
                           addr.get('neighbourhood') or
                           addr.get('district') or 'N/A')
            }

        except Exception as e:
            print(f"  Försök {attempt+1} misslyckades: {e}")
            time.sleep(3)

    return None


# Function to apply the adress to the existing rows - also adding a new column for 'Stadsdel' to be able to get more locational
# informamtion from the lat and lon
def apply_address(df):
    # loop through the rows
    for index, row in df.iterrows():
        # If 'Gata' or 'Nr' is null or empty then get the adress from lon and lat
        if (pd.isna(row['Gata']) or row['Gata'] == 'N/A' or pd.isna(row['Nr']) or row['Nr'] == 'N/A'):

            location_data = get_address(row['Lat'], row['Lon'])
            # If it exist then add the gata, nr and stadsdel
            if location_data:
                df.at[index, 'Gata'] = location_data['road']
                df.at[index, 'Nr'] = location_data['house_number']
                df.at[index, 'Stadsdel'] = location_data['suburb']

            print(f"Rad {index}: {location_data}")
            # To be able to use geopy it must not call it again for at least 1 second
            time.sleep(1.1)

    # Write it to a new csv - file
    df.to_csv('data_files/bromma_data_with_adress.csv',
              index=False, encoding='utf-8-sig')
    print("Klart!")


if __name__ == "__main__":
    apply_address(pd.read_csv('data_files/bromma_data.csv'))
