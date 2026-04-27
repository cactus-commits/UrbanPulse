import streamlit as st
import pandas as pd
from bokoll.utils.constants import DATA_PATH


@st.cache_data
def load_boende():
    df = pd.read_csv(DATA_PATH / "boende_regso.csv", sep=";", decimal=",")
    df = df.dropna(subset=["value"])
    df = df[df["Upplåtelseform_Stor"].isin(["Bostadsrätt", "Hyresrätt", "Äganderätt"])]
    return df


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