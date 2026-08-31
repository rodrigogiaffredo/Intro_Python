# Outras loterias além da megasena

# lotomania -> escolher 50 números entre 0 e 99 (range será 0, 99)
# lotofacil -> escolher 15 números entre 1 e 25 (range será 0, 25)

import random

print()
print('Palpite para a Lotomania - 50 números')
lotomaniagerados = list()
cont = 0
while True:
    n = random.randint(0, 99)
    if n not in lotomaniagerados:
        lotomaniagerados.append(n)
        cont += 1
        if cont >= 50:
            break

lotomaniaemordem = sorted(lotomaniagerados)

print('-' * 39)
print('NÚMEROS GERADOS - LOTOMANIA:'.center(39))
print('-' * 39)
for i in range(0, len(lotomaniaemordem)):
    print(f'{lotomaniaemordem[i]:3}', end = ' ')
    if (i + 1) % 10 == 0:
        print()


print()
print('Palpite para a Lotofácil - 15 números')
lotofacilgerados = list()
cont = 0
while True:
    n = random.randint(1, 25)
    if n not in lotofacilgerados:
        lotofacilgerados.append(n)
        cont += 1
        if cont >= 15:
            break

lotofacilemordem = sorted(lotofacilgerados)

print('-' * 39)
print('NÚMEROS GERADOS - LOTOFÁCIL:'.center(39))
print('-' * 39)
for i in range(0, len(lotofacilemordem)):
    print(f'{lotofacilemordem[i]:3}', end = ' ')
    if (i + 1) % 5 == 0:
        print()



