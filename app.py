import streamlit as st

presentationData = [
    {
        "title": "Introducción a CUDA y GPU",
        "content": [
            "CUDA (Compute Unified Device Architecture): Plataforma de computación paralela de NVIDIA",
            "GPU (Unidad de Procesamiento Gráfico): Hardware especializado para procesamiento paralelo",
            "CUDA permite a los desarrolladores usar GPU para cómputo de propósito general",
            "Ventajas del cómputo en GPU vs CPU: Mayor paralelismo y rendimiento en ciertas tareas"
        ]
    },
    {
        "title": "Componentes clave de hardware",
        "content": [
            "GPU compatibles con CUDA: Principalmente tarjetas NVIDIA (series GeForce, Quadro, Tesla)",
            "Arquitectura de GPU: Miles de núcleos pequeños para procesamiento paralelo",
            "Memoria de GPU: Alta velocidad, crucial para el rendimiento en cómputo",
            "Interconexión CPU-GPU: PCIe para transferencia de datos",
            "Requerimientos mínimos: Tarjeta NVIDIA compatible, suficiente RAM y PSU adecuada"
        ]
    },
    {
        "title": "Instalación y configuración",
        "content": [
            "Drivers de NVIDIA: Necesarios para la comunicación básica con la GPU",
            "CUDA Toolkit: SDK y runtime para desarrollo y ejecución de aplicaciones CUDA",
            "Pasos de instalación:",
            "1. Instalar los drivers de NVIDIA más recientes",
            "2. Descargar e instalar CUDA Toolkit del sitio de NVIDIA",
            "3. Configurar variables de entorno (PATH, LD_LIBRARY_PATH)",
            "4. Verificar la instalación con comandos como nvcc --version y deviceQuery"
        ]
    },
    {
        "title": "Librerías asociadas importantes",
        "content": [
            "cuDNN (CUDA Deep Neural Network library): Optimizada para deep learning",
            "NCCL (NVIDIA Collective Communications Library): Para comunicación multi-GPU eficiente",
            "cuBLAS: Implementación de BLAS (Basic Linear Algebra Subprograms) para GPU",
            "TensorRT: Para optimización de inferencia en deep learning",
            "OpenCV-GPU: Versión acelerada por GPU de la biblioteca de visión por computadora",
            "Thrust: Biblioteca de algoritmos paralelos similar a la STL de C++"
        ]
    },
    {
        "title": "Consideraciones de hardware",
        "content": [
            "Memoria de la GPU: Crucial para el rendimiento, determina el tamaño máximo de datos procesables",
            "Ancho de banda de memoria: Afecta la velocidad de transferencia de datos",
            "Número de núcleos CUDA: Impacta directamente en la capacidad de procesamiento paralelo",
            "Potencia de la fuente de alimentación: GPUs de alto rendimiento requieren PSUs potentes",
            "Refrigeración: Las GPUs generan mucho calor, es importante una buena refrigeración",
            "Compatibilidad de la placa base: Verificar soporte para múltiples GPUs si es necesario"
        ]
    },
    {
        "title": "Aplicaciones comunes",
        "content": [
            "Aprendizaje profundo y machine learning: Entrenamiento e inferencia de redes neuronales",
            "Procesamiento de imágenes y video: Renderizado, codificación/decodificación, filtros",
            "Simulaciones científicas: Dinámica de fluidos, modelado climático, física de partículas",
            "Criptografía y minería de criptomonedas",
            "Análisis de big data y computación de alto rendimiento",
            "Renderizado en tiempo real para videojuegos y realidad virtual"
        ]
    },
    {
        "title": "Conclusión y perspectivas futuras",
        "content": [
            "CUDA y las GPUs han revolucionado el cómputo de alto rendimiento",
            "Continuo desarrollo de arquitecturas GPU más potentes y eficientes",
            "Tendencia hacia la integración más estrecha de CPU y GPU",
            "Creciente importancia en IA, análisis de datos y computación científica",
            "Desafíos: Consumo de energía, programación paralela compleja",
            "Futuro: GPUs más especializadas, mejor soporte para precisión mixta y AI"
        ]
    }
]

st.title("CUDA y GPU: Presentación")

slide = st.select_slider(
    "Selecciona una diapositiva",
    options=range(len(presentationData)),
    format_func=lambda x: f"Slide {x+1}: {presentationData[x]['title']}"
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

# Barra de progreso
st.progress((slide + 1) / len(presentationData))
