import streamlit as st
# import pandas as pd
from bokoll.components.map import show_map
from bokoll.components.filter import filter_layout
from bokoll.assets.style.styling_page import columns_layout


if __name__ == "__main__":
    filter_map = filter_layout()
    show_map(filter_map)
