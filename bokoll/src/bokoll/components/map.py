
import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
from folium.plugins import Geocoder
from bokoll.utils.constants import DATA_PATH
from bokoll.utils.helpers import load_map_data
import geopandas as gpd


df = load_map_data()


def show_map(data=None):
    if data is None or data.empty:
        st.warning("Ingen data finns för den valda platsen")
        return

    # Räkna ut centrumpunkt för kartan baserat på koordinaterna
    map_center = [data['lat'].mean(), data['lon'].mean()]

    # Skapa kartobjektet - vi använder en något högre zoom för att se cirklarna bättre
    m = folium.Map(location=map_center, zoom_start=10,
                   tiles="CartoDB positron")

    # Visar sökfält med collaps
    Geocoder(collapsed=True).add_to(m)

    # Loopa igenom data och lägg till cirklar
    for idx, row in data.iterrows():
        # Bestäm färg baserat på kategori (Hex-koder ger snyggare färger)
        if row['kategori'] == 'Grundskolor':
            color_hex = "#003F47"
        elif row['kategori'] == 'Anpassade Grundskolor':
            color_hex = "#003F47"  # DodgerBlue
        elif row['kategori'] == 'Förskola':
            color_hex = "#003F47"  # DodgerBlue
        elif row['kategori'] == 'Öppen Förskola':
            color_hex = "#003F47"  # DodgerBlue
        elif row['kategori'] == 'Park':
            color_hex = "#738168"  # SeaGreen
        elif row['kategori'] == 'Lekplats':
            color_hex = "#738168"  # SeaGreen
        elif row["kategori"] == "Restaurang & Snabbmat":
            color_hex = "#A2C1C6"
        elif row["kategori"] == "Kafé":
            color_hex = "#A2C1C6"
        elif row["kategori"] == "Gym/Utomhusgym":
            color_hex = "#D8BD86"
        elif row["kategori"] == "Matbutik":
            color_hex = "#E39D4D"
        elif row["kategori"] == "Systembolag":
            color_hex = "#E39D4D"
        elif row["kategori"] == "Bibliotek":
            color_hex = "#E39D4D"
        elif row["kategori"] == "Apotek":
            color_hex = "#E39D4D"
        elif row["kategori"] == "Vårdcentral":
            color_hex = "#8F4D16"
        elif row["kategori"] == "Sjukhus":
            color_hex = "#8F4D16"
        elif row["kategori"] == "Tandläkare":
            color_hex = "#8F4D16"
        elif row["kategori"] == "Fysioterapeut":
            color_hex = "#8F4D16"
        elif row["kategori"] == "Biograf":
            color_hex = "#B59775"
        elif row["kategori"] == "Trafikskola":
            color_hex = "#B59775"
        elif row["kategori"] == "Bensinmack":
            color_hex = "#B59775"
        else:
            color_hex = "white"  # DarkOrange

        folium.CircleMarker(
            location=[row['lat'], row['lon']],
            # Storlek på cirkeln (minska för att göra mindre)
            radius=6,
            color="#FEFEFE",       # Kantfärg
            weight=1,                # Tjocklek på kantlinjen
            fill=True,
            fill_color=color_hex,    # Fyllnadsfärg
            fill_opacity=0.8,        # Genomskinlighet
            tooltip=row['namn'],     # Visa namn vid hovring
            popup=folium.Popup(
                f"<b>{row['namn']}</b><br>{row['kategori']}<br>{row['gata']}", max_width=200)
        ).add_to(m)

    # Visa kartan i Streamlit
    st_folium(
        m,
        use_container_width=True,
        height=213,
        returned_objects=[]
    )
