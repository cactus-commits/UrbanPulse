import pandas as pd
import plotly.express as px
import streamlit as st

from bokoll.utils.helpers import load_folkmangd
from bokoll.assets.style.style_bar_befolkning import (
    FARGER, ORDNING, styla_bar_befolkning
)


# Vi grupperar SCB:s 5-årsåldrar till bredare 10-årsgrupper för läsbarhet
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


def bar_chart_befolkning(filtered_df):
    folk = load_folkmangd()

    # Filtrera på valt område från slicern
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

    if data.empty:
        st.info("Ingen befolkningsdata för det valda urvalet.")
        return

    # Räkna ihop antal personer per 10-årsgrupp
    rader = []
    for grupp, ingaende_aldrar in ALDERSGRUPPER_10.items():
        antal = data[data["Alder"].isin(ingaende_aldrar)]["value"].sum()
        rader.append({"Aldersgrupp": grupp, "Antal": antal})

    aggregerat = pd.DataFrame(rader)

    # Bygg själva diagrammet med Plotly
    fig = px.bar(
        aggregerat,
        x="Aldersgrupp",
        y="Antal",
        color="Aldersgrupp",
        color_discrete_map=FARGER,
        category_orders={"Aldersgrupp": ORDNING},
    )

    # Lägg på all styling från style-filen
    fig = styla_bar_befolkning(fig)

    st.plotly_chart(fig, use_container_width=True)