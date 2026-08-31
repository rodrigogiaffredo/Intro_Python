# No Python as strings começam sempre em zero (a primeira letra "C" no exemplo abaixo).
# Dica: colchetes são sinalizadores de listas [ ].

# Transformação de strings (ocorre sempre através de métodos)

frase = 'Curso Teórico e Prático Python'
outra = '   Aprenda Python  '

# Substituição de trechos (exemplo, Python por Android)
# Importante: a substituição não acontece na variável em definitivo, só na instância print
print(frase.replace('Python', 'Android'))
# Trasformar para maiúsculas (mantém o que já está, altera o restante)
print(frase.upper())
# Transformar para minúsculas (lógica idêntica à anterior)
print(frase.lower())
# Transformar para primeira inicial da frase apenas em maiúscula (diferente do formato título, essa só capitaliza a primeira letra da string)
print(frase.capitalize())
# Transformar iniciais de cada palavra em maiúscula
print(frase.title())
# Remoção de espaços inúteis do começo e do final da string, preservando os espaços entre palavras (criei a frase "outra" com espaços inúteis pra testar)
print(outra)
print(outra.strip())
# Remoção de somente os últimos espaços, os da direita, do final da string apenas
print(outra.rstrip())
# Remoção de somente os primeiros espaços, os da esquerda, do inicio da string apenas
print(outra.lstrip())

