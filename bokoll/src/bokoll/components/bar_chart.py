import streamlit as st
import pandas as pd
from bokoll.utils.helpers import load_boende, load_brott_2025
import plotly.express as px
import altair as alt


def bar_chart(vald_stadsdel='Alla', vald_stadsdelsomrade='Alla'):

    df = load_boende()

    if vald_stadsdel != 'Alla':
        df = df[df['Stadsdel'] == vald_stadsdel]
    if vald_stadsdelsomrade != 'Alla':
        df = df[df['stadsdelsomrade'] == vald_stadsdelsomrade]

    aggregerat = (
        df.groupby("Upplåtelseform_Stor", as_index=False)["value"]
        .sum()
        .sort_values("value", ascending=False)
    )

    total = aggregerat["value"].sum()
    aggregerat["andel"] = (aggregerat["value"] / total) * 100

    st.bar_chart(
        aggregerat,
        x="Upplåtelseform_Stor",
        y="andel",
        x_label="",
        y_label="Andel (%)",
        color="#6B7B8C",
    )


# def bar_chart_brott_2025(vald_stadsdelsomrade='Alla'):
#     df = load_brott_2025()

#     if vald_stadsdelsomrade != 'Alla':
#         df = df[df['Stadsdelsområde'] == vald_stadsdelsomrade]
#     fig = px.bar(df, x="År", y="Stadsdelsområde")

#     fig.update_layout(xaxis_title="Antal brott")

#     st.plotly_chart(fig, use_container_width=True)

def bar_chart_brott_2025(vald_stadsdelsomrade='Alla'):
    df = load_brott_2025()
    df_total = df[df['Brottstyp'] == 'Totalt antal brott'].copy()

    fig = alt.Chart(df_total).mark_bar().encode(
        x=alt.X('År:Q', title='Antal brott'),
        y=alt.Y('Stadsdelsområde:N'),
        color=alt.condition(
            alt.datum.Stadsdelsområde == vald_stadsdelsomrade,
            alt.value('cyan'),
            alt.value('lightblue')
        )
    ).properties(width=600)

    st.altair_chart(fig, use_container_width=True)