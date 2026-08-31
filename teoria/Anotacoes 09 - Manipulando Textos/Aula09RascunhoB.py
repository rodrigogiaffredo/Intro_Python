# No Python as strings começam sempre em zero (a primeira letra "C" no exemplo abaixo).
# Dica: colchetes são sinalizadores de listas [ ].

# Análise de strings

frase = 'Curso Teórico e Prático Python'

# Comprimento da frase em caracteres (útil para saber de antemão o tamanho da string).
print(len(frase))
# Contagem de determinado caractere (exemplo, ocorrências de "o" minúsculo).
print(frase.count('o'))
# Contagem de caractere num range especificado (exemplo, de zero a 13 lembrando
# que o 13 fica de fora)
print(frase.count('o',0,13))
# Encontrando trechos (exemplo, encontrando "deo" retorna o caracter inicial da ocorrência)
# Se pedir para encontrar algo que não existe na frase, a resposta será -1
print(frase.find('deo'))
# Booleano para trechos na frase (exemplo, existe "Curso" na frase)
print('Curso' in frase)


