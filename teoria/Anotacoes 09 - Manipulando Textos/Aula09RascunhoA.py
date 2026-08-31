# No Python as strings começam sempre em zero (a primeira letra "C" no exemplo abaixo).
# Dica: colchetes são sinalizadores de listas [ ].

# A contagem de elementos começa no zero. A quantidade de posições começa no 1.
# Rodrigo tem 7 posições, e o elemento zero é a letra 'R'
# Portanto o print(frase[3:6]) de Rodrigo retornaria ('rig') que é o conteúdo entre o
# elemento 3 ('r') e a posição 6 ('g')

# String    R   O   D   R   I   G   O
# Elemento  0   1   2   3   4   5   6
# Posição   1   2   3   4   5   6   7

frase = 'Curso Teórico e Prático Python'

# Fatiamento pegando um elemento
print(frase[9])
# Fatiamento pegando um trecho (do elemento 9 até a posição 14)
print(frase[9:14])
# Fatiamento pulando de n em n (exemplo, do elemento 9 à posição 21 pulando de 2 em 2)
print(frase[9:21:2])
# Fatiamento até uma certa posição (exemplo, do elemento zero até a posição 5)
print(frase[:5])
# Fatiamento de certo elemento até o final (do elemento 15 até o final)
print(frase[15:])
# Fatiamento até o final pulando de n em n (do elemento 9 ao final pulando de 3 em 3)
print(frase[9::3])

