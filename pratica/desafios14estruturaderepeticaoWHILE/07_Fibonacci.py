# Escrever um programa que leia um número n inteiro qualquer e mostre na tela os
# n primeiros elementos de uma sequência de Fibonacci. Ex: a pessoa digitou 7, apareceu
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

q = int(input('Quantas posições da sequência de Fibonacci você quer ver?: '))
p1 = 0
p2 = 1
fibo = 0
n = 3

print(p1, end = ', ')
print(p2, end = ', ')

while n <= q:
    fibo = p1 + p2
    print(fibo, end='')
    # Aí o lance da vírgula não pegar o último número da sequência12
    print(', ' if n < q else '', end='')
    p1 = p2
    p2 = fibo
    n += 1

print(' -- Fim -- ')
