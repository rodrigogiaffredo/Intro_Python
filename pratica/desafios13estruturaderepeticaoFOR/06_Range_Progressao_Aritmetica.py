# Desenvolver um programa que leia o primeiro termo e a razão de uma PA (Progressão
# Aritmética). No final, mostre os 10 primeiros termos dessa progressão.
# Notação geral da PA: an = a1 + (n - 1) * r onde n é posição, a1 = primeiro termo e
# r = razão

print('=' * 20)
print('DEZ TERMOS DE UMA PA')
print('=' * 20)

a1 = int(input('Digite o primeiro termo da progressão aritmética (PA): '))
r = int(input('Digite a razão da progressão aritmética (PA): '))

print('-' * 20)

print(f'Os 10 primeiros termos da PA de {a1} na razão {r} são:', end=' ')

for n in range(1, 10+1):
    print(f'{a1 + (n - 1) * r}', end= ' ')
print()

print('-' * 20)
print('-- Fim --')
