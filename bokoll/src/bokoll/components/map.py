
import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
from folium.plugins import Geocoder
from bokoll.utils.constants import DATA_PATH
from bokoll.utils.helpers import load_map_data
import geopandas as gpd
import plotly.express as px

df = load_map_data()


def show_map(data=None):

    if data is None or data.empty:
        # data = df
        st.warning("Ingen data finns för den valda platsen")
        return

    map_center = [data['lat'].mean(), data['lon'].mean()]
    m = folium.Map(location=map_center, zoom_start=9, height=300)

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

    st_folium(m, use_container_width=True, height=213)


# def plotly_map():
#     geo_df = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))
#     fig = px.scatter_map(geo_df,
#                         lat=geo_df.geometry.y,
#                         lon=geo_df.geometry.x,
#                         hover_name="kategori",
#                         zoom=1)
#     fig.show()
