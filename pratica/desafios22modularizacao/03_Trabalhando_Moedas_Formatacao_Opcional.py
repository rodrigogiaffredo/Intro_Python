# Modificar as funções que foram criadas no primeiro exercício para que elas aceitem um
# parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela
# função moeda() desenvolvida no exercício anterior.

import moeda

preco = float(input('Digite o preço: R$ '))
print()
print('Impressões com formatação = True')
print()
print(f'A medade de {moeda.moeda(preco)} é igual a {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é igual a {moeda.dobro(preco, True)}')
print(f'Reduzindo {moeda.moeda(preco)} em 39% temos {moeda.diminuir(preco, 39, True)}')
print(f'Aumentado {moeda.moeda(preco)} em 157% temos {moeda.aumentar(preco, 157, True)}')
print()
print('Impressões com formatação = False')
print()
print(f'A medade de {moeda.moeda(preco)} é igual a {moeda.metade(preco)}')
print(f'O dobro de {moeda.moeda(preco)} é igual a {moeda.dobro(preco)}')
print(f'Reduzindo {moeda.moeda(preco)} em 39% temos {moeda.diminuir(preco, 39)}')
print(f'Aumentando {moeda.moeda(preco)} em 157% temos {moeda.aumentar(preco, 157)}')



