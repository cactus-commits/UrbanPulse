
import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
from folium.plugins import Geocoder
from bokoll.utils.constants import DATA_PATH
from bokoll.components.filter import filter_layout

df = pd.read_csv(DATA_PATH / "combined_services_for_map_cleaned.csv")


def show_map(data=None):

    if data is None or data.empty:
        # data = df
        st.warning("Ingen data finns för den valda platsen")
        return

    map_center = [data['lat'].mean(), data['lon'].mean()]
    m = folium.Map(location=map_center, zoom_start=12)

    # Add searchbar to the map
    Geocoder().add_to(m)

   # adds marker for the location
    for idx, row in data.iterrows():
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"<b>{row['namn']}</b><br>{row['kategori']}<br>{row['gata']}",
            tooltip=row['namn'],
            icon=folium.Icon(color='beige', icon='info-sign')
        ).add_to(m)

    # shows the map
    st_folium(m, width=700, height=500)
