# lista:                Pessoas
# dado:                 Pedro 25    Maria 19    João 32
# elemento (em dados):   0    1       0   1      0   1
# ------------------------------------------------------
# elemento(em pessoas):     0           1           2
# item (em pessoas):        1           2           3


# Criando a primeira lista
print('Criação da primeira lista:')
dados = list()
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)
print(dados)
print()

# Aninhando a primeira lista numa segunda lista
print('Aninhamento da primeira lista na segunda:')
pessoas = list()
pessoas.append(dados[0:2])
pessoas.append(dados[2:4])
pessoas.append(dados[4:6])
print(pessoas)
print()

# Imprimindo o elemento 0 do elemento 0 da lista pessoas
print('Impressão do nome Pedro - elemento zero DO elemento zero:')
print(pessoas[0][0])
print()

# Imprimindo o elemento 1 do elemento 1 da lista pessoas
print('Impressão da idade da Maria - elemento 1 DO elemento 1:')
print(pessoas[1][1])
print()

# Imprimindo o elemento 0 do elemento 2 da lista pessoas
print('Impressão do nome João - elemento 0 DO elemento 2:')
print(pessoas[2][0])
print()

# Imprimindo todos os elementos do elemento 1 da lista pessoas
print('Imprimindo os dados da Maria - elemento 1 da lista pessoas:')
print(pessoas[1])
print()


