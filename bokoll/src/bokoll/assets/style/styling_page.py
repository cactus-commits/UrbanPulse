import streamlit as st

def styled_container(bg_color: str = "#FEFEFE", radius: str = "16px", padding: str = "10px", border: bool = False, height=None):
    
    st.markdown(
        f"""
        <style>
        div.st-emotion-cache-18kf3ut.e1rw0b1u4 > div {{
            background-color: {bg_color} !important;
            border-radius: {radius} !important;
            padding: {padding} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    if height is not None:
        return st.container(border=border, height=height)
    return st.container(border=border)