from fastapi import FastAPI
import httpx
import pandas as pd

app = FastAPI()

# Städer att filtrera på
CITY = ["Älvsjö", "Hägersten-Älvsjö", "Hägersten"]

# Mapping mellan endpoint-namn och service type ID
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
        return {"error": "Invalid API response"}

    # Filtrera på stad
    filtered = [
        unit for unit in data["data"]
        if any(
            city.lower() in (
                unit.get("attributes", {})
                    .get("address", {})
                    .get("city", "")
            ).lower()
            for city in CITY
        )
    ]

    return filtered if filtered else {"error": "No units found in the specified city."}


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/alla")
async def get_all():
    try:
        dfs = []

        for name, type_id in SERVICE_TYPES.items():
            data = await fetch_service_units(type_id)

            # Hoppa över om svaret är ett felmeddelande
            if isinstance(data, list):
                df = pd.json_normalize(data)
                df["kategori"] = name  # Lägg till kategori baserat på endpoint-namn
                dfs.append(df)

        # Slå ihop alla DataFrames till en
        combined_df = pd.concat(dfs, ignore_index=True)
        return combined_df.to_dict(orient="records")

    except Exception as e:
        return {"error": str(e)}


# Registrera dynamiskt en endpoint per verksamhetstyp
for name, type_id in SERVICE_TYPES.items():
    app.add_api_route(
        f"/{name}",
        make_endpoint(type_id),
        methods=["GET"]
    )



# from fastapi import FastAPI
# import httpx
# import pandas as pd

# app = FastAPI()

# CITY = ["Älvsjö", "Hägersten-Älvsjö", "Hägersten"]

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/grundskolor")
# async def get_schools():
#     try:
#         url = "https://apigw.stockholm.se/api/PublicHittaCMS/api/serviceunits?&filter[servicetype.id]=13&page[limit]=1500&page[offset]=0&sort=name"
#         async with httpx.AsyncClient() as client:
#             response = await client.get(url)
#             grundskolor = response.json()

#         if "data" in grundskolor:
#             filtered_schools = [
#                 school for school in grundskolor["data"]
#                 if any(
#                     city.lower() in (
#                         school.get("attributes", {})
#                             .get("address", {})
#                             .get("city", "")
#                     ).lower()
#                     for city in CITY
#                 )
#             ]

#             if filtered_schools:
#                 return filtered_schools
#             else:
#                 return {"error": "No schools found in the specified city."}
#         else:
#             return {"error": "Invalid API response"}
#     except Exception as e:
#         return {"error": str(e)}
    
# @app.get("/anpassade_grundskolor")
# async def get_schools():
#     try:
#         url = "https://apigw.stockholm.se/api/PublicHittaCMS/api/serviceunits?&filter[servicetype.id]=14&page[limit]=1500&page[offset]=0&sort=name"
#         async with httpx.AsyncClient() as client:
#             response = await client.get(url)
#             anpassade_grundskolor = response.json()

#         if "data" in anpassade_grundskolor:
#             filtered_schools = [
#                 school for school in anpassade_grundskolor["data"]
#                 if any(
#                     city.lower() in (
#                         school.get("attributes", {})
#                             .get("address", {})
#                             .get("city", "")
#                     ).lower()
#                     for city in CITY
#                 )
#             ]

#             if filtered_schools:
#                 return filtered_schools
#             else:
#                 return {"error": "No schools found in the specified city."}
#         else:
#             return {"error": "Invalid API response"}
#     except Exception as e:
#         return {"error": str(e)}


# @app.get("/öppen_förskola")
# async def get_schools():
#     try:
#         url = "https://apigw.stockholm.se/api/PublicHittaCMS/api/serviceunits?&filter[servicetype.id]=10&page[limit]=1500&page[offset]=0&sort=name"
#         async with httpx.AsyncClient() as client:
#             response = await client.get(url)
#             öppen_förskola = response.json()

#         if "data" in öppen_förskola:
#             filtered_schools = [
#                 school for school in öppen_förskola["data"]
#                 if any(
#                     city.lower() in (
#                         school.get("attributes", {})
#                             .get("address", {})
#                             .get("city", "")
#                     ).lower()
#                     for city in CITY
#                 )
#             ]

#             if filtered_schools:
#                 return filtered_schools
#             else:
#                 return {"error": "No schools found in the specified city."}
#         else:
#             return {"error": "Invalid API response"}
#     except Exception as e:
#         return {"error": str(e)}


# @app.get("/förskola")
# async def get_schools():
#     try:
#         url = "https://apigw.stockholm.se/api/PublicHittaCMS/api/serviceunits?&filter[servicetype.id]=2&page[limit]=1500&page[offset]=0&sort=name"
#         async with httpx.AsyncClient() as client:
#             response = await client.get(url)
#             förskola = response.json()

#         if "data" in förskola:
#             filtered_schools = [
#                 school for school in förskola["data"]
#                 if any(
#                     city.lower() in (
#                         school.get("attributes", {})
#                             .get("address", {})
#                             .get("city", "")
#                     ).lower()
#                     for city in CITY
#                 )
#             ]

#             if filtered_schools:
#                 return filtered_schools
#             else:
#                 return {"error": "No schools found in the specified city."}
#         else:
#             return {"error": "Invalid API response"}
#     except Exception as e:
#         return {"error": str(e)}
    


#FANNS INGA KOMVUX SKOLOR
# @app.get("/komvux")
# async def get_schools():
#     try:
#         url = "https://apigw.stockholm.se/api/PublicHittaCMS/api/serviceunits?&filter[servicetype.id]=113&page[limit]=1500&page[offset]=0&sort=name"
#         async with httpx.AsyncClient() as client:
#             response = await client.get(url)
#             komvux = response.json()

#         if "data" in komvux:
#             filtered_schools = [
#                 school for school in komvux["data"]
#                 if any(
#                     city.lower() in (
#                         school.get("attributes", {})
#                             .get("address", {})
#                             .get("city", "")
#                     ).lower()
#                     for city in CITY
#                 )
#             ]

#             if filtered_schools:
#                 return filtered_schools
#             else:
#                 return {"error": "No schools found in the specified city."}
#         else:
#             return {"error": "Invalid API response"}
#     except Exception as e:
#         return {"error": str(e)}
