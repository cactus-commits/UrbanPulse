import streamlit as st
import pandas as pd
from bokoll.components.map import show_map, plotly_map
from bokoll.components.filter import filter_layout
from bokoll.components.donut import show_age_donut
from bokoll.components.bar_chart import bar_chart
from bokoll.components.kpis import total_boende_kpi, antal_skolor
from bokoll.components.line_chart import line_chart_brott
from bokoll.components.table import dataTable
from bokoll.components.images import home_image


def page_layout():
    st.title("Översikt")
    st.subheader("Filtrera på kategori och stadsdel")
    filter_df = filter_layout()

    # plotly_map()

    col_img, col_kpi = st.columns(2, gap="medium", vertical_alignment="center")

    with col_img:
        home_image(vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    with col_kpi:
        with st.container(border=True):
            total_boende_kpi(vald_stadsdel=st.session_state.vald_stadsdel,
                             vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
            antal_skolor(vald_stadsdel=st.session_state.vald_stadsdel,
                         vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    col_map, col_list = st.columns(
        2, gap="medium", vertical_alignment="center")

    with col_map:
        with st.container(border=True):
            show_map(filter_df)

    with col_list:
        with st.container(border=True):
            st.subheader(
                "Lista över serviceutbud & tjänster för det valda området")
            dataTable(filter_df)

    col_donut, col_barchart = st.columns(
        2, gap="small", vertical_alignment="center")

    with col_donut:
        with st.container(border=True, height=500, vertical_alignment="center"):
            st.subheader("Befolkningsmängd")
            show_age_donut(filter_df)

    with col_barchart:
        with st.container(border=True, height=500, vertical_alignment="center"):
            st.subheader("Boendeform")
            bar_chart(vald_stadsdel=st.session_state.vald_stadsdel,
                      vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    with st.container(border=True):
        st.subheader("Antal anmälda brott")

        line_chart_brott(
            vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)


if __name__ == "__main__":
    page_layout()
