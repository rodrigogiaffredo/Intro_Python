# Criar um programa que leia um número real qualquer pelo teclado e mostre na tela
# apenas sua porção inteira.

from math import trunc

n = float(input('Digite um número real qualquer: '))
i = trunc(n)
print(f'(Usando trunc) A parte inteira do número {n} é {i}.')

# Só pra constar, dá pra resolver também sem o módulo math

print(f'(Usando int) A parte inteira de {n} é {int(n)}.')
