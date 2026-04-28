import streamlit as st
from bokoll.utils.helpers import load_map_data
import pandas as pd


def dataTable(filter_df):

    st.dataframe(
        filter_df[['namn', 'kategori', 'stadsdel', 'stadsdelsomrade']].rename(columns={
            'namn': 'Namn',
            'kategori': 'Kategori',
            'stadsdel': 'Stadsdel',
            'stadsdelsomrade': 'Stadsdelsområde'
        }),
        hide_index=True,
        height=213
    )
