from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st
from bokoll.utils.helpers import load_folkmangd
from bokoll.utils.constants import DATA_PATH



def show_age_donut(filtered_df: pd.DataFrame):
    st.subheader("Åldersfördelning")

    folk = load_folkmangd()

    # Matcha filtret från filter_layout mot folkmängd-datan
    if filtered_df is not None and not filtered_df.empty:
        stadsdelar = filtered_df["stadsdel"].dropna().unique()
        omraden = filtered_df["stadsdelsomrade"].dropna().unique()

        mask = pd.Series(True, index=folk.index)
        if len(stadsdelar) < folk["Stadsdel"].nunique():
            mask &= folk["Stadsdel"].isin(stadsdelar)
        if len(omraden) < folk["stadsdelsomrade"].nunique():
            mask &= folk["stadsdelsomrade"].isin(omraden)

        data = folk[mask]
        rubrik = ", ".join(stadsdelar) if len(stadsdelar) <= 3 else "valt urval"
    else:
        data = folk
        rubrik = "hela staden"

    if data.empty:
        st.info("Ingen befolkningsdata för det valda urvalet.")
        return

    aggregerat = (
        data.groupby("Ålderskategori", as_index=False)["value"].sum()
    )

    ordning = ["Barn (0-19)", "Unga (20-39)", "Vuxna (40-64)", "Äldre (65+)"]

    fig = px.pie(
        aggregerat,
        names="Ålderskategori",
        values="value",
        hole=0.5,
        category_orders={"Ålderskategori": ordning},
        color_discrete_sequence=px.colors.sequential.Blues_r,
        title=f"Åldersfördelning – {rubrik}",
    )
    fig.update_traces(textposition="outside", textinfo="percent+label")
    fig.update_layout(
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.1),
        margin=dict(t=50, b=20, l=20, r=20),
    )

    st.plotly_chart(fig, use_container_width=True)