# Refazer o exercício de leitura do primeiro termo e da razão de uma PA (aula 13 desafio 06)
# mostrando os 10 primeiros termos da progressão aritmética usando a estrutura WHILE.
# Enunciado da aula 13 desafio 06: Desenvolver um programa que leia o primeiro termo e a
# razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa
# progressão. an = a1 + (n-1) * r onde a1 = primeiro termo r = razão

print()
print('-' * 43)
print('-- CÁLCULO DE PROGRESSÃO ARITMÉTICA (PA) --')
print('-' * 43)

a1 = int(input('Digite o primeiro termo da PA: '))
r  = int(input('Digite a razão da PA: '))
n = 1

# an = a1 + (n-1) * r

print(f'Os 10 primeiros termos da PA {a1} razão {r} são: ', end = ' ')

while n <= 10: # Número de termos dado no enunciado (10)
    print(f'{a1}', end = '')
    # Aí o lance de omitir a última flechinha, aprendi no desafio anterior e já fiz aqui.
    print(' -> ' if n < 10 else ' -- Fim -- ', end = '')
    a1 += r
    n += 1
print()
