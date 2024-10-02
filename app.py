import streamlit as st
import streamlit.components.v1 as components

# Declare the React component
presentation_cards = components.declare_component(
    "presentation_cards",
    path="path/to/your/react/build/folder"  # Asegúrate de que esta ruta sea correcta
)

st.title("CUDA y GPU: Presentación")

# Usa el componente
presentation_cards()
