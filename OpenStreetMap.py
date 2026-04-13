import requests
import pandas as pd
from geopy.geocoders import Nominatim

# variables to be able to run them seperatly in the functions
bromma = 5689303 + 3600000000
alvsjo = 8844985 + 3600000000

# Python-dict that translates to swedish
TYP_SVENSKA = {
    # Health care
    'centre':           'Hälsocenter',
    'doctor':           'Vårdcentral',
    'doctors':          'Vårdcentral',
    'hospital':         'Sjukhus',
    'dentist':          'Tandläkare',
    'physiotherapist':  'Fysioterapeut',
    'psychotherapist':  'Psykoterapeut',
    'pharmacy':         'Apotek',
    # Food and beverage
    'supermarket':      'Matbutik',
    'restaurant':       'Restaurang & Snabbmat',
    'fast_food':        'Restaurang & Snabbmat',
    'cafe':             'Kafé',
    # Education
    'driving_school':   'Trafikskola',
    # Other
    'library':          'Bibliotek',
    'fuel':             'Bensinmack',
    'cinema':           'Biograf',
    'alcohol':          'Systembolag',
    'fitness_centre':   'Gym/Utomhusgym',
    'fitness_station':  'Gym/Utomhusgym',
    'playground':       'Lekplats'
}

# Function to get the data url and query parameters
# - response is JSON
# - timeout:180 - wait 180 seconds
# - area Hägersten-Älvsjö into variable .a
# nwr N — Node (nod), W — Way (linje/yta), R — Relation
# out center - returns centered coordinate pair for ways/relations


def get_data(area_id):
    url = "https://overpass.kumi.systems/api/interpreter?data="

    query = f"""[out:json][timeout:300];
    area({area_id})->.a;
    (
        nwr["shop"~"supermarket|alcohol"](area.a);
        nwr["amenity"~"pharmacy|restaurant|fast_food|cafe|doctors|hospital|dentist|driving_school|library|fuel|cinema"](area.a);
        nwr["healthcare"~"centre|doctor|physiotherapist|psychotherapist"](area.a);
        nwr["leisure"~"playground|fitness_centre|fitness_station"](area.a);
        );
    out center;"""

    #   nwr["amenity" = "school"](area.a);
    #   nwr["amenity"="kindergarten"](area.a);
    #   nwr["amenity"="college"](area.a);
    #   nwr["amenity"="university"](area.a);
    #   nwr["amenity"="language_school"](area.a);
    #   nwr["amenity"="music_school"](area.a);
    print("Anropar Overpass API för {area_id}...")

    try:
        response = requests.get(
            url + query)
        response.raise_for_status()
        data = response.json()

        elements = data.get('elements', [])
        results = []

        for element in elements:
            tags = element.get('tags', {})
            # healthcare > amenity > shop > leisure
            raw_typ = tags.get('healthcare') or tags.get(
                'amenity') or tags.get('shop') or tags.get('leisure')

            namn = tags.get('name')
            if not namn:
                namn = TYP_SVENSKA.get(raw_typ)

            results.append({
                'Namn':     namn,
                'Typ':      raw_typ,
                'Kategori': TYP_SVENSKA.get(raw_typ),
                'Gata':     tags.get('addr:street', 'N/A'),
                'Nr':       tags.get('addr:housenumber', ''),
                'Lat':      element.get('lat') or element.get('center', {}).get('lat'),
                'Lon':      element.get('lon') or element.get('center', {}).get('lon'),
            })

        df = pd.DataFrame(results)

        print(f"Klart! Hittade {len(df)} platser.")
        print(df.head())
        df.to_csv(f"data_files/bromma_data.csv",
                  index=False, encoding='utf-8-sig')
        print("Sparad till csv")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP-fel: {err}")
    except Exception as e:
        print(f"Ett fel uppstod: {e}")


if __name__ == "__main__":
    get_data(bromma)
