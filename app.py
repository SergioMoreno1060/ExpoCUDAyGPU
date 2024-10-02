import streamlit as st

presentationData = [
    {
        "title": "Introducción a CUDA y GPU",
        "content": [
            "Definición de CUDA y su relación con las GPU",
            "Ventajas del cómputo en GPU vs CPU"
        ]
    },
    {
        "title": "Componentes clave de hardware",
        "content": [
            "GPU compatibles con CUDA (NVIDIA)",
            "Requerimientos mínimos de sistema"
        ]
    },
    {
        "title": "Instalación y configuración",
        "content": [
            "Drivers de NVIDIA",
            "Toolkit de CUDA"
        ]
    },
    {
        "title": "Librerías asociadas importantes",
        "content": [
            "cuDNN para redes neuronales",
            "NCCL para comunicación multi-GPU"
        ]
    },
    {
        "title": "Consideraciones de hardware",
        "content": [
            "Memoria de la GPU",
            "Potencia de la fuente de alimentación"
        ]
    },
    {
        "title": "Aplicaciones comunes",
        "content": [
            "Aprendizaje profundo",
            "Procesamiento de imágenes y video"
        ]
    },
    {
        "title": "Conclusión y perspectivas futuras",
        "content": [
            "Resumen de puntos clave",
            "Futuro de CUDA y computación en GPU"
        ]
    }
]

st.title("CUDA y GPU: Presentación")

slide = st.select_slider(
    "Selecciona una diapositiva",
    options=range(len(presentationData)),
    format_func=lambda x: f"Slide {x+1}"
)

current_slide = presentationData[slide]
st.header(current_slide["title"])
for point in current_slide["content"]:
    st.markdown(f"• {point}")

# Botones de navegación
col1, col2, col3 = st.columns(3)
with col1:
    if slide > 0:
        if st.button("⬅️ Anterior"):
            slide -= 1
with col3:
    if slide < len(presentationData) - 1:
        if st.button("Siguiente ➡️"):
            slide += 1
