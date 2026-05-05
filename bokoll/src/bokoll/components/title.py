import pandas as pd
import streamlit as st


def get_title(base="Översikt", filter_type="main"):
    """Enkel version - returnerar 'Bas - Område'"""

    prefix = "brott_" if filter_type == "brott" else "demografi_" if filter_type == "demografi" else ""

    stadsdel = st.session_state.get(f'{prefix}vald_stadsdel', 'Alla')
    omrade = st.session_state.get(f'{prefix}vald_stadsdelsomrade', 'Alla')

    # Välj mest specifika område
    area = stadsdel if stadsdel != 'Alla' else omrade if omrade != 'Alla' else "Stockholm"

    return f"{base} - {area}"
