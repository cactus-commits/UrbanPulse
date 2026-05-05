import streamlit as st

NAV_STYLE = """
    display: flex;
    gap: 12px;
    margin: 8px 0;
"""

BUTTON_STYLE = """
    padding: 6px 16px;
    border-radius: 8px;
    background: #003F47;
    color: white;
    font-size: 14px;
    border: none;
    box-shadow: none;
    cursor: pointer;
"""

def nav_buttons():
    """Navigationsknappar till varje sektion."""
    st.markdown(f"""
        <div style="{NAV_STYLE}">
            <a href="#oversikt"  style="text-decoration:none"><button style="{BUTTON_STYLE}">Översikt</button></a>
            <a href="#demografi" style="text-decoration:none"><button style="{BUTTON_STYLE}">Demografi</button></a>
            <a href="#brott"     style="text-decoration:none"><button style="{BUTTON_STYLE}">Brottsstatistik</button></a>
        </div>
    """, unsafe_allow_html=True)


def back_to_top():
    """Tillbaka till toppen-knapp."""
    st.markdown(f"""
        <div style="text-align: center; padding: 8px 0 16px;">
            <a href="#toppen" style="text-decoration:none">
                <button style="{BUTTON_STYLE}">Tillbaka till toppen</button>
            </a>
        </div>
    """, unsafe_allow_html=True)


def section_anchor(anchor_id: str):
    """Osynlig anchor-punkt för en sektion."""
    st.markdown(f'<a name="{anchor_id}"></a>', unsafe_allow_html=True)