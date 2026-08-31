# Criar um programa que leia 2 valores e mostre um menu na tela: [1] somar [2] multiplicar
# [3] maior [4] novos números [5] sair do programa. O programa deverá realizar a operação
# solicitada em cada caso.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0

print('''--- MENU DE OPÇÕES ---
[1] Somar um com o outro
[2] Multiplicar um pelo outro
[3] Saber qual dos dois é o maior
[4] Escolher outros números
[5] Sair do programa
''')

escolha = int(input(f'O que você quer fazer com os números {n1} e {n2}?: '))

while escolha != 5:

    if escolha == 1:
        print(f'A soma {n1} + {n2} = {n1 + n2}.')
        escolha = int(input('Faça outra escolha: '))

    if escolha == 2:
        print(f'A multiplicação {n1} x {n2} = {n1 * n2}')
        escolha = int(input('Faça outra escolha: '))

    if escolha == 3:
        if n1 > n2:
            print(f'O maior número digitado foi {n1}.')
            escolha = int(input('Faça outra escolha: '))
        else:
            print(f'O maior número digitado foi {n2}.')
            escolha = int(input('Faça outra escolha: '))

    if escolha == 4:
        print('----------')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('''--- MENU DE OPÇÕES ---
[1] Somar um com o outro
[2] Multiplicar um pelo outro
[3] Saber qual dos dois é o maior
[4] Escolher outros números
[5] Sair do programa
        ''')
        escolha = int(input(f'O que você quer fazer com os números {n1} e {n2}?: '))

    if escolha < 1:
        escolha = int(input(f'Opção {escolha} inválida, escolha novamente: '))

    if escolha > 5:
        escolha = int(input(f'Opção {escolha} inválida, escolha novamente: '))

print('-- Até a próxima, obrigado por participar! --')

print('-- Fim --')





