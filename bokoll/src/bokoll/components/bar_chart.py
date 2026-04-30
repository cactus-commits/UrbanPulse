import pandas as pd
import plotly.express as px
import streamlit as st

from bokoll.utils.helpers import load_boende
from bokoll.assets.style.style_bar import FARGER, styla_bar


def bar_chart(vald_stadsdel="Alla", vald_stadsdelsomrade="Alla"):
    # Hämta boendedata
    df = load_boende()

    # Filtrera ned till valt område
    if vald_stadsdel != "Alla":
        df = df[df["Stadsdel"] == vald_stadsdel]
    if vald_stadsdelsomrade != "Alla":
        df = df[df["stadsdelsomrade"] == vald_stadsdelsomrade]

    # Räkna ihop totalsumma per upplåtelseform
    aggregerat = (
        df.groupby("Upplåtelseform_Stor", as_index=False)["value"]
        .sum()
        .sort_values("value", ascending=False)
    )

    # Visa meddelande om ingen data hittades
    if aggregerat.empty:
        st.info("Ingen boendedata för det valda urvalet.")
        return

    # Skapa stapeldiagrammet
    fig = px.bar(
        aggregerat,
        x="Upplåtelseform_Stor",
        y="value",
        color="Upplåtelseform_Stor",
        color_discrete_map=FARGER,
    )

    # Lägg på all styling från style_bar
    fig = styla_bar(fig)

    # Visa diagrammet i Streamlit
    st.plotly_chart(fig, use_container_width=True)