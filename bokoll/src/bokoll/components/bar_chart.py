import streamlit as st
import pandas as pd
from bokoll.utils.helpers import load_boende


def bar_chart():
    st.subheader("Boendeform")

    df = load_boende()

    aggregerat = (
        df.groupby("Upplåtelseform_Stor", as_index=False)["value"]
        .sum()
        .sort_values("value", ascending=False)
    )

    # Räkna om till procent av totalen
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