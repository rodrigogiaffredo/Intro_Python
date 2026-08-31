# Simular uma cafeteria orientada a objetos, a nossa prepara café, chá e leite. A
# SUPERCLASSE BebidaQuente {abstract} com os MÉTODOS preparar() {concreto}, ferver_agua()
# {concreto}, misturar() {abstract} e servir() {abstract}. As 3 SUBCLASSES são Café com
# MÉTODOS misturar() e servir(), Cha com os MÉTODOS misturar() e servir(), e Leite com os
# MÉTODOS misturar() e servir().

from cafeteria import *

def main():
    b1 = Cafe()
    b2 = Cha()
    b3 = Leite()

    print()
    b1.preparar()
    print()
    b2.preparar()
    print()
    b3.preparar()


if __name__ == '__main__':
    main()
