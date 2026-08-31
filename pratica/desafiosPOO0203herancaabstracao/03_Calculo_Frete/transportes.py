# Criar classes capazes de calcular fretes de veículos diferentes. O diagrama é a
# SUPERCLASSE Transporte {abstract}, com ATRIBUTOS distancia e frete, e MÉTODOS
# calc_frete() {abstract}. As 3 SUBCLASSES serão Moto com ATRIBUTO fator = 0.50 e MÉTODOS
# calc_frete() Caminhao ATRIBUTO fator = 1.20 METODO calc_frete() e Drone ATRIBUTO
# fator = 9.50 METODO calc_frete(). Se o frete for de Moto ele é livre (não tem distância
# mínima nem máxima). Caminhao o mínimo é 50km. Drone no máximo 10km de entrega.

from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator
        return f'R$ {self.frete:.2f}'


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return 'Recusado. Percurso abaixo do raio mínimo de 50km.'
        else:
            self.frete = self.distancia * Caminhao.fator
            return f'R$ {self.frete:.2f}'


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia > 10:
            self.frete = 0
            return 'Recusado. Percurso acima do raio máximo de 10km.'
        else:
            self.frete = self.distancia * Drone.fator
            return f'R$ {self.frete:.2f}'
