import React, { useState } from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';

const presentationData = [
  {
    title: "Introducción a CUDA y GPU",
    content: [
      "Definición de CUDA y su relación con las GPU",
      "Ventajas del cómputo en GPU vs CPU"
    ]
  },
  {
    title: "Componentes clave de hardware",
    content: [
      "GPU compatibles con CUDA (NVIDIA)",
      "Requerimientos mínimos de sistema"
    ]
  },
  {
    title: "Instalación y configuración",
    content: [
      "Drivers de NVIDIA",
      "Toolkit de CUDA"
    ]
  },
  {
    title: "Librerías asociadas importantes",
    content: [
      "cuDNN para redes neuronales",
      "NCCL para comunicación multi-GPU"
    ]
  },
  {
    title: "Consideraciones de hardware",
    content: [
      "Memoria de la GPU",
      "Potencia de la fuente de alimentación"
    ]
  },
  {
    title: "Aplicaciones comunes",
    content: [
      "Aprendizaje profundo",
      "Procesamiento de imágenes y video"
    ]
  },
  {
    title: "Conclusión y perspectivas futuras",
    content: [
      "Resumen de puntos clave",
      "Futuro de CUDA y computación en GPU"
    ]
  }
];

const PresentationCards = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % presentationData.length);
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + presentationData.length) % presentationData.length);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <div className="bg-white rounded-lg shadow-lg p-6 max-w-md w-full">
        <h2 className="text-2xl font-bold mb-4 text-center text-blue-600">
          {presentationData[currentSlide].title}
        </h2>
        <ul className="list-disc pl-6 mb-4">
          {presentationData[currentSlide].content.map((item, index) => (
            <li key={index} className="mb-2">{item}</li>
          ))}
        </ul>
        <div className="flex justify-between mt-4">
          <button
            onClick={prevSlide}
            className="flex items-center justify-center p-2 rounded-full bg-blue-500 text-white hover:bg-blue-600 transition-colors"
          >
            <ChevronLeft size={24} />
          </button>
          <span className="text-gray-500">
            {currentSlide + 1} / {presentationData.length}
          </span>
          <button
            onClick={nextSlide}
            className="flex items-center justify-center p-2 rounded-full bg-blue-500 text-white hover:bg-blue-600 transition-colors"
          >
            <ChevronRight size={24} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default PresentationCards;
