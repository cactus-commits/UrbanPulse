import streamlit as st

pg = st.navigation([
    st.Page("first_page.py", title="Översikt", default=True),
    st.Page("demografi.py", title="Demografi"),
    st.Page("skolor.py", title="Skolor"),
    st.Page("brottsstatistik.py", title="Brottsstatistik"),
    st.Page("serviceutbud.py", title="Serviceutbud"),
])

pg.run()