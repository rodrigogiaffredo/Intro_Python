# Simular um sistema de batalha entre personagens de um RPG. SUPERCLASSE Personagem
# {abstract} ATRIBUTOS nome, vida, golpes, e MÉTODOS atacar(alvo, forca), receber
# dano(dano), curar() {abstract}. SUBCLASSES Guerreiro com o MÉTODOS curar() e Mago curar().

from personagens import *
from rich import inspect


def main():
    p1 = Guerreiro('Megaman', 1000)
    #inspect(p1, methods=True)
    p2 = Mago('Merlin', 5000)

    p1.atacar(p2, 200)
    p2.atacar(p1, 230)

    p1.curar()
    p2.curar()


if __name__ == '__main__':
    main()
