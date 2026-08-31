# Criar um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro(), e metade(). Fazer também um programa que importe esse módulo e use
# algumas dessas funções.

# Não é pra caprichar nos valores monetários, porque isso é missão do próximo exercício.

import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A medade de R$ {preco} é {moeda.metade(preco)}')
print(f'O dobro de R$ {preco} é {moeda.dobro(preco)}')
print(f'Aumentando R$ {preco} em 10% temos {moeda.aumentar(preco, 10)}')
print(f'Reduzindo R$ {preco} em 13% temos {moeda.diminuir(preco, 13)}')


