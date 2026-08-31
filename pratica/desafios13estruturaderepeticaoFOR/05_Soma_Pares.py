# Desenvolver um programa que leia seis números inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsiderar.

soma = 0
cont = 0
for c in range(1, 6+1):
    num = int(input(f'Digite o {c}o. número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if soma == 0:
    print('Todos os números digitados são ímpares.')
else:
    print(f'Você digitou {cont} número(s) par(es) que somado(s) resulta(m) em {soma}.')
print('-- Fim --')
