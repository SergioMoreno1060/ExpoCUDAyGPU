import streamlit as st
from streamlit_react import ReactComponent

st.title("CUDA y GPU: Presentación")

# Cargar el componente React
presentation_cards = ReactComponent("PresentationCards.jsx")

# Renderizar el componente
presentation_cards()
