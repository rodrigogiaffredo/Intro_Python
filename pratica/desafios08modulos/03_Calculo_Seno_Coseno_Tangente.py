# Fazer um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

# Quando eu calculei diretamente em cima do número digitado, o resultado do programa
# não passou pelo check de verdade, daí descobri que tinha que primeiro converter o número
# digitado para radianos, para então calcular sen,cos,tan

from math import cos, sin, tan, radians
a = float(input('Digite o valor do ângulo: '))
r = radians(a)
s = sin(r)
c = cos(r)
t = tan(r)

print(f'Tenho algumas informações sobre o ângulo de {a}°:\n>>> O seno de {a}° é igual a {s:.2f}\n>>> O coseno de {a}° é igual a {c:.2f}\n>>> A tangente de {a}° é igual a {t:.2f}')
