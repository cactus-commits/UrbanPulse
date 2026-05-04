import pandas as pd
import plotly.express as px
import streamlit as st
import altair as alt

from bokoll.utils.helpers import load_boende, load_brott_2025
from bokoll.assets.style.style_bar import FARGER, bygg_bar

def bar_chart(demografi_vald_stadsdel="Alla", demografi_vald_stadsdelsomrade="Alla"):
    df = load_boende()

    if demografi_vald_stadsdel != "Alla":
        df = df[df["Stadsdel"] == demografi_vald_stadsdel]
    if demografi_vald_stadsdelsomrade != "Alla":
        df = df[df["stadsdelsomrade"] == demografi_vald_stadsdelsomrade]

    aggregerat = (
        df.groupby("Upplåtelseform_Stor", as_index=False)["value"]
        .sum()
        .sort_values("value", ascending=False)
    )

    if aggregerat.empty:
        st.info("Ingen boendedata för det valda urvalet.")
        return

    chart = bygg_bar(aggregerat)
    st.altair_chart(chart, use_container_width=True)


def bar_chart_brott_2025(vald_stadsdelsomrade='Alla'):
    df = load_brott_2025()
    df_total = df[df['Brottstyp'] == 'Totalt antal brott'].copy()


    fig = alt.Chart(df_total).mark_bar().encode(
        x=alt.X('År:Q', title='Antal brott'),
        y=alt.Y('Stadsdelsområde:N'),
        color=alt.condition(
            alt.datum.Stadsdelsområde == vald_stadsdelsomrade,
            alt.value('#E39D4D'),
            alt.value('#A2C1C6')
        )
    ).properties(width=600).configure_axis(
        grid=False  # Ta bort grid lines
    )

    st.altair_chart(fig, use_container_width=True)
