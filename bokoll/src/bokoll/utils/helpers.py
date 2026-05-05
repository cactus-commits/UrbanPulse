import streamlit as st
import pandas as pd
from bokoll.utils.constants import DATA_PATH, IMAGE_PATH
from PIL import Image


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
    df = df[df["Upplåtelseform_Stor"].isin(
        ["Bostadsrätt", "Hyresrätt", "Äganderätt"])]
    return df


@st.cache_data
def load_map_data():
    df = pd.read_csv(
        DATA_PATH / "combined_services_for_map_cleaned.csv",  encoding='utf-8-sig')
    df['kategori'] = df['kategori'].str.replace('_', ' ').str.title()
    return df


@st.cache_data
def load_folkmangd() -> pd.DataFrame:
    df = pd.read_excel(DATA_PATH / "folkmangd_regso.xlsx")
    df = df.dropna(subset=["Region", "Ålderskategori", "value"])
    df = df[~df["Alder"].isin(["Total", "No filters applied"])]
    df = df[df['Alder'] != 'Total']
    return df.copy()  # så att den inte chachar något konstigt


@st.cache_data
def load_brott_statistik():
    df = pd.read_csv(DATA_PATH / "Antal_anmälda_brott.csv")
    df.columns = df.columns.str.strip().str.rstrip(":")
    df = df.dropna(how="all")
    df = df.rename(columns={"Område": "stadsdelsomrade"})
    return df


@st.cache_data
def load_hyresutveckling():
    df = pd.read_csv(DATA_PATH / "Hyresutveckling.csv")
    df = df.dropna(how="all")
    return df


@st.cache_data
def load_images(vald_img):
    img = Image.open(IMAGE_PATH/f'{vald_img}.png')
    st.image(img)


# Inkomstdata för Sverige (Stockholm finns med här)
@st.cache_data
def load_inkomst():
    df = pd.read_csv(DATA_PATH / "sverige_snittinkomst_2024.csv")
    return df


# Skattesatser för Sveriges kommuner
@st.cache_data
def load_skattesatser():
    df = pd.read_csv(DATA_PATH / "sverige_skattesatser_2026.csv")
    return df


# Brottsstatistik per capita
@st.cache_data
def load_brott_per_capita():
    df = pd.read_csv(DATA_PATH / "brottsstatistik_per_capita_cleaned.csv")
    return df


@st.cache_data
def load_brott_2025():
    df = pd.read_csv(DATA_PATH / "bra_alla_kommuner_2025_NY.csv")
    df["Stadsdelsområde"] = df["Stadsdelsområde"].replace(
        {"Hägersten - Älvsjö": "Hägersten-Älvsjö"})
    return df

@st.cache_data
def load_brott_befolkning():
    df = pd.read_excel(DATA_PATH / "brott_befolkning_2025.xlsx")
    return df

