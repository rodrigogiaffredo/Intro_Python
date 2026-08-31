# Criar um programa que simule o funcionamento de um caixa eletrônico. No início, perguntar
# ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues. Obs.: considerar que o caixa possui cédulas
# de R$ 50,00, R$ 20,00 R$ 10,00 e R$ 1,00.

cont50 = cont20 = cont10 = cont1 = 0

print('-' * 30)
print('CAIXA ELETRÔNICO')

print('-' * 30)
saque = int(input('Digite o valor do saque: R$ '))
saqueoriginal = saque

while True:

    if saque // 50 != 0:
        cont50 = saque // 50
        saque -= (saque // 50) * 50

    else:
        if saque // 20 != 0:
            cont20 = saque // 20
            saque -= (saque // 20) * 20

        else:
            if saque // 10 != 0:
                cont10 = saque // 10
                saque -= (saque // 10) * 10

            else:
                if saque // 1 != 0:
                    cont1 = saque // 1
                    saque -= (saque // 1) * 1

    if saque == 0:
        break


print('-' * 30)
print(f'Total sacado: R$ {saqueoriginal},00')
if cont50 != 0:
    print(f'Qtd de notas de R$ 50,00: {cont50}')
if cont20 != 0:
    print(f'Qtd de notas de R$ 20,00: {cont20}')
if cont10 != 0:
    print(f'Qtd de notas de R$ 10,00: {cont10}')
if cont1 != 0:
    print(f'Qtd de notas de R$ 1,00: {cont1}')
print()
print('-- Volte Sempre --')
print('-- Fim do Programa --')
