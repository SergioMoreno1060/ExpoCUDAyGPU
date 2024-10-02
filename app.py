import streamlit as st
from streamlit_components_react import ReactComponent

st.title("CUDA y GPU: Presentación")

# Cargar el componente React
presentation_cards = ReactComponent("presentation-cards-component.tsx")

# Renderizar el componente
presentation_cards()
