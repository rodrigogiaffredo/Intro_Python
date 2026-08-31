# Fazer um programa que jogue par ou ímpar com o computador (cada um mostra seu número
# de 1 a 5, e a soma dos números é verificada se é par ou ímpar). O jogo só será interrompido
# quando o usuário perder, mostrando o total de vitórias consecutivas que ele conquistou no
# final do jogo.

import random

vitoria = 0

while True:

    comput = random.randint(1, 5)

    print('=' * 23)
    print('PAR OU ÍMPAR?')
    print('=' * 23)

    numero = int(input('Diga um valor de 1 a 5: '))

    while numero not in (1, 2, 3, 4, 5):
        numero = int(input('Opção inválida, digite novamente: '))

    escolha = str(input('Escolhe Par ou Impar?: ')).upper().strip()

    while escolha not in ('PAR', 'IMPAR'):
        escolha = str(input('Opção inválida, digite novamente: ')).upper().strip()


    print('-' * 23)
    print(f'Minha mão: {comput}')
    print(f'Sua mão: {numero}')
    print(f'Total: {comput + numero}')
    print('=' * 23)

    parouimpar = ()

    if (comput + numero) % 2 == 0:
        parouimpar = 'PAR'
    else:
        parouimpar = 'IMPAR'

    if escolha == parouimpar:
        print(f'{comput + numero} é {escolha}, você ganhou!')
        vitoria += 1
        print('Vamos jogar novamente.')

    else:
        break

print('Você perdeu, fim de jogo.')
print(f'Você acumulou {vitoria} vitória(s).')



