# Criar um programa que leia um número inteiro qualquer e mostre na tela se ele é
# par ou ímpar.

n = int(input('Digite um número: '))

print(f'O número {n} é par.' if (n % 2 == 0) else f'O número {n} é ímpar.')
print('--FIM--')
