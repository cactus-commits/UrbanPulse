import streamlit as st
from bokoll.components.navigation import back_to_top
from bokoll.utils.helpers import load_images


def footer():

    with st.container(height=300, border=False):
        col1, col2, col3 = st.columns([2, 4, 2])
        with col2:
            load_images('Logotyp')
            st.markdown(
                "Skapad av STI-studenterna **Hannah Zemack**, **Christoffer Carlsson** och **Miranda Lyng**.  \n"
                "Design av **Camilla Somero**, **Cassandra Book**, **Janika Lember** och **Ramona Dusey Ahmed**."
            )
            # st.markdown("---")
            st.caption("Källor: Stockholms stad · SCB · Brå · Openstreetmap")
