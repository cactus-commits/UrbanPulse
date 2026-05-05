import streamlit as st
from bokoll.components.navigation import back_to_top
from bokoll.utils.helpers import load_images

def footer():
    st.markdown("---")
    back_to_top()
    with st.container(height=200):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            load_images('Logotyp')
            st.markdown(
                "Skapad av STI-studenterna **Hannah Zemack**, **Christoffer Carlsson** och **Miranda Lyng**.  \n"
                "Design av **Camilla Somero**, **Cassandra Book**, **Janika Lember** och **Ramona Dusey Ahmed**."
            )
            st.markdown("---")
            st.caption("Källor: Stockholms stad · SCB · Brå · Openstreetmap")
    

