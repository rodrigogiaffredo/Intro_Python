# Implementar o diagrama de classes: SUPERCLASSE Polígono {abstract}, ATRIBUTO qtd_lados,
# MÉTODOS perímetro() {abstract}, área() {abstract}. SUBCLASSE Quadrado, ATRIBUTO lado,
# MÉTODOS perímetro() e área(), e SUBCLASSE Circulo, ATRIBUTO raio, MÉTODOS perímetro() e
# área(). E estabelecer a relação de herança 'ÉUM' entre eles (Quadrado 'ÉUM' Polígono,
# Circulo 'ÉUM' Polígono).

from abc import ABC, abstractmethod
import math



class Poligono(ABC):

    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):

    def __init__(self, lado = 1):
        # Por ser quadrado, já defino 4 no métodos (os 4 lados do polígono)
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio = 1):
        # Partindo da premissa de que um círculo tem zero lados.
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2
