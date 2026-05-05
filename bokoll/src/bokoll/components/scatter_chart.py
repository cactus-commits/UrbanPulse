import streamlit as st
from bokoll.utils.helpers import load_brott_befolkning
import plotly.express as px

def scatter_brott_befolkning():
    df = load_brott_befolkning()
    df.columns = ["Brottstyp", "Antal brott", "Område", "Barn", "Unga", "Vuxna", "Äldre", "Totalt"]
 
    st.title("Brott per capita 2025")
 
    fig = px.scatter(df, x="Brottstyp", y="Antal brott", color="Område")
    st.plotly_chart(fig)
