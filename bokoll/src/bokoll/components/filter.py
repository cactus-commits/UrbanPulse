import streamlit as st
import pandas as pd
from bokoll.utils.helpers import load_map_data

df = load_map_data()


def sync_main_to_all():
    st.session_state.brott_vald_stadsdelsomrade = st.session_state.vald_stadsdelsomrade
    st.session_state.demografi_vald_stadsdel = st.session_state.vald_stadsdel
    st.session_state.demografi_vald_stadsdelsomrade = st.session_state.vald_stadsdelsomrade

def sync_brott_to_main():
    st.session_state.vald_stadsdelsomrade = st.session_state.brott_vald_stadsdelsomrade

def sync_demografi_to_main():
    st.session_state.vald_stadsdel = st.session_state.demografi_vald_stadsdel
    st.session_state.vald_stadsdelsomrade = st.session_state.demografi_vald_stadsdelsomrade

def reset_filters():
    for key in ['vald_kategori', 'vald_stadsdel', 'vald_stadsdelsomrade',
                'brott_vald_stadsdel', 'brott_vald_stadsdelsomrade',
                'demografi_vald_stadsdel', 'demografi_vald_stadsdelsomrade']:
        if key in st.session_state:
            st.session_state[key] = 'Alla'


def filter_layout():
    kategorilista = ['Alla'] + sorted(df["kategori"].dropna().unique())
    stadsdel_lista = ['Alla'] + sorted(df["stadsdel"].dropna().unique())
    stadsdelsomrade_lista = ['Alla'] + sorted(df["stadsdelsomrade"].dropna().unique())

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        vald_kategori = st.selectbox(
            "Välj kategori:",
            options=kategorilista,
            key="vald_kategori",
            on_change=sync_main_to_all
        )

    with col2:
        vald_stadsdel = st.selectbox(
            "Välj stadsdel:",
            options=stadsdel_lista,
            key="vald_stadsdel",
            on_change=sync_main_to_all
        )

    with col3:
        vald_stadsdelsomrade = st.selectbox(
            "Välj område:",
            options=stadsdelsomrade_lista,
            key="vald_stadsdelsomrade",
            on_change=sync_main_to_all
        )

    with col4:
        st.button("Återställ filter", on_click=reset_filters)

    filtered_df = df.copy()

    if vald_kategori != 'Alla':
        filtered_df = filtered_df[filtered_df['kategori'] == vald_kategori]
    if vald_stadsdelsomrade != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdelsomrade'] == vald_stadsdelsomrade]
    if vald_stadsdel != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdel'] == vald_stadsdel]

    return filtered_df


def filter_brott():
    stadsdelsomrade_lista = ['Alla'] + sorted(df["stadsdelsomrade"].dropna().unique())

    col2, col3 = st.columns(2)

    with col2:
        vald_stadsdelsomrade = st.selectbox(
            "Välj område:",
            options=stadsdelsomrade_lista,
            key="brott_vald_stadsdelsomrade",
            on_change=sync_brott_to_main
        )

    with col3:
        st.button("Återställ filter", on_click=reset_filters, key="brott_reset")

    filtered_df = df.copy()

    if vald_stadsdelsomrade != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdelsomrade'] == vald_stadsdelsomrade]

    return filtered_df


def filter_demografi():
    stadsdel_lista = ['Alla'] + sorted(df["stadsdel"].dropna().unique())
    stadsdelsomrade_lista = ['Alla'] + sorted(df["stadsdelsomrade"].dropna().unique())

    col1, col2, col3 = st.columns(3)

    with col1:
        vald_stadsdel = st.selectbox(
            "Välj stadsdel:",
            options=stadsdel_lista,
            key="demografi_vald_stadsdel",
            on_change=sync_demografi_to_main
        )

    with col2:
        vald_stadsdelsomrade = st.selectbox(
            "Välj område:",
            options=stadsdelsomrade_lista,
            key="demografi_vald_stadsdelsomrade",
            on_change=sync_demografi_to_main
        )

    with col3:
        st.button("Återställ filter", on_click=reset_filters, key="demografi_reset")

    filtered_df = df.copy()

    if vald_stadsdelsomrade != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdelsomrade'] == vald_stadsdelsomrade]
    if vald_stadsdel != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdel'] == vald_stadsdel]

    return filtered_df