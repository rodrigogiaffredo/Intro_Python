# Criar classes capazes de calcular fretes de veículos diferentes. O diagrama é a
# SUPERCLASSE Transporte {abstract}, com ATRIBUTOS distancia e frete, e MÉTODOS
# calc_frete() {abstract}. As 3 SUBCLASSES serão Moto com ATRIBUTO fator = 0.50 e MÉTODOS
# calc_frete() Caminhao ATRIBUTO fator = 1.20 METODO calc_frete() e Drone ATRIBUTO
# fator = 9.50 METODO calc_frete(). Se o frete for de Moto ele é livre (não tem distância
# mínima nem máxima). Caminhao o mínimo é 50km. Drone no máximo 10km de entrega.

from transportes import *
from rich import print
from rich.table import Table
from rich import inspect


def main():
    dist = 80

    entrega = Drone(dist)
    print()
    # O comando 'type(entrega).__name__' serve para retornar o nome da classe no print
    print(f'Frete de {type(entrega).__name__} em {dist}km = {entrega.calcular_frete()}')

    print()

    # Criando uma tabela de fretes
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title='Tabela de Fretes')
    tabela.add_column('Distância')
    tabela.add_column('Tipo')
    tabela.add_column('Frete')

    for item in viagem:
        tabela.add_row(f'{dist}km', f'{type(item).__name__}', f'{item.calcular_frete()}')


    print(tabela)

if __name__ == '__main__':
    main()
