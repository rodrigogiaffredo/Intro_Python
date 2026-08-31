# Criar um programa que leia uma frase qualquer e diga se ela é um palíndromo
# (frases que são lidas da mesma forma tanto da esquerda para a direita, quanto da
# direita para a esquerda. Ex.: apos a sopa, a sacada da casa, o lobo ama o bolo,
# anotaram a data da maratona, a torre da derrota.) desconsiderando os espaços e
# os acentos (os espaços devem ser digitados para que o programa os desconsidere,
# os acentos não).


frase = str(input('Digite uma frase sem pontuação ou acentos: ')).strip().upper().replace(' ', '')
n = len(frase)

# Vamos contar quantas vezes as letras dos extremos opostos são diferentes na comparação.
# Qualquer coisa diferente de 0 mostra que a frase não é um palíndromo.
dif = 0

for c in range(0, n):
# Confesso: deu erro de range um milhão de vezes, fui na tentativa e erro. Basicamente o
# que eu entendi foi que se não colocarmos o +1 após o c, ele considerará a posição n do
# len, o que deixaria o teste fora do range mencionado no for já que n - 0 daria n.
    if frase[c] != frase[n - (c + 1)]:
        dif += 1
if dif != 0:
    print(f'O inverso de {frase} é', end = (' '))
    for c in range(0, n):
        # Não tinha feito o print abaixo, vi na correção e inclui.
        print(frase [n - (c + 1)], end = '')
    print()
    print('Você não digitou um palíndromo.')
else:
    print(f'O inverso de {frase} é', end = (' '))
    for c in range(0, n):
        # Não tinha feito o print abaixo, vi na correção e inclui.
        print(frase [n - (c + 1)], end = '')
    print()
    print('Você acaba de digitar um palíndromo.')
print('-- Fim --')
