# Implementar o diagrama de classes: SUPERCLASSE Polígono {abstract}, ATRIBUTO qtd_lados,
# MÉTODOS perímetro() {abstract}, área() {abstract}. SUBCLASSE Quadrado, ATRIBUTO lado,
# MÉTODOS perímetro() e área(), e SUBCLASSE Circulo, ATRIBUTO raio, MÉTODOS perímetro() e
# área(). E estabelecer a relação de herança 'ÉUM' entre eles (Quadrado 'ÉUM' Polígono,
# Circulo 'ÉUM' Polígono).

from rich import print, inspect
from poligono import *

def main():

    q = Quadrado(20)
    #inspect(q, methods=True)
    print(f'Um quadrado de lado {q.lado}cm tem um perímetro de {q.perimetro():.1f}cm')
    print(f'Um quadrado de lado {q.lado}cm tem uma área de {q.area():.1f}cm2')

    c = Circulo(12)
    #inspect(c, methods=True)
    print(f'Um círculo de raio {c.raio}cm tem um perímetro de {c.perimetro():.2f}cm')
    print(f'Um círculo de raio {c.raio}cm tem uma área de {c.area():.2f}cm2')

if __name__ == '__main__':
    main()
