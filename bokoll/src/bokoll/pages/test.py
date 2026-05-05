import streamlit as st
import pandas as pd
from bokoll.components.map import show_map
from bokoll.components.filter import filter_layout, filter_brott, filter_demografi, filter_kategori_only, filter_radar
from bokoll.components.donut import show_age_donut
from bokoll.components.bar_chart import bar_chart, bar_chart_brott_2025, bar_chart_type_of_crime
from bokoll.components.bar_chart_befolkning import bar_chart_befolkning
from bokoll.components.kpis import total_boende_kpi, antal_skolor, total_service_kpi, kpi_brott, demografi_snittålder, demografi_invånare, demografi_inkomst, demografi_skattesats
from bokoll.components.line_chart import line_chart_brott, line_chart_hyresutveckling
from bokoll.components.table import dataTable
from bokoll.components.images import home_image
from bokoll.assets.style.styling_page import styled_container
from bokoll.components.navigation import nav_buttons, section_anchor, back_to_top
from bokoll.utils.helpers import load_images
from bokoll.components.footer import footer
from bokoll.components.title import get_title
from bokoll.components.radar_socio import show_radar_socio


def page_layout():
    section_anchor("toppen")
    section_anchor("oversikt")
    load_images("Logotyp")
    col_header1, col_header2, col_header3 = st.columns(3)
    with col_header1:
        st.markdown(get_title("### Översikt", "main"))
    with col_header3:
        nav_buttons()
    # st.markdown(
    #     "# BoKoll - Få en koll på boende, service och brott i Stockholms stadsdelar")
    # Lägg till en horisontell linje för att separera sektionerna
    # st.markdown("---")

    col_filter, col_2 = st.columns(2, gap="medium", vertical_alignment="top")
    with col_filter:
        #st.markdown("###### Filtrera på stadsdel och område")
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
                                 # kanske borde bytas till något annat
                                 vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
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

    col_kategori, col_2 = st.columns(2)
    with col_kategori:
        #st.markdown("###### Filtrera på kategori")
        filter_df = filter_kategori_only()

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


    section_anchor("demografi")
    # Lägg till en horisontell linje för att separera sektionerna
    st.markdown("---")
    col_demografi1, col_demografi2, col_demografi3 = st.columns(3)
    with col_demografi1:
        st.markdown(get_title("### Demografi", "demografi"))
    with col_demografi3:
        nav_buttons()

    col_filter, col_2= st.columns(2, gap="medium", vertical_alignment="top")
    with col_filter:
        #st.markdown("###### Filtrera på stadsdel och område")
        filter_df = filter_demografi()

    rad1_col1, rad1_col2 = st.columns(2, gap="medium")

    with rad1_col1:
        with st.container(border=False):
            st.subheader("Hyresutveckling")
            line_chart_hyresutveckling(
                demografi_vald_stadsdelsomrade=st.session_state.demografi_vald_stadsdelsomrade)

    with rad1_col2:
        with st.container(border=False):
            st.subheader("Demografi i korthet")

            # 2x2-grid med fyra KPI:er
            kpi_col1, kpi_col2 = st.columns(2, gap="small")
            with kpi_col1:
                demografi_snittålder(
                    demografi_vald_stadsdel=st.session_state.demografi_vald_stadsdel,
                    demografi_vald_stadsdelsomrade=st.session_state.demografi_vald_stadsdelsomrade)
            with kpi_col2:
                demografi_invånare(
                    demografi_vald_stadsdel=st.session_state.demografi_vald_stadsdel,
                    demografi_vald_stadsdelsomrade=st.session_state.demografi_vald_stadsdelsomrade)

            kpi_col3, kpi_col4 = st.columns(2, gap="small")
            with kpi_col3:
                demografi_inkomst(
                    demografi_vald_stadsdel=st.session_state.demografi_vald_stadsdel,
                    demografi_vald_stadsdelsomrade=st.session_state.demografi_vald_stadsdelsomrade)
            with kpi_col4:
                demografi_skattesats(
                    demografi_vald_stadsdel=st.session_state.demografi_vald_stadsdel,
                    demografi_vald_stadsdelsomrade=st.session_state.demografi_vald_stadsdelsomrade)

    col_donut, col_barchart = st.columns(
        [5, 5], gap="small", vertical_alignment="top")

    with col_donut:
        with styled_container():
            st.markdown("###### Befolkningsmängd")
            show_age_donut(filter_df)

    with col_barchart:
        with styled_container():
            st.markdown("###### Boendeform")
            bar_chart(demografi_vald_stadsdel=st.session_state.demografi_vald_stadsdel,
                      demografi_vald_stadsdelsomrade=st.session_state.demografi_vald_stadsdelsomrade)


    with st.container(border=False):

        st.markdown("###### Socioekonomisk profil")
        col_filter, col_2 = st.columns(2, gap="medium", vertical_alignment="top")
        with col_filter:
            filter_radar()
        show_radar_socio(st.session_state.get('radar_vald_stadsdelsomrade', 'Alla'))


##############################################################
    section_anchor("brott")
    # Lägg till en horisontell linje för att separera sektionerna
    st.markdown("---")
    col_brott1, col_brott2, col_brott3 = st.columns(3)
    with col_brott1:
        st.markdown(get_title("### Brottsstatistik", "brott"))
    with col_brott3:
        nav_buttons()

    col_filter, col_2 = st.columns(2, gap="medium", vertical_alignment="top")
    with col_filter:
        #st.markdown("###### Filtrera på område")
        filter_df = filter_brott()

    col_kpi_brott, col_linechart = st.columns(
        [4, 6], gap="medium", vertical_alignment="top")
    with col_kpi_brott:
        with styled_container():
            st.markdown(
                "###### Brottsutveckling \n Totala antal brott 2025 \n samt ökning eller minskning jämfört med 2024")
            col1, col2 = st.columns(
                2, gap="small", vertical_alignment="center", border=False)
            with col1:
                kpi_brott(("Narkotikabrott"), "Narkotikabrott",
                          brott_vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))
                kpi_brott("Misshandel", "Misshandel",
                          brott_vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))

            with col2:
                kpi_brott("Sexualbrott", "Sexualbrott",
                          brott_vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))
                kpi_brott("Bostadsinbrott", "Bostadsinbrott",
                          brott_vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))

    with col_linechart:
        with styled_container():
            st.markdown("###### Antal anmälda brott")
            line_chart_brott(
                brott_vald_stadsdelsomrade=st.session_state.get('brott_vald_stadsdelsomrade', 'Alla'))

    col_barchart2, col1 = st.columns(
        [5, 5], gap="small", vertical_alignment="top")
    with col_barchart2:
        with styled_container():
            st.markdown('###### Antal anmälda brott vs Stockholm')
            bar_chart_brott_2025(st.session_state.get(
                'brott_vald_stadsdelsomrade', 'Alla'))
    with col1:
        with styled_container():
            st.markdown('###### Typ av anmälda brott')
            bar_chart_type_of_crime(st.session_state.get(
                'brott_vald_stadsdelsomrade', 'Alla'))

    back_to_top()
    st.markdown("---")
    footer()


if __name__ == "__main__":
    page_layout()
