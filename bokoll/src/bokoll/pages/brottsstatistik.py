import streamlit as st
from bokoll.components.kpis import kpi_brott
from bokoll.components.filter import filter_layout
from bokoll.assets.style.styling_page import styled_container
from bokoll.components.bar_chart import bar_chart_brott_2025


def page_layout():
    st.title("Brottsstatistik")
    col_filter = st.columns(1, gap="medium", vertical_alignment="center")
    with col_filter[0]:
        st.subheader("Filtrera på kategori och stadsdel")
        filter_df = filter_layout()

    col_kpi, col_2 = st.columns(
        [4, 6], gap="medium", vertical_alignment="top")
    with col_kpi:
        with styled_container():
            st.markdown(
                "###### Brottsutveckling \n Totala antal brott 2025 \n samt ökning eller minskning jämfört med 2024")
            col1, col2 = st.columns(
                2, gap="small", vertical_alignment="center")
            with col1:
                kpi_brott("Narkotikabrott", "Narkotikabrott",
                          vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
                kpi_brott("Misshandel", "Misshandel",
                          vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

            with col2:

                kpi_brott("Sexualbrott", "Sexualbrott",
                          vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
                kpi_brott("Bostadsinbrott", "Bostadsinbrott",
                          vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
    with col_2:
        with styled_container():
            st.markdown('###### Antal anmälda brott vs Stockholm')
            bar_chart_brott_2025(st.session_state.get('vald_stadsdelsomrade', 'Alla'))


if __name__ == "__main__":
    page_layout()
