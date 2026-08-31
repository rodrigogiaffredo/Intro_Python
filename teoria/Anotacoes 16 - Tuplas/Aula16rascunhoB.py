
# Criando a tupla (sempre usando parênteses, isso caracteriza uma variável composta tupla).
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

# tupla     hamburguer  suco    pizza   pudim
# elemento  0           1       2       3
# posição   1           2       3       4

# Sempre lembrando: Tuplas são IMUTÁVEIS via programa.
# Ou seja, o comando abaixo daria erro:
# lanche[1] = 'Refrigerante'

# Imprimindo a tupla
print(lanche)

# Imprimindo o segundo elemento (já que a contagem começa sempre no 0)
print(lanche[1])

# Imprimindo o elemento da penúltima posição (o elemento da última posição sempre será -1).
print(lanche[-2])

# Imprimindo até a terceira posição a partir do elemento 1
print(lanche[1:3])

# Imprimindo do elemento 2 até o final
print(lanche[2:])

# Imprimindo tudo até a posição 2
print(lanche[:2])

# Imprimindo do elemento da antepenúltima posição até o final
print(lanche[-3:])




