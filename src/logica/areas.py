import math


class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo.
        Returns:
            float: Área calculada.
        """
        return math.pi * self.radio ** 2


class Triangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2


class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo."""
        return self.base * self.altura


class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del cuadrado."""
        return self.lado ** 2