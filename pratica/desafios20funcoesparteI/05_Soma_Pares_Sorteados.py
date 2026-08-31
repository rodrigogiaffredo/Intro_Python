# Fazer um programa que tenha uma lista chamada [números] e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função
# anterior.

from random import randint
from time import sleep

# Cabeçalho
print('-' * 25)
print('Sorteando 5 números...')
print('-' * 25)
sleep(1.5)
numeros = list()

# Eu tinha feito o FOR no programa principal, mas a forma como o professor criou a função
# 'sorteia', trazendo o FOR para dentro dela, é mais interessante, por isso adotei.
# Eu só não trouxe para dentro da função porque o número de passos é fechado (5 números
# sorteados), mas pelo visto isso não tem nada a ver.

# SOLUÇÃO DO PROFESSOR

def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))

# Programa principal
sorteia(numeros)
print(f'Os números sorteados foram {numeros}.')

# MINHA SOLUÇÃO

#def sorteia(num):
#    num = randint(0, 100)
#    numeros.append(num)

# Programa principal
#for c in range(0, 5):
#    sorteia(c)
#print(f'Os números sorteados foram {numeros}.')

# Minha solução e a do professor bateram nesse quesito.
def somapar(lista):
    s = 0
    for c in lista:
        if c % 2 == 0:
            s += c
    sleep(1.5)
    print(f'A soma dos números pares sorteados é igual a {s}.')
    print()

# Programa principal
somapar(numeros)


