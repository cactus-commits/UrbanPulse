import streamlit as st
import duckdb
from bokoll.utils.helpers import load_folkmangd


def total_boende_kpi(vald_stadsdel='Alla', vald_stadsdelsomrade='Alla'):
    df = load_folkmangd()

    # Filtrera bort summa-rader och rader utan stadsdelsområde
    df = df[~df['Alder'].isin(['Total', 'No filters applied'])]
    df = df.dropna(subset=['Alder', 'value', 'stadsdelsomrade'])

    if vald_stadsdel != 'Alla':
        df = df[df['Stadsdel'] == vald_stadsdel]
    if vald_stadsdelsomrade != 'Alla':
        df = df[df['stadsdelsomrade'] == vald_stadsdelsomrade]

    result = duckdb.sql("""
        SELECT SUM(value)::INT AS total_boende
        FROM df
    """).df()

    total = int(result["total_boende"].iloc[0])
    st.metric(label="Totalt antal boende", value=f"{total:,}".replace(",", " "))