# Criar um programa que gere 5 números aleatórios e coloque em uma tupla. Mostrar a
# listagem de números gerados e indicar o menor e o maior valor que está na tupla.
# Respostas no formato 1- Os valores sorteados foram: 2- O maior valor sorteado foi:
# 3- O menor valor sorteado foi:

import random
n1 = random.randint(1, 5)
n2 = random.randint(1, 5)
n3 = random.randint(1, 5)
n4 = random.randint(1, 5)
n5 = random.randint(1, 5)
tupla = (n1, n2, n3, n4, n5)

# O professor fez de outro jeito na correção, legal também porque já randomiza dentro de uma
# variável composta só, no caso a tupla:
tuplaprofessor = (random.randint(1, 5), random.randint(1, 5),
                  random.randint(1, 5), random.randint(1, 5),
                  random.randint(1, 5))
print('-' * 42)
print('Tupla no método do professor na correção:')
print(tuplaprofessor)

# A partir daqui é o código que desenrolei sozinho, fazendo o agrupamento das 5 variáveis n
# em apenas 1 chamada de tupla.

print('-' * 42)

print('Tupla criada por mim antes da correção:')
print(f'Os valores sorteados foram: ', end = (''))
for c in range(0, len(tupla)):
    print(tupla[c], end = '  ')
    c += 1

print()
print('-' * 42)

# Essa parte de max e min foi sugestão de autocomplete do próprio PyCharm, eu peguei porque
# é algo útil que não me lembro de ter visto na aula de manipulação de textos, nem na de
# operadores matemáticos, nem na de módulos.
# Muito legal: foi exatamente esse métodoh que o professor ensinou na correção.

print(f'O maior valor sorteado foi {max(tupla)}.')
print(f'O menor valor sorteado foi {min(tupla)}.')

print('-' * 42)
print('-- Fim --')
