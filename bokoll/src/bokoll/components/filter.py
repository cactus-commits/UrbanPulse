import streamlit as st
import pandas as pd
from bokoll.components.clean_map_data import df


def filter_layout():
    st.title("Översikt")

    st.header("Filtrera på kategori och stadsdel")

    df['kategori'] = df['kategori'].str.replace('_', ' ').str.title()

    kategorilista = ['Alla'] + sorted(df["kategori"].dropna().unique())
    stadsdel_lista = ['Alla'] + sorted(df["stadsdel"].dropna().unique())
    stadsdelsomrade_lista = ['Alla'] + \
        sorted(df["stadsdelsomrade"].dropna().unique())

    col1, col2, col3 = st.columns(3)

    with col1:
        vald_kategori = st.selectbox(
            "Välj kategori:",
            options=kategorilista,
            index=0
        )

    with col2:
        vald_stadsdel = st.selectbox(
            "Välj stadsdel:",
            options=stadsdel_lista,
            index=0
        )

    with col3:
        vald_stadsdelsomrade = st.selectbox(
            "Välj område:",
            options=stadsdelsomrade_lista,
            index=0
        )

    filtered_df = df.copy()

    if vald_kategori != 'Alla':
        filtered_df = filtered_df[filtered_df['kategori'] == vald_kategori]

    if vald_stadsdelsomrade != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdelsomrade']
                                  == vald_stadsdelsomrade]
    if vald_stadsdel != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdel'] == vald_stadsdel]

    st.dataframe(
        filtered_df[['namn', 'kategori', 'stadsdel', 'stadsdelsomrade']])

    return filtered_df
