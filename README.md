# 📐 Calculadora de Áreas

## 📋 Descripción

Este proyecto es una aplicación de escritorio desarrollada en **Python** con **PyQt6**. Permite calcular el área de figuras geométricas básicas mediante una interfaz gráfica intuitiva.

El usuario puede seleccionar una figura desde el menú y luego ingresar sus dimensiones para obtener el área correspondiente.

### Figuras disponibles:
- Círculo
- Triángulo
- Rectángulo
- Cuadrado

---

## ⚙️ Dependencias

Este proyecto requiere:

- Python 3.10 o superior
- PyQt6

Puedes instalar las dependencias usando `pip`:

```bash
pip install PyQt6
```

También puedes usar un `requirements.txt` si lo tienes:

```bash
pip install -r requirements.txt
```

---

## 📁 Estructura del proyecto

```
Proyecto/
├── app.py             # Archivo principal de ejecución
├── README.md          # Documento de descripción del proyecto
├── .venv/             # Entorno virtual (excluido con .gitignore)
└── src/
    ├── logica/
    │   └── areas.py   # Lógica para el cálculo de áreas de figuras geométricas
    └── vista/
        └── ui_main.py # Interfaz gráfica generada desde Qt Designer (.ui convertido a .py)
```

---

## ▶️ ¿Cómo usar la aplicación?

### 1. Clona el repositorio

```bash
git clone https://github.com/Alexander7313/proyecto.git
cd proyecto
```

### 2. (Opcional) Crea un entorno virtual

```bash
python -m venv .venv
```

### 3. Activa el entorno virtual

- En Windows:
  ```bash
  .\.venv\Scriptsctivate
  ```

- En Linux/macOS:
  ```bash
  source .venv/bin/activate
  ```

### 4. Instala las dependencias

```bash
pip install PyQt6
```

### 5. Ejecuta la aplicación

```bash
python app.py
```

---

## 👥 Integrantes del equipo

| Nombre completo                      | Rol            |
|--------------------------------------|----------------|
| Landa Rojas Alexander Nelson         | Desarrollador  |
| Salvador Rivera Bruce Joshua         | Desarrollador  |

---

## 📂 .gitignore recomendado

Para evitar subir archivos innecesarios, crea un archivo `.gitignore` con lo siguiente:

```
# Entornos virtuales
.venv/
env/
venv/

# Archivos de Python
__pycache__/
*.pyc

# Archivos de PyQt / Qt Designer
*.ui~
*.qmlc
*.qrc~

# Archivos de IDEs
.idea/
.vscode/

# Archivos de sistema
.DS_Store
Thumbs.db
```

---


