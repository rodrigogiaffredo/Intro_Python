# Um programa que converte R$ para USD com base em taxa pré-definida

br = float(input('Quanto dinheiro você tem na carteira? R$: '))
us = 3.27
print(f'Então você pode comprar US$ {br / us:.2f} já que a cotação atual é R$ {us}.')
