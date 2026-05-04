import streamlit as st
import pandas as pd
from bokoll.components.map import show_map  # , plotly_map
from bokoll.components.filter import filter_layout
from bokoll.components.donut import show_age_donut
from bokoll.components.bar_chart import bar_chart
from bokoll.components.kpis import total_boende_kpi, antal_skolor, total_service_kpi
from bokoll.components.line_chart import line_chart_brott
from bokoll.components.table import dataTable
from bokoll.components.images import home_image


def page_layout():
    st.title("Översikt")

    col_filter = st.columns(1, gap="medium", vertical_alignment="center")
    with col_filter[0]:
        st.subheader("Filtrera på kategori och stadsdel")
        filter_df = filter_layout()

    # plotly_map()

    img_col, col_kpi = st.columns(
        [7, 3], gap="medium", vertical_alignment="center")
    with img_col:
        home_image(vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    with col_kpi:
        with st.container(border=False):
            col1, col2 = st.columns(
                2, gap="medium", vertical_alignment="center")
            with col1:
                total_boende_kpi(vald_stadsdel=st.session_state.vald_stadsdel,
                                 vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
                antal_skolor(vald_stadsdel=st.session_state.vald_stadsdel,
                             vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
            with col2:
                total_service_kpi('Matbutik', "Antal Mataffärer", vald_stadsdel=st.session_state.vald_stadsdel,
                                  vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
                total_service_kpi('Apotek', "Antal Apotek", vald_stadsdel=st.session_state.vald_stadsdel,
                                  vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    col_map, col_list = st.columns(
        [3.5, 6.5], gap="medium", vertical_alignment="center")

    with col_map:
        with st.container(border=False):
            show_map(filter_df)

    with col_list:
        with st.container(border=False):
            st.subheader(
                "Lista över serviceutbud & tjänster för det valda området")
            dataTable(filter_df)

    col_donut, col_barchart = st.columns(
        [6, 4], gap="small", vertical_alignment="center")

    with col_donut:
        with st.container(border=False, height=600, vertical_alignment="center"):
            st.subheader("Befolkningsmängd")
            show_age_donut(filter_df)

    with col_barchart:
        with st.container(border=False, height=500, vertical_alignment="center"):
            st.subheader("Boendeform")
            bar_chart(vald_stadsdel=st.session_state.vald_stadsdel,
                      vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    with st.container(border=False):
        st.subheader("Antal anmälda brott")

        line_chart_brott(
            vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)


if __name__ == "__main__":
    page_layout()
