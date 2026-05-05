from bokoll.utils.helpers import load_brott_per_capita  # eller din datakälla
import pandas as pd
import plotly.express as px
import streamlit as st
import altair as alt

from bokoll.utils.helpers import load_boende, load_brott_2025, load_brott_per_capita
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
    ).properties(width=600, height=350).configure_axis(
        grid=False  # Ta bort grid lines
    )

    st.altair_chart(fig, use_container_width=True)


def bar_chart_type_of_crime(vald_stadsdelsomrade='Alla'):
    # Ladda rådata
    df_raw = load_brott_per_capita()

    # 1. Omvandla från Wide till Long format direkt
    # Detta gör att vi får en kolumn 'År' och en kolumn 'Antal'
    df = df_raw.melt(
        id_vars=['Brottstyp', 'område'],
        value_vars=['2023', '2024', '2025'],
        var_name='År',
        value_name='Antal'
    )

    # 2. Filtrera data om specifikt område är valt
    # Notera: Använder 'område' som matchar din data
    if vald_stadsdelsomrade != 'Alla':
        df = df[df['område'] == vald_stadsdelsomrade]

    # 3. Skapa stapeldiagram
    fig = alt.Chart(df).mark_bar().encode(
        x=alt.X(
            'Brottstyp:N',
            title='Visar antalet polisanmälda brott per brottstyp (per 100 000 invånare)',
            axis=alt.Axis(
                labelAngle=-45,
                labelAlign='right'
            )
        ),
        y=alt.Y(
            'sum(Antal):Q',  # Använder sum() för att hantera 'Alla'-valet
            title='Antal brott',
            axis=alt.Axis(
                format='.0f'
            )
        ),
        color=alt.Color(
            'År:N',
            scale=alt.Scale(
                domain=['2023', '2024', '2025'],
                range=['#6B8E7C', '#A2C1C6', '#E39D4D']
            ),
            legend=alt.Legend(title="År")
        ),
        xOffset='År:N'  # Grupperar staplarna snyggt
    ).properties(
        width=800,
        height=350
    ).configure_view(
        strokeWidth=0
    )

    st.altair_chart(fig, use_container_width=True)
