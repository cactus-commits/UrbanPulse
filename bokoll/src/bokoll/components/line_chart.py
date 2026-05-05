import streamlit as st
from bokoll.utils.helpers import load_brott_statistik
from bokoll.utils.helpers import load_hyresutveckling
import plotly.express as px


def line_chart_brott(vald_stadsdelsomrade):
    df = load_brott_statistik()
    if vald_stadsdelsomrade and vald_stadsdelsomrade != "Alla":
        df = df[df["stadsdelsomrade"] == vald_stadsdelsomrade.strip()]

    fig = px.line(df, x="År", y="Diagramvärde",
                  color="stadsdelsomrade", height=300)
    fig.update_yaxes(range=[1500, df["Diagramvärde"].max() * 1.05])
    fig.update_xaxes(dtick=1)

    fig.update_layout(yaxis_title="Antal brott")

    st.plotly_chart(fig, use_container_width=True)


def line_chart_hyresutveckling(demografi_vald_stadsdelsomrade):
    df = load_hyresutveckling()
    if demografi_vald_stadsdelsomrade and demografi_vald_stadsdelsomrade != "Alla":
        df = df[df["stadsdelsomrade "] == demografi_vald_stadsdelsomrade.strip()]

    fig = px.line(df, x="År", y="Sum_of_Medelhyra_kvm",
                  color="stadsdelsomrade ")
    fig.update_yaxes(range=[1500, df["Sum_of_Medelhyra_kvm"].max() * 1.05])
    st.plotly_chart(fig, use_container_width=True)
