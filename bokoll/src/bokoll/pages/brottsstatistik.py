import streamlit as st
from bokoll.components.kpis import kpi_brott
from bokoll.components.filter import filter_layout

def page_layout():
    st.title("Brottsstatistik")
    st.header("Filtrera på kategori och stadsdel")

    col_filter = st.columns(1, gap="medium", vertical_alignment="center")
    with col_filter[0]:
        st.subheader("Filtrera på kategori och stadsdel")
        filter_df = filter_layout()

    kpi_brott("Narkotikabrott", "Narkotikabrott", vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
    kpi_brott("Misshandel", "Misshandel", vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)


if __name__ == "__main__":
    page_layout()