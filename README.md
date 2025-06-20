# Proyecto: Calculadora de Áreas

## 📋 Descripción

Este proyecto es una **aplicación gráfica en Python** desarrollada con **PyQt6**, que permite al usuario calcular el área de distintas figuras geométricas básicas de forma sencilla e interactiva.

Las figuras disponibles en el menú son:

- Círculo
- Triángulo
- Rectángulo
- Cuadrado

El usuario selecciona una figura desde el menú, ingresa las dimensiones requeridas (como radio, base o altura) mediante cuadros de diálogo, y recibe el resultado del área calculada.

## ⚙️ Tecnologías usadas

- Python 3.10+
- PyQt6
- Qt Designer (para generar la interfaz gráfica)
- Git (control de versiones)

## 📁 Estructura del proyecto
'''
Proyecto/
├── app.py # Archivo principal de ejecución
├── README.md # Documento de descripción del proyecto
├── .venv/ # Entorno virtual (excluido con .gitignore)
└── src/
├── logica/
│ └── areas.py # Lógica para el cálculo de áreas de figuras geométricas
└── vista/
└── ui_main.py # Interfaz gráfica generada desde Qt Designer (.ui convertido a .py)
'''
