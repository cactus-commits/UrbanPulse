import requests
import pandas as pd
from geopy.geocoders import Nominatim
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
    'restaurant':       'Restaurang',
    'fast_food':        'Snabbmat',
    'cafe':             'Kafé',
    # Education
    'school':           'Skola',
    'kindergarten':     'Skola',
    'college':          'Skola',
    'university':       'Skola',
    'driving_school':   'Trafikskola',
    # Other
    'parking':          'Parkering',
}

# Function to get the data url and query parameters
# - response is JSON
# - timeout:180 - wait 180 seconds
# - area Hägersten-Älvsjö into variable .a
# nwr N — Node (nod), W — Way (linje/yta), R — Relation
# out center - returns centered coordinate pair for ways/relations


def get_data():
    url = "https://overpass-api.de/api/interpreter?data="

    query = """
    [out:json][timeout:180];
    area(3605691404)->.a;
    (
      nwr["shop"="supermarket"](area.a);
      nwr["amenity"="pharmacy"](area.a);
      nwr["amenity"~"restaurant|fast_food|cafe"](area.a);
      nwr["amenity"~"doctors|hospital|dentist"](area.a);
      nwr["healthcare"~"centre|doctor|physiotherapist|psychotherapist"](area.a);
      nwr["amenity"="school"](area.a);
      nwr["amenity"="kindergarten"](area.a);
      nwr["amenity"="college"](area.a);
      nwr["amenity"="university"](area.a);
      nwr["amenity"="language_school"](area.a);
      nwr["amenity"="music_school"](area.a);
      nwr["amenity"="driving_school"](area.a);
      nwr["amenity"="parking"](area.a);
    );
    out center;
    """

    print("Anropar Overpass API för Hägersten-Älvsjö...")

    try:
        response = requests.get(
            url + query)
        response.raise_for_status()
        data = response.json()

        elements = data.get('elements', [])
        results = []

        for element in elements:
            tags = element.get('tags', {})
            # Priorotize healthcare > amenity > shop
            raw_typ = tags.get('healthcare') or tags.get(
                'amenity') or tags.get('shop')
            results.append({
                'Namn':     tags.get('name', 'N/A'),
                'Typ':      raw_typ,
                'Kategori': TYP_SVENSKA.get(raw_typ, raw_typ),
                'Gata':     tags.get('addr:street', 'N/A'),
                'Nr':       tags.get('addr:housenumber', ''),
                'Lat':      element.get('lat') or element.get('center', {}).get('lat'),
                'Lon':      element.get('lon') or element.get('center', {}).get('lon'),
            })

        df = pd.DataFrame(results)

        print(f"Klart! Hittade {len(df)} platser.")
        print(df.head())
        df.to_csv("alvsjo_data_V2.csv", index=False, encoding='utf-8-sig')
        print("Sparad till alvsjo_data.csv")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP-fel: {err}")
    except Exception as e:
        print(f"Ett fel uppstod: {e}")


if __name__ == "__main__":
    get_data()
