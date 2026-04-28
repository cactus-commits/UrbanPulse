import streamlit as st
import duckdb
from bokoll.utils.helpers import load_map_data
from bokoll.utils.helpers import load_folkmangd


def total_boende_kpi(vald_stadsdel='Alla', vald_stadsdelsomrade='Alla'):
    df = load_folkmangd()

    if vald_stadsdel != 'Alla':
        df = df[df['stadsdel'] == vald_stadsdel]
    if vald_stadsdelsomrade != 'Alla':
        df = df[df['stadsdelsomrade'] == vald_stadsdelsomrade]

    result = (
        duckdb.sql("""
            SELECT 
                SUM("Befolkning Totalt Område"):: INT AS total_boende
            FROM df
        """)
        .df()
    )

    st.metric(label="Totalt antal boende", value=result["total_boende"])

