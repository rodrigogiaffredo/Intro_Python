# Fazer um programa que leia o comprimento do cateto oposto e do adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hp = hypot(co, ca)

print(f'Considerando as informações abaixo:\n>>> Cateto oposto: {co}\n>>> Cateto adjacente: {ca}\nO comprimento da hipotenusa é igual a {hp:.2f}.')

# E só pra constar, dá pra fazer sem o módulo math também, óbvio
# O quadrado da hipotenusa é igual a soma dos quadrados dos catetos (Pitágoras)
# hp**2 = co**2 + ca**2 então hp = (co**2 + ca**2)**1/2

print(f'(Na unha) A hipotenusa mede {(co**2 + ca**2)**0.5:.2f}.')
