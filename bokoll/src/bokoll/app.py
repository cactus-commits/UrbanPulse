import streamlit as st

pages = [
    st.Page("pages/first_page.py", title="Översikt"),
    st.Page("pages/demografi.py", title="Demografi"),
    st.Page("pages/skolor.py", title="Skolor"),
    st.Page("pages/brottsstatistik.py", title="Brottsstatistik"),
    st.Page("pages/serviceutbud.py", title="Serviceutbud")
]

pg = st.navigation(pages)

pg.run()
