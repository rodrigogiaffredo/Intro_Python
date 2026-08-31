# Escrever um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
# vai pagar. Calcular o valor da prestação mensal, sabendo que ela não pode exceder 30%
# do salário ou então o empréstimo será negado.

valor = float(input('Digite o valor do imóvel a ser financiado: '))
salario = float(input('Digite o salário do responsável pelo financiamento: '))
quitacao = int(input('Em quantos anos pretende quitar o financiamento: '))

if float(valor / (quitacao * 12)) > (salario * 0.30):
    print('Empréstimo negado.\nSua renda atual está fora das regras e condições para aprovação.\n>>> Regra: prestação não pode ultrapassar 30% do valor da renda mensal.')
    print(f'* Prestação nas condições solicitaddas: R$ {(valor / (quitacao * 12)):.2f}')
    print(f'* 30% da renda informada: R$ {salario * 0.30:.2f}')
else:
    print(f'Empréstimo aprovado!\nVocê pagará {(quitacao * 12):.0f} prestações mensais de R$ {valor / (quitacao * 12):.2f}.')
print('-- Obrigado pela preferência --')
