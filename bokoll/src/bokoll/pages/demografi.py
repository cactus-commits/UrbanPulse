from bokoll.components.filter import filter_layout
import streamlit as st
from bokoll.components.line_chart import line_chart_hyresutveckling
from bokoll.components.kpis import demografi_snittålder, demografi_invånare


def page_layout():
    st.title("Demografi")
    st.header("Filtrera på kategori och stadsdel")
    filter_df = filter_layout()

    col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")

    with col1:
        st.subheader("Hyresutveckling")
        with st.container(border=True):
            line_chart_hyresutveckling(
                vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

    with col2:
        with st.container(border=True):
            demografi_snittålder(
                vald_stadsdel=st.session_state.vald_stadsdel,
                vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
            demografi_invånare(
                vald_stadsdel=st.session_state.vald_stadsdel,
                vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)


if __name__ == "__main__":
    page_layout()