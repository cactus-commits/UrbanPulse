import streamlit as st
from bokoll.utils.helpers import load_brott_statistik

def line_chart_brott(vald_stadsdelsomrade):
    df = load_brott_statistik()

    if vald_stadsdelsomrade and vald_stadsdelsomrade != "Alla":
        df = df[df["stadsdelsomrade"] == vald_stadsdelsomrade.strip()]


    df_pivot = df.pivot(index="År", columns="stadsdelsomrade", values="Diagramvärde")
    
    st.line_chart(df_pivot)