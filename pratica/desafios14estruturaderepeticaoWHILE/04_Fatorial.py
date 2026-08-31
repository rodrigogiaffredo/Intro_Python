# Faça um programa que leia um número qualquer e mostre o seu fatorial. Mostrar conforme o exemplo:
# 5!=5x4x3x2x1=120

n = int(input('Digite o número para cálculo do fatorial: '))
c = 1
fatorial = 1
mascaran = n

print(f'{n}! = ', end = '')

while c <= n:
    fatorial *= c
    print(mascaran, end='')
    # É assim que resolve o último x que não deve aparecer.
    print(' x ' if mascaran > 1 else ' = ', end = '')
    c += 1
    mascaran -= 1

print(f'{fatorial}.')

print()
print('-- Fim --')
