import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from bokoll.utils.helpers import load_folkmangd
from bokoll.assets.style.style_spider import ORDNING, styla_spider


# Mappning från SCB-åldersgrupper till de bredare grupperna i diagrammet
ALDERSGRUPPER_10 = {
    "0-9":   ["0-4 år", "5-9 år"],
    "10-19": ["10-14 år", "15-19 år"],
    "20-29": ["20-24 år", "25-29 år"],
    "30-39": ["30-34 år", "35-39 år"],
    "40-49": ["40-44 år", "45-49 år"],
    "50-59": ["50-54 år", "55-59 år"],
    "60-69": ["60-64 år", "65-69 år"],
    "70-79": ["70-74 år", "75-79 år"],
    "80+":   ["80- år"],
}


def show_age_spider(filtered_df):
    # Hämta all folkmängdsdata
    folk = load_folkmangd()

    # Filtrera ned till valt område
    if filtered_df is not None and not filtered_df.empty:
        stadsdelar = filtered_df["stadsdel"].dropna().unique()
        omraden = filtered_df["stadsdelsomrade"].dropna().unique()

        filter_mask = pd.Series(True, index=folk.index)

        if len(stadsdelar) < folk["Stadsdel"].nunique():
            filter_mask = filter_mask & folk["Stadsdel"].isin(stadsdelar)

        if len(omraden) < folk["stadsdelsomrade"].nunique():
            filter_mask = filter_mask & folk["stadsdelsomrade"].isin(omraden)

        data = folk[filter_mask]
    else:
        data = folk

    # Visa meddelande om ingen data hittades
    if data.empty:
        st.info("Ingen befolkningsdata för det valda urvalet.")
        return

    # Räkna ihop antal personer per 10-årsgrupp
    varden = []
    for grupp, ingaende_aldrar in ALDERSGRUPPER_10.items():
        antal = data[data["Alder"].isin(ingaende_aldrar)]["value"].sum()
        varden.append(antal)

    # Skapa spider chart
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=varden,
        theta=ORDNING,
        name="Antal personer",
    ))

    # Lägg på styling
    fig = styla_spider(fig)

    # Visa diagrammet i Streamlit
    st.plotly_chart(fig, use_container_width=True)