# No Python as strings começam sempre em zero (a primeira letra "C" no exemplo abaixo).
# Dica: colchetes são sinalizadores de listas [ ].

# Divisão de strings

frase = 'Curso Teórico e Pratico Phyton'
lista = frase.split()


# Dividir a string exatamente onde ocorrem os espaços em branco (se antes apenas o
# "C" inicial era zero, agora a inicial de cada palavra passa a ser zero). O output
# é uma lista de palavras, e "Curso" passa a ser a palavra zero dela.
# Existem outros atributos que podem ser usados nos parênteses, ficou de lição de casa
print(frase.split())



# Junção de strings

# Conectar os elementos da lista usando um separador (no meu caso usei hífen)
print('-'.join(lista))
