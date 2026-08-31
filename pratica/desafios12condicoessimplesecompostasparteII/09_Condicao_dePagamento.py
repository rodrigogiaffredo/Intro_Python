# Elaborar um programa que calcule o valor a ser pago por um produto, considerando seu
# preço normal e condição de pagamento: à vista dinheiro/cheque 10% de desconto; à vista
# no cartão 5% de desconto; em até 2x no cartão preço normal; 3x ou mais no cartão 20% de
# juros.

# O professor usou três aspas para criar o menu, lembrei, gostei e repliquei.

# Lembrei de colocar um pedido de quantas parcelas usar na opção 3, mas esqueci de blindar
# contra a escolha de uma opção inválida, o professor chamou atenção na aula daí incluí.
# Temos que blindar o sistema contra usuários despreparados.

preco = float(input('Digite o preço do produto: R$ '))
avdc = preco * .90
dvnc = preco
tvomnc = preco * 1.20
print('''Formas de pagamento disponíveis:
1- Pagamento à vista no dinheiro ou no cheque com 10% de desconto.
2- Parcelado em 2x iguais no cartão de crédito no preço normal.
3- Parcelado em 3x ou mais no cartão de crédito com 20% de acréscimo.
''')

escolha = int(input('Digite a forma de pagamento escolhida: '))


if escolha == 1:
    print(f'O total ficou R$ {avdc:.2f} e você ganhou 10% de desconto.')
elif escolha == 2:
    print(f'O total ficou R$ {dvnc:.2f} e você pagará 2 parcelas iguais de R$ {dvnc / 2:.2f}')
elif escolha == 3:
    print(f'O total ficou R$ {tvomnc:.2f} com acréscimo de 20% ao preço normal.')
    quantas = int(input('Quer parcelar em quantas vezes? (à partir de 3x): '))
    if quantas < 3:
        print('Número de parcelas não permitido - forma de pagamento válida para 3 ou mais prestações.')
    else:
        print(f'Você pagará {quantas} parcelas de R$ {tvomnc / quantas:.2f}.')
else:
    print('Opção de pagamento inválida, tente novamente.')
print()
print('-- Obrigado pela preferência, volte sempre!')
