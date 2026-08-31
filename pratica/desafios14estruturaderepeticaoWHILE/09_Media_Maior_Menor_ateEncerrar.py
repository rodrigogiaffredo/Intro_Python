# Criar um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostrar a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = 0
cont = 0
maior = 0
menor = 0

n = float(input('Digite um número: '))
soma += n
cont += 1
opcao = str(input('Quer digitar outro número? S / N: ')).upper().strip()
maior = n
menor = n

while opcao == 'S':
    n = float(input('Digite outro número: '))
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    opcao = str(input('Quer digitar outro número? S / N: ')).upper().strip()

print(f'A média dos valores digitados deu {soma / cont}.')
print(f'O maior valor digitado foi {maior:.0f} e o menor foi {menor:.0f}.')
