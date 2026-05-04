import pandas as pd
import plotly.express as px
import streamlit as st

from bokoll.utils.helpers import load_folkmangd
from bokoll.assets.style.style_donut import FARGER, ORDNING, styla_donut


def show_age_donut(filtered_df):
    # Hämta all folkmängdsdata
    folk = load_folkmangd()

    # Filtrera ned till valt område
    if filtered_df is not None and not filtered_df.empty:
        stadsdelar = filtered_df["stadsdel"].dropna().unique()
        omraden = filtered_df["stadsdelsomrade"].dropna().unique()

        # Bygg ett filter steg för steg
        filter_mask = pd.Series(True, index=folk.index)

        if len(stadsdelar) < folk["Stadsdel"].nunique():
            filter_mask = filter_mask & folk["Stadsdel"].isin(stadsdelar)

        if len(omraden) < folk["stadsdelsomrade"].nunique():
            filter_mask = filter_mask & folk["stadsdelsomrade"].isin(omraden)

        data = folk[filter_mask]

        # Skapa rubrik baserat på antal valda områden
        if len(stadsdelar) <= 3:
            rubrik = ", ".join(stadsdelar)
        else:
            rubrik = "valt urval"
    else:
        data = folk
        rubrik = "hela staden"

    # Visa meddelande om ingen data hittades
    if data.empty:
        st.info("Ingen befolkningsdata för det valda urvalet.")
        return

    # Räkna ihop antal personer per åldersgrupp
    aggregerat = data.groupby("Ålderskategori", as_index=False)["value"].sum()
    total_antal = int(aggregerat["value"].sum())

    # Skapa donut-diagrammet
    fig = px.pie(
        aggregerat,
        names="Ålderskategori",
        values="value",
        hole=0.6,
        category_orders={"Ålderskategori": ORDNING},
        color="Ålderskategori",
        color_discrete_map=FARGER,
        title=f"Åldersfördelning – {rubrik}",
        height=350
    )

    # Lägg på all styling från style_donut
    fig = styla_donut(fig, total_antal)

    # Visa diagrammet i Streamlit
    st.plotly_chart(fig, use_container_width=True)