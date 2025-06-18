import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow

# Configuración absoluta de paths
PROJECT_ROOT = Path(__file__).parent
SRC_DIR = PROJECT_ROOT / "src"

# Añade todas las posibles rutas necesarias
sys.path.extend([
    str(PROJECT_ROOT),
    str(SRC_DIR),
    str(SRC_DIR / "vista"),
    str(SRC_DIR / "logica")
])

# Sistema de importación robusto
try:
    # Intento 1: Importación estándar
    from src.vista.ui_main import Ui_MainWindow
    from src.logica.areas import Circulo, Triangulo, Rectangulo, Cuadrado
except ImportError:
    try:
        # Intento 2: Importación alternativa
        from vista.ui_main import Ui_MainWindow
        from logica.areas import Circulo, Triangulo, Rectangulo, Cuadrado
    except ImportError as e:
        print("\nERROR CRÍTICO: No se pudo importar los módulos")
        print("Paths de búsqueda actuales:")
        for p in sys.path:
            print(f"- {p}")
        print("\nArchivos encontrados en src/vista/:")
        vista_dir = SRC_DIR / "vista"
        if vista_dir.exists():
            for f in vista_dir.iterdir():
                print(f"- {f.name}")
        else:
            print("¡La carpeta src/vista/ no existe!")
        raise

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setup