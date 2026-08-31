# Um programa que pergunta o preço do item e informa o novo
# preço com 5% de desconto

p = float(input('Qual o preço atual do produto? R$: '))
d = float(5/100)
print(f'Se você levar agora, te dou 5% de desconto', end = (' '))
print(f'e você vai pagar apenas R$ {p - (p * d):.2f}.')
