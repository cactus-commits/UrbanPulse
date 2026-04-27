import streamlit as st
import pandas as pd
from bokoll.components.map import show_map
from bokoll.components.filter import filter_layout


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
    filter_map = filter_layout()
    show_map(filter_map)
    
