import streamlit as st
import pandas as pd
from bokoll.utils.helpers import load_map_data

df = load_map_data()


def sync_main_to_brott():
    st.session_state.brott_vald_stadsdel = st.session_state.vald_stadsdel
    st.session_state.brott_vald_stadsdelsomrade = st.session_state.vald_stadsdelsomrade

def sync_brott_to_main():
    st.session_state.vald_stadsdel = st.session_state.brott_vald_stadsdel
    st.session_state.vald_stadsdelsomrade = st.session_state.brott_vald_stadsdelsomrade

def sync_main_to_demografi():
    st.session_state.demografi_vald_stadsdel = st.session_state.vald_stadsdel
    st.session_state.demografi_vald_stadsdelsomrade = st.session_state.vald_stadsdelsomrade

def sync_demografi_to_main():
    st.session_state.vald_stadsdel = st.session_state.demografi_vald_stadsdel
    st.session_state.vald_stadsdelsomrade = st.session_state.demografi_vald_stadsdelsomrade

def reset_filters():
    for key in ['vald_kategori', 'vald_stadsdel', 'vald_stadsdelsomrade',
                'brott_vald_stadsdel', 'brott_vald_stadsdelsomrade', 'demografi_vald_stadsdel', 'demografi_vald_stadsdelsomrade']:
        if key in st.session_state:
            st.session_state[key] = 'Alla'


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
            key="vald_kategori",
            on_change=sync_main_to_brott
        )

    with col2:
        vald_stadsdel = st.selectbox(
            "Välj stadsdel:",
            options=stadsdel_lista,
            key="vald_stadsdel",
            on_change=sync_main_to_brott
        )

    with col3:
        vald_stadsdelsomrade = st.selectbox(
            "Välj område:",
            options=stadsdelsomrade_lista,
            key="vald_stadsdelsomrade",
            on_change=sync_main_to_brott
        )

    with col4:

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



def filter_brott():
    stadsdel_lista = ['Alla'] + sorted(df["stadsdel"].dropna().unique())
    stadsdelsomrade_lista = ['Alla'] + sorted(df["stadsdelsomrade"].dropna().unique())

    # Sync from main filter if already set
    default_stadsdel = st.session_state.get('vald_stadsdel', 'Alla')
    default_omrade = st.session_state.get('vald_stadsdelsomrade', 'Alla')

    col1, col2, col3 = st.columns(3)

    with col1:
        vald_stadsdel = st.selectbox(
            "Välj stadsdel:",
            options=stadsdel_lista,
            index=stadsdel_lista.index(default_stadsdel) if default_stadsdel in stadsdel_lista else 0,
            key="brott_vald_stadsdel",
            on_change=sync_brott_to_main 
        )

    with col2:
        vald_stadsdelsomrade = st.selectbox(
            "Välj område:",
            options=stadsdelsomrade_lista,
            index=stadsdelsomrade_lista.index(default_omrade) if default_omrade in stadsdelsomrade_lista else 0,
            key="brott_vald_stadsdelsomrade",
            on_change=sync_brott_to_main
        )

    with col3:
        st.button("Återställ filter", on_click=reset_filters, key="brott_reset")

    filtered_df = df.copy()

    if vald_stadsdelsomrade != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdelsomrade'] == vald_stadsdelsomrade]
    if vald_stadsdel != 'Alla':
        filtered_df = filtered_df[filtered_df['stadsdel'] == vald_stadsdel]

    return filtered_df

def filter_demografi():
    stadsdel_lista = ['Alla'] + sorted(df["stadsdel"].dropna().unique())
    stadsdelsomrade_lista = ['Alla'] + sorted(df["stadsdelsomrade"].dropna().unique())

    # Sync from main filter if already set
    default_stadsdel = st.session_state.get('vald_stadsdel', 'Alla')
    default_omrade = st.session_state.get('vald_stadsdelsomrade', 'Alla')

    col1, col2, col3 = st.columns(3)

    with col1:
        vald_stadsdel = st.selectbox(
            "Välj stadsdel:",
            options=stadsdel_lista,
            index=stadsdel_lista.index(default_stadsdel) if default_stadsdel in stadsdel_lista else 0,
            key="demografi_vald_stadsdel",
            on_change=sync_demografi_to_main 
        )

    with col2:
        vald_stadsdelsomrade = st.selectbox(
            "Välj område:",
            options=stadsdelsomrade_lista,
            index=stadsdelsomrade_lista.index(default_omrade) if default_omrade in stadsdelsomrade_lista else 0,
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