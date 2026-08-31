# Simular uma cafeteria orientada a objetos, a nossa prepara café, chá e leite. A
# SUPERCLASSE BebidaQuente {abstract} com os MÉTODOS preparar() {concreto}, ferver_agua()
# {concreto}, misturar() {abstract} e servir() {abstract}. As 3 SUBCLASSES são Café com
# MÉTODOS misturar() e servir(), Cha com os MÉTODOS misturar() e servir(), e Leite com os
# MÉTODOS misturar() e servir().

from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    def preparar(self):
        print('--- Iniciando o Preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('--- Bebida Pronta ---')

    def ferver_agua(self):
        print('Fervendo água a 100 graus Celsius.')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print('Passando água pressurizada pelo pó de café moído.')

    def servir(self):
        print('Servindo em xícara pequena.')


class Cha(BebidaQuente):
    def misturar(self):
        print('Mergulhando o sachê de ervas na água.')

    def servir(self):
        print('Servindo em caneca de porcelana com limão espremido.')


class Leite(BebidaQuente):
    def misturar(self):
        print('Passando água pressurizada pelo leite em pó.')

    def servir(self):
        print('Servindo em caneca grande contendo café.')
