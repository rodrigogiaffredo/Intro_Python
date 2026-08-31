# Criar um programa que leia vários números e os coloque em uma lista. Mostrar: 1- quantos
# números foram digitados 2- a lista de valores em ordem crescente 3- se o valor 5 foi
# digitado e está ou não na lista.

lista = []

# Input de dados
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    continuar = str(input('Quer digitar outro número? S/N: ')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Opção inválida, digite novamente: ')).upper().strip()
    if continuar == 'N':
        break


# Análise dos valores digitados

print('-' * 40)
print('ANÁLISE DOS VALORES DIGITADOS'.center(40))
print('-' * 40)

print(f'Foram digitados {len(lista)} números.')
# Eu tinha dado mole e não vi que o enunciado era decrescente, fiz na demo da correção
lista.sort(reverse=True)
print(f'Os valores digitados foram (em ordem decrescente): {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')

print('-' * 40)
print('-- Fim do Programa --')
