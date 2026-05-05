import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from bokoll.utils.constants import DATA_PATH
from bokoll.assets.style.style_radar import (
    LINJEFARG_VAL, FYLLNAD_VAL,
    LINJEFARG_REF, FYLLNAD_REF,
    INDIKATORER, styla_radar,
)


# Mappning från långa kolumnnamn till kortare etiketter
KOLUMN_TILL_LABEL = {
    "Andelen med ekonomiskt bistånd och/eller långtidsarbetslösa": "Ekonomiskt bistånd",
    "Andelen med förgymnasial utbildning": "Förgymnasial utbildning",
    "Andelen personer med låg ekonomisk standard (oavsett ålder)": "Låg ekonomisk standard",
}


def radar_omrade_val(demografi_vald_stadsdelsomrade="Alla"):
    options = ["Bromma", "Hägersten-Älvsjö"]

    # Init
    if "radar_omrade_val" not in st.session_state:
        st.session_state["radar_omrade_val"] = demografi_vald_stadsdelsomrade

    # Sync från huvudfilter → radar (innan widget skapas)
    st.session_state["radar_omrade_val"] = st.session_state.get(
        "demografi_vald_stadsdelsomrade", options[0]
    )

    # Callback: radar → huvudfilter
    def sync_to_main():
        st.session_state["demografi_vald_stadsdelsomrade"] = st.session_state["radar_omrade_val"]

    valt_omrade = st.selectbox(
        "Område",
        options=options,
        key="radar_omrade_val",
        label_visibility="collapsed",
        on_change=sync_to_main,  # 🔥 här sker syncen korrekt
    )

    return valt_omrade


def show_radar_socio(valt_omrade):
    # Hämta socioekonomisk data
    df = pd.read_csv(DATA_PATH / "stockholm_socioekonomiskt_2024.csv")

    # Räkna ut Stockholm-snittet
    snitt_stockholm = []
    for kolumn in KOLUMN_TILL_LABEL:
        snitt_stockholm.append(df[kolumn].mean())

    # Räkna ut värden för valt område
    df_valt = df[df["stadsdelsomrade"] == valt_omrade]

    if df_valt.empty:
        st.info("Ingen data för valt område.")
        return

    valda_varden = []
    for kolumn in KOLUMN_TILL_LABEL:
        valda_varden.append(df_valt[kolumn].mean())

    # Skapa radarn
    fig = go.Figure()

    # Stockholm-referens (orange streckad)
    fig.add_trace(go.Scatterpolar(
        r=snitt_stockholm + [snitt_stockholm[0]],
        theta=INDIKATORER + [INDIKATORER[0]],
        name="Stockholm (snitt)",
        line=dict(color=LINJEFARG_REF, width=2, dash="dash"),
        fillcolor=FYLLNAD_REF,
        fill="toself",
        marker=dict(size=6, color=LINJEFARG_REF),
    ))

    # Valt område (mörkgrön)
    fig.add_trace(go.Scatterpolar(
        r=valda_varden + [valda_varden[0]],
        theta=INDIKATORER + [INDIKATORER[0]],
        name=valt_omrade,
        line=dict(color=LINJEFARG_VAL, width=2),
        fillcolor=FYLLNAD_VAL,
        fill="toself",
        marker=dict(size=6, color=LINJEFARG_VAL),
    ))

    # Beräkna max-värde för axeln
    max_value = max(snitt_stockholm + valda_varden) * 1.1

    # Lägg på styling
    fig = styla_radar(fig, max_value)

    st.plotly_chart(fig, use_container_width=True)