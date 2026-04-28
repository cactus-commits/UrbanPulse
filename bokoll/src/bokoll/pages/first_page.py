import streamlit as st
import pandas as pd
from bokoll.components.map import show_map
from bokoll.components.filter import filter_layout
from bokoll.components.donut import show_age_donut
from bokoll.components.bar_chart import bar_chart
from bokoll.components.kpis import total_boende_kpi


def page_layout():
    st.title("Översikt")
    st.header("Filtrera på kategori och stadsdel")


# def columns_layout():
#     col1, col2 = st.columns(2, gap="medium", vertical_alignment="center")

#     with col1:

#         filter_map = filter_layout()

#     with col2:
#         show_map(filter_map)



if __name__ == "__main__":
    page_layout()
    filter_df = filter_layout()
    total_boende_kpi(vald_stadsdel=st.session_state.vald_stadsdel, vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
    show_map(filter_df)
    show_age_donut(filter_df)
    bar_chart(vald_stadsdel=st.session_state.vald_stadsdel, vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

