import streamlit as st
import pandas as pd
from bokoll.components.map import show_map
from bokoll.components.filter import filter_layout
from bokoll.components.donut import show_age_donut
from bokoll.components.bar_chart import bar_chart
from bokoll.components.kpis import total_boende_kpi
from bokoll.components.line_chart import line_chart_brott
from bokoll.components.table import dataTable





def page_layout():
    st.title("Översikt")
    st.subheader("Filtrera på kategori och stadsdel")
    filter_df = filter_layout()

    col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")

    with col1:
        with st.container(border=True):
            show_map(filter_df)

    with col2:
        with st.container(border=True):
            total_boende_kpi(vald_stadsdel=st.session_state.vald_stadsdel,vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    st.subheader("Lista över serviceutbud & tjänster för det valda området")
    with st.container(border=True):
        dataTable(filter_df)

    col3, col4 = st.columns(2, gap="small", vertical_alignment="center")

    with col3:
        st.subheader("Befolkningsmängd")
        with st.container(border=True,height=600, vertical_alignment="center"): 
            show_age_donut(filter_df)

    with col4:
        st.subheader("Boendeform")
        with st.container(border=True, height=600, vertical_alignment="center"):
            
            bar_chart(vald_stadsdel=st.session_state.vald_stadsdel,
                      vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    st.subheader("Antal anmälda brott")
    with st.container(border=True):
        line_chart_brott(
            vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)


if __name__ == "__main__":
    page_layout()
