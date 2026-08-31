# Criar um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas já são maiores.

from datetime import date
hoje = date.today().year
maior = 0
menor = 0

for c in range(1, 7 + 1):
    nasc = int(input(f'Digite o ano de nascimento da {c}a. pessoa: '))
    if hoje - nasc >= 21:
        maior += 1
    else:
        menor +=1
print(f'Das 7 pessoas informadas, {maior} já atingiram a maioridade, enquanto {menor} ainda não atingiram.')
