import streamlit as st
import pandas as pd
from bokoll.utils.helpers import load_boende


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
