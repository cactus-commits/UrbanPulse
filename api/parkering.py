import csv
import asyncio
import httpx

PARKING_DISTRICTS = ["Älvsjö", "Hägersten-Älvsjö", "Hägersten", "Bromma norra"]

API_KEY = "66c6730d-1af7-4889-a250-d93d443d1e26"
API_URL = "https://openparking.stockholm.se/LTF-Tolken/v1/ptillaten/all"

async def fetch_parking_data():
    params = {
        "maxFeatures": 50000,
        "outputFormat": "json",
        "apiKey": API_KEY
    }
    
    timeout = httpx.Timeout(10)
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.get(API_URL, params=params)
        data = response.json()
    
    return data.get("features", [])

async def main():
    print("Hämtar parkeringsdata...")
    features = await fetch_parking_data()
    
    rows = []
    for feature in features:
        props = feature.get("properties", {})
        parking_district = props.get("PARKING_DISTRICT", "")
        
        # Filtrera på önskade stadsdelar
        if parking_district not in PARKING_DISTRICTS:
            continue
        
        # Hämta koordinater från geometry
        coords = feature.get("geometry", {}).get("coordinates", [[None, None]])[0]
        
        rows.append({
            "gata": props.get("STREET_NAME"),
            "adress": props.get("ADDRESS"),
            "stadsdel": props.get("CITY_DISTRICT"),
            "parkeringsomrade": parking_district,
            "platstyp": props.get("VF_PLATS_TYP"),
            "taxa": props.get("PARKING_RATE"),
            "ovrig_info": props.get("OTHER_INFO"),
            "giltigt_fran": props.get("VALID_FROM"),
            "start_manad": props.get("START_MONTH"),
            "slut_manad": props.get("END_MONTH"),
            "start_dag": props.get("START_DAY"),
            "slut_dag": props.get("END_DAY"),
            "start_tid": props.get("START_TIME"),
            "slut_tid": props.get("END_TIME"),
            "veckodag": props.get("START_WEEKDAY"),
            "longitud": coords[0],
            "latitud": coords[1],
            "fordon": props.get("VEHICLE"),
            "beslut": props.get("CITATION"),
            "rdt_url": props.get("RDT_URL"),
        })
    
    # Spara till CSV
    if rows:
        with open("data_files/parkering.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"Klar! {len(rows)} parkeringsregler sparade till parkering.csv")
    else:
        print("Ingen parkeringsdata hittades för de angivna stadsdelarna")

if __name__ == "__main__":
    asyncio.run(main())