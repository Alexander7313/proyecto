import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox

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
        self.ui.setupUi(self)

        # Conecta las acciones del menú a métodos
        self.ui.actionCirculo.triggered.connect(self.mostrar_ventana_circulo)
        self.ui.actionTriangulo.triggered.connect(self.mostrar_ventana_triangulo)
        self.ui.actionRectangulo.triggered.connect(self.mostrar_ventana_rectangulo)
        self.ui.actionCuadrado.triggered.connect(self.mostrar_ventana_cuadrado)
        self.ui.actionSalir.triggered.connect(self.close)

    def mostrar_ventana_circulo(self):
        radio, ok = QInputDialog.getDouble(self, "Área del Círculo", "Ingrese el radio:", min=0.01)
        if ok:
            figura = Circulo(radio)
            area = figura.calcular_area()
            QMessageBox.information(self, "Resultado", f"Área del círculo: {area:.2f}")

    def mostrar_ventana_triangulo(self):
        base, ok1 = QInputDialog.getDouble(self, "Área del Triángulo", "Ingrese la base:", min=0.01)
        if ok1:
            altura, ok2 = QInputDialog.getDouble(self, "Área del Triángulo", "Ingrese la altura:", min=0.01)
            if ok2:
                figura = Triangulo(base, altura)
                area = figura.calcular_area()
                QMessageBox.information(self, "Resultado", f"Área del triángulo: {area:.2f}")

    def mostrar_ventana_rectangulo(self):
        base, ok1 = QInputDialog.getDouble(self, "Área del Rectángulo", "Ingrese la base:", min=0.01)
        if ok1:
            altura, ok2 = QInputDialog.getDouble(self, "Área del Rectángulo", "Ingrese la altura:", min=0.01)
            if ok2:
                figura = Rectangulo(base, altura)
                area = figura.calcular_area()
                QMessageBox.information(self, "Resultado", f"Área del rectángulo: {area:.2f}")

    def mostrar_ventana_cuadrado(self):
        lado, ok = QInputDialog.getDouble(self, "Área del Cuadrado", "Ingrese el lado:", min=0.01)
        if ok:
            figura = Cuadrado(lado)
            area = figura.calcular_area()
            QMessageBox.information(self, "Resultado", f"Área del cuadrado: {area:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
