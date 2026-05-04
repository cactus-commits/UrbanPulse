import streamlit as st
import pandas as pd
from bokoll.components.map import show_map
from bokoll.components.filter import filter_layout, filter_brott
from bokoll.components.donut import show_age_donut
from bokoll.components.bar_chart import bar_chart, bar_chart_brott_2025
from bokoll.components.bar_chart_befolkning import bar_chart_befolkning
from bokoll.components.kpis import total_boende_kpi, antal_skolor, total_service_kpi, kpi_brott, demografi_snittålder, demografi_invånare, demografi_inkomst, demografi_skattesats
from bokoll.components.line_chart import line_chart_brott, line_chart_hyresutveckling
from bokoll.components.table import dataTable
from bokoll.components.images import home_image
from bokoll.assets.style.styling_page import styled_container


def page_layout():
    st.markdown("# Översikt")
    st.markdown("---")  # Lägg till en horisontell linje för att separera sektionerna

    col_filter = st.columns(1, gap="medium", vertical_alignment="top")
    with col_filter[0]:
        st.markdown("###### Filtrera på kategori och stadsdel")
        filter_df = filter_layout()

    img_col, col_kpi = st.columns(
        [7, 3], gap="medium", vertical_alignment="top")
    with img_col:
        home_image(vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    with col_kpi:
        with styled_container():
            col1, col2 = st.columns(
                2, gap="medium", vertical_alignment="top")
            with col1:
                total_boende_kpi(vald_stadsdel=st.session_state.vald_stadsdel,
                                 vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade) #kanske borde bytas till något annat
                antal_skolor(vald_stadsdel=st.session_state.vald_stadsdel,
                             vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
                total_service_kpi('Gym/Utomhusgym', "Gym", vald_stadsdel=st.session_state.vald_stadsdel,
                                  vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
            with col2:
                total_service_kpi('Matbutik', "Mataffärer", vald_stadsdel=st.session_state.vald_stadsdel,
                                  vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
                total_service_kpi('Apotek', "Apotek", vald_stadsdel=st.session_state.vald_stadsdel,
                                  vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
                total_service_kpi('Vårdcentral', "Vårdcentraler", vald_stadsdel=st.session_state.vald_stadsdel,
                                  vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    col_map, col_list = st.columns(
        [4, 6], gap="medium", vertical_alignment="top")

    with col_map:
        with styled_container():
            st.markdown(
                "###### Karta")
            show_map(filter_df)

    with col_list:
        with styled_container():
            st.markdown(
                "###### Lista över serviceutbud & tjänster för det valda området")
            dataTable(filter_df)
    
##############################################################
    st.markdown("# Demografi")
    st.markdown("---")  # Lägg till en horisontell linje för att separera sektionerna

    rad1_col1, rad1_col2 = st.columns(2, gap="medium")

    with rad1_col1:
        with st.container(border=True):
            st.subheader("Hyresutveckling")
            line_chart_hyresutveckling(
                vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
            st.caption("Källa: SCB")

    with rad1_col2:
        with st.container(border=True):
            st.subheader("Demografi i korthet")

            # 2x2-grid med fyra KPI:er
            kpi_col1, kpi_col2 = st.columns(2, gap="small")
            with kpi_col1:
                demografi_snittålder(
                    vald_stadsdel=st.session_state.vald_stadsdel,
                    vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
            with kpi_col2:
                demografi_invånare(
                    vald_stadsdel=st.session_state.vald_stadsdel,
                    vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

            kpi_col3, kpi_col4 = st.columns(2, gap="small")
            with kpi_col3:
                demografi_inkomst(
                    vald_stadsdel=st.session_state.vald_stadsdel,
                    vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
            with kpi_col4:
                demografi_skattesats(
                    vald_stadsdel=st.session_state.vald_stadsdel,
                    vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

            st.caption("Källa: SCB")

    col_donut, col_barchart = st.columns(
        [5, 5], gap="small", vertical_alignment="top")

    with col_donut:
        with styled_container():
            st.markdown("###### Befolkningsmängd")
            show_age_donut(filter_df)

    with col_barchart:
        with styled_container():
            st.markdown("###### Boendeform")
            bar_chart(vald_stadsdel=st.session_state.vald_stadsdel,
                      vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
            
    rad2_col1, rad2_col2 = st.columns(2, gap="medium")

    with rad2_col1:
        with st.container(border=True):
            st.subheader("Befolkningsmängd")
            bar_chart_befolkning(filter_df)
            st.caption("Källa: SCB")

            
##############################################################      
    st.markdown("# Brottsstatistik")
    st.markdown("---")  # Lägg till en horisontell linje för att separera sektionerna

    col_filter = st.columns(1, gap="medium", vertical_alignment="top")
    with col_filter[0]:
        st.markdown("###### Filtrera på kategori och stadsdel")
        filter_df = filter_brott()

    col_kpi_brott, col_linechart = st.columns(
        [4, 6], gap="medium", vertical_alignment="top")
    with col_kpi_brott:
        with styled_container():
            st.markdown(
                "###### Brottsutveckling \n Totala antal brott 2025 \n samt ökning eller minskning jämfört med 2024")
            col1, col2 = st.columns(
                2, gap="small", vertical_alignment="center")
            with col1:
                kpi_brott(("Narkotikabrott"), "Narkotikabrott",
                          vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))
                kpi_brott("Misshandel", "Misshandel",
                          vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))

            with col2:
                kpi_brott("Sexualbrott", "Sexualbrott",
                          vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))
                kpi_brott("Bostadsinbrott", "Bostadsinbrott",
                          vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))

    with col_linechart:
        with styled_container():
            st.markdown("###### Antal anmälda brott")
            line_chart_brott(
                vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))

    col_barchart2, col1 = st.columns(
        [5, 5], gap="small", vertical_alignment="top")
    with col_barchart2:
            with styled_container():
                st.markdown('###### Antal anmälda brott vs Stockholm')
                bar_chart_brott_2025(st.session_state.get(
                    'vald_stadsdelsomrade', 'Alla'))


if __name__ == "__main__":
    page_layout()
