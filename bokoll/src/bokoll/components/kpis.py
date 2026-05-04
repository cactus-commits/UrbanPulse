import streamlit as st
import duckdb
from bokoll.utils.helpers import load_folkmangd, load_map_data, load_brott_per_capita
import pandas as pd


def total_boende_kpi(vald_stadsdel='Alla', vald_stadsdelsomrade='Alla'):
    df = load_folkmangd().copy()  # Skapa en kopia av DataFrame för att undvika cache-problem

    # Filtrera bort summa-rader och rader utan stadsdelsområde
    df = df[~df['Alder'].isin(['Total', 'No filters applied'])]
    df = df.dropna(subset=['Alder', 'value', 'stadsdelsomrade'])

    if vald_stadsdel != 'Alla':
        df = df[df['Stadsdel'] == vald_stadsdel]
    if vald_stadsdelsomrade != 'Alla':
        df = df[df['stadsdelsomrade'] == vald_stadsdelsomrade]
        
    total = int(df['value'].sum())
    st.metric(label="Antal boende", value=f"{total:,}".replace(",", " "))

def demografi_snittålder(vald_stadsdel='Alla', vald_stadsdelsomrade='Alla'):
    df = load_folkmangd()

    if vald_stadsdel != 'Alla':
        df = df[df['Stadsdel'] == vald_stadsdel]
    if vald_stadsdelsomrade != 'Alla':
        df = df[df['stadsdelsomrade'] == vald_stadsdelsomrade]

    mittpunkt = {
        '0-4 år': 2, '5-9 år': 7, '10-14 år': 12, '15-19 år': 17,
        '20-24 år': 22, '25-29 år': 27, '30-34 år': 32, '35-39 år': 37,
        '40-44 år': 42, '45-49 år': 47, '50-54 år': 52, '55-59 år': 57,
        '60-64 år': 62, '65-69 år': 67, '70-74 år': 72, '75-79 år': 77,
        '80- år': 85
    }

    df = df[df['Alder'].isin(mittpunkt)].copy()
    df['mp'] = df['Alder'].map(mittpunkt)
    total = round((df['mp'] * df['value']).sum() / df['value'].sum(), 1)

    st.metric(label="Snittålder", value=f"{total:.1f}")


def demografi_invånare(vald_stadsdel='Alla', vald_stadsdelsomrade='Alla'):
    df = load_folkmangd()
    df = df[df['stadsdelsomrade'].notna()]

    if vald_stadsdel != 'Alla':
        df = df[df['Stadsdel'] == vald_stadsdel]
    if vald_stadsdelsomrade != 'Alla':
        df = df[df['stadsdelsomrade'] == vald_stadsdelsomrade]

    total = int(df['value'].sum())
    st.metric(label="Antal invånare", value=f"{total:,}".replace(",", " "))


def antal_skolor(vald_stadsdel='Alla', vald_stadsdelsomrade='Alla'):
    df = load_map_data()
    skolor = df[df['kategori'].isin(
        ['Grundskolor', 'Öppen Förskola', 'Förskola', 'Anpassade Grundskolor'])]

    if vald_stadsdel != 'Alla':
        skolor = skolor[skolor['stadsdel'] == vald_stadsdel]
    if vald_stadsdelsomrade != 'Alla':
        skolor = skolor[skolor['stadsdelsomrade'] == vald_stadsdelsomrade]

    total = len(skolor)
    st.metric(label="Skolor", value=f"{total:,}".replace(",", " "))


def total_service_kpi(kategori, label, vald_stadsdel='Alla', vald_stadsdelsomrade='Alla'):
    df = load_map_data()

    # Filtrera på kategori
    df = df[df['kategori'] == kategori]

    if vald_stadsdel != 'Alla':
        df = df[df['stadsdel'] == vald_stadsdel]
    if vald_stadsdelsomrade != 'Alla':
        df = df[df['stadsdelsomrade'] == vald_stadsdelsomrade]

    result = duckdb.sql("""--sql
        SELECT COUNT(*)::INT AS total
        FROM df
    """).df()

    total = int(result["total"].iloc[0])
    st.metric(label=label, value=f"{total:,}".replace(",", " "))

def kpi_brott(brottstyp, label, vald_stadsdelsomrade='Alla'):
    df = load_brott_per_capita()
    df = df[df['Brottstyp'] == brottstyp]

    if vald_stadsdelsomrade != 'Alla':
        df = df[df['område'] == vald_stadsdelsomrade]

    result = duckdb.sql("""
        SELECT 
            SUM("2025")::INT AS total_2025,
            SUM("2024")::INT AS total_2024
        FROM df
    """).df()

    total_2025 = int(result["total_2025"].iloc[0])
    total_2024 = int(result["total_2024"].iloc[0])

    diff = total_2025 - total_2024
    pct = (diff / total_2024 * 100) if total_2024 != 0 else 0
    delta_str = f"{diff:+,} ({pct:+.1f}%)".replace(",", " ")

    st.metric(
        label=label,
        value=f"{total_2025:,}".replace(",", " "),
        delta=delta_str,
        delta_color="inverse"  # rött = ökning (fler brott = dåligt), grönt = minskning
    )