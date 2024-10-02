import streamlit as st
import streamlit.components.v1 as components

st.title("CUDA y GPU: Presentación")

# Cargar el componente React
presentation_cards = ReactComponent("presentation-cards-component.tsx")

# Renderizar el componente
presentation_cards()
