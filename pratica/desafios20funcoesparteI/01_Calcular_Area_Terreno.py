# Fazer um programa que tenha uma função chamada área() que receba as dimensões de um
# terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(a, b):
    print(f'A área de um terreno {a} x {b} é de {a * b:.2f} metros quadrados.')

# Programa principal
print('-' * 35)
print('Controle de Terrenos')
print('-' * 35)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

