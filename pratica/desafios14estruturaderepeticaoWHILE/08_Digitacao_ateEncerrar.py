# Criar um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag ou condição
# de parada).

soma = 0
cont = 0

n = int(input('Digite um número (ou digite 999 para encerrar): '))

while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite outro número (ou 999 para encerrar): '))

print(f'Você digitou {cont} números.')
print(f'A soma dos {cont} números digitados é igual a {soma}.')
print()
print('-- Fim --')


