import csv
import asyncio
import httpx

CITY = ["Älvsjö", "Hägersten-Älvsjö", "Hägersten"]

SERVICE_TYPES = {
    "grundskolor": 13,
    "anpassade_grundskolor": 14,
    "öppen_förskola": 10,
    "förskola": 2,
}

async def fetch_service_units(service_type_id: int):
    url = (
        f"https://apigw.stockholm.se/api/PublicHittaCMS/api/serviceunits"
        f"?filter[servicetype.id]={service_type_id}&page[limit]=1500&page[offset]=0&sort=name"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    if "data" not in data:
        return []

    return [
        unit for unit in data["data"]
        if any(
            city.lower() in (unit.get("attributes", {}).get("address", {}).get("city", "")).lower()
            for city in CITY
        )
    ]

async def main():
    rows = []
    for name, type_id in SERVICE_TYPES.items():
        data = await fetch_service_units(type_id)
        for unit in data:
            attrs = unit.get("attributes", {})
            address = attrs.get("address", {})
            location = attrs.get("location", {})
            rows.append({
                "id": unit.get("id"),
                "kategori": name,
                "namn": attrs.get("name"),
                "gatuadress": address.get("street"),
                "postnummer": address.get("postalCode"),
                "stad": address.get("city"),
                "koordinat_east": location.get("east"),
                "koordinat_north": location.get("north"),
            })

    with open("data_files/skolor.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Klar! {len(rows)} rader sparade till data_files/skolor.csv")

asyncio.run(main())