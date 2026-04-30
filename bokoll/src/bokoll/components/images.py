import streamlit as st
from bokoll.utils.helpers import load_images


def home_image(vald_stadsdelsomrade='Alla'):

    if vald_stadsdelsomrade == 'Bromma':
        load_images('bromma')
    if vald_stadsdelsomrade == 'Hägersten-Älvsjö':
        load_images('alvsjo')

    if vald_stadsdelsomrade == 'Alla':
        load_images('stockholm')
