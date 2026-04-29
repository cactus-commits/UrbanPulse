import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
from bokoll.utils.constants import STYLES_PATH
from bokoll.utils.helpers import read_css


st.set_page_config(layout="wide")

read_css(STYLES_PATH / "styling.css")

pages = [
    st.Page("pages/first_page.py", title="Översikt"),
    st.Page("pages/demografi.py", title="Demografi"),
    # st.Page("pages/skolor.py", title="Skolor"),
    st.Page("pages/brottsstatistik.py", title="Brottsstatistik"),
    # st.Page("pages/serviceutbud.py", title="Serviceutbud")
]

pg = st.navigation(pages)

pg.run()
