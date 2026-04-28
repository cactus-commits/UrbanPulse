import streamlit as st
import pandas as pd
from bokoll.utils.constants import DATA_PATH


def read_textfile(path):
    with open(path) as file:
        return file.read()


def read_css(path):
    css = read_textfile(path)
    st.write(
        f"<style>{css}</style>", unsafe_allow_html=True
    )


@st.cache_data
def load_boende():
    df = pd.read_csv(DATA_PATH / "boende_regso.csv", sep=";", decimal=",")
    df = df.dropna(subset=["value"])
    df = df[df["Upplåtelseform_Stor"].isin(["Bostadsrätt", "Hyresrätt", "Äganderätt"])]
    return df

@st.cache_data
def load_map_data():
    df = pd.read_csv(DATA_PATH / "combined_services_for_map.csv",  encoding='utf-8-sig')
    return df

@st.cache_data
def load_folkmangd() -> pd.DataFrame:
    df = pd.read_excel(DATA_PATH / "folkmangd_regso.xlsx")
    df = df.dropna(subset=["Region", "Ålderskategori", "value"])
    df = df[~df["Alder"].isin(["Total", "No filters applied"])]
    return df