# Fazer um programa que leia 3 números e mostre qual é o maior, e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 == n2 and n1 == n3:
    print('Você digitou 3 números iguais, pensa que eu sou trouxa?')
else:
    if n1 >= n2 and n1 >= n3:
        maior = n1
    else:
        menor = n1

    if n2 >= n1 and n2 >= n3:
        maior = n2
    else:
        menor = n2

    if n3 >= n1 and n3 >= n2:
        maior = n3
    else:
        menor = n3

    print(f'O maior número digitado foi {maior}.\nO menor número digitado foi {menor}.')
print('--FIM--')
