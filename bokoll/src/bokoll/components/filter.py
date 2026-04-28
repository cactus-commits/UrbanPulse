import streamlit as st
import pandas as pd
from bokoll.utils.helpers import load_map_data

df = load_map_data()


def reset_filters():
    st.session_state.vald_kategori = 'Alla'
    st.session_state.vald_stadsdel = 'Alla'
    st.session_state.vald_stadsdelsomrade = 'Alla'


def filter_layout():

    kategorilista = ['Alla'] + sorted(df["kategori"].dropna().unique())
    stadsdel_lista = ['Alla'] + sorted(df["stadsdel"].dropna().unique())
    stadsdelsomrade_lista = ['Alla'] + \
        sorted(df["stadsdelsomrade"].dropna().unique())

    # if 'vald_kategori' not in st.session_state:
    #     st.session_state.vald_kategori = 'Alla'
    # if 'vald_stadsdel' not in st.session_state:
    #     st.session_state.vald_stadsdel = 'Alla'
    # if 'vald_stadsdelsomrade' not in st.session_state:
    #     st.session_state.vald_stadsdelsomrade = 'Alla'

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        vald_kategori = st.selectbox(
            "Välj kategori:",
            options=kategorilista,
            key="vald_kategori"
        )

    with col2:
        vald_stadsdel = st.selectbox(
            "Välj stadsdel:",
            options=stadsdel_lista,
            key="vald_stadsdel"
        )

    with col3:
        vald_stadsdelsomrade = st.selectbox(
            "Välj område:",
            options=stadsdelsomrade_lista,
            key="vald_stadsdelsomrade"
        )

    with col4:
        st.markdown("")
        st.markdown("")
        st.button("Återställ filter", on_click=reset_filters)

    filtered_df = df.copy()

    if vald_kategori != 'Alla':
        filtered_df = filtered_df[filtered_df['kategori'] == vald_kategori]

    if vald_stadsdelsomrade != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdelsomrade']
                                  == vald_stadsdelsomrade]
    if vald_stadsdel != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdel'] == vald_stadsdel]

    return filtered_df
