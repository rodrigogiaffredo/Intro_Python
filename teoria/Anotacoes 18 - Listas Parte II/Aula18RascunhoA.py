# Pequeno recap:

# Listas são mutáveis, e o comando abaixo cria uma lista caracterizada por []:
# dados = list()
# dados.append('Dado') adiciona 'Dado' ao final da lista dados

# É possível fazer aninhamento de listas, através da lógica do append.

# Primeira lista:

# dados = list()
# dados.append('Pedro')
# dados.append(25)


# lista:        Dados
# dado:         Pedro       25      Maria       19      João        32
# elemento:       0         1         2         3         4         5
# item:           1         2         3         4         5         6

# Segunda lista:

# pessoas = list()


# A inserção da primeira lista dentro da segunda, fará com que a primeira lista inteira ocupe
# o elemento zero da segunda lista. Ela é feita também através de um append, porém ao invés
# de um dado específico, inserimos uma cópia da lista inteira:

# pessoas.append(dados[:])

# O resultado será:

# lista:                Pessoas
# dado:                 Pedro 25    Maria 19    João 32
# elemento (em dados):   0    1       0   1      0   1
# ------------------------------------------------------
# elemento(em pessoas):     0           1           2
# item (em pessoas):        1           2           3


# Se eu quisesse declarar manualmente toda essa estrutura acima, seguindo a lógica de aninhar
# listas, eu poderia usar:

# pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

# Leitura da declaração acima: dentro da lista 'pessoas' tenho outras 3 listas, sendo a primeira
# a lista do Pedro (elemento 0 da lista pessoas), a segunda a da Maria (elemento 1 da lista
# pessoas), e a terceira a do João (elemento 2 da lista pessoas).


