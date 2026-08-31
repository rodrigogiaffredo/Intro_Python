# Fazer um programa que tenha uma função chamada maior() que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o
# maior. Exercício de desempacotamento.

from time import sleep

def maior(* num):
    print('-' * 40)
    print('Analisando os valores informados...')
    print('-' * 40)
    sleep(0.5)
    print(f'Foram digitados {len(num)} números.')
    if num == ():
        print('Não há números para mostrar.')
        print('Não há número maior.')
    else:
        print(f'São eles:', end=' ')
        for v in range(0, len(num)):
            print(f'{num[v]}', end = '  ')
            sleep(0.5)
        print()
        print(f'O maior número digitado foi {max(num)}')

# Programa principal
maior(9, 8, 1, 3, 5)
maior(0, 2, 1, 987, 4, 11, 26, 41)
maior(0)
maior()


# O professor usou contadores na montagem da função para encontrar o maior número, e para
# informar quantos números foram analisados, enquanto eu usei as funções 'len' e 'max' direto.
# Na correção, o dele ficou assim (for the record):

# def maior(* núm):
# cont = maior = 0
# print('-=' * 30)
# print('Analisando os valores passados...')
# for val in núm:
#   print(f'{val}', end = '')
#   sleep(0.3)
#   if cont == 0:
#       maior = val
#   else:
#       if val > maior
#           maior = val
#   cont += 1
# print(f'Foram informados {cont} valores no total.')
# print(f'O maior valor digitado foi {maior}.')




