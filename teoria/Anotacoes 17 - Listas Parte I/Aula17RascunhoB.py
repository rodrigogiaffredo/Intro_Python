# Listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura
# os quais são acessíveis por chaves individuais.

# Ao contrário das tuplas, as listas são variáveis compostas MUTÁVEIS, e são caracterizadas
# pelo uso de colchetes [].

# Sintaxe genérica: lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
# elemento:                         0           1       2       3
# posição:                          1           2       3       4


# A lista original
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)

# A substituição do elemento 3
lanche[3] = 'sorvete'
print(lanche)

# A inserção de um elemento
lanche.append('cookie')
print(lanche)

# O deslocamento dos elementos
lanche.insert(0, 'hotdog')
print(lanche)

# A remoção de elementos
# Usando comando e referenciando o elemento
del lanche[3]
# Usando métodoh para o mesmo resultado
lanche.pop(3)
# Ou para remover o último elemento da lista
lanche.pop()
# Usando métodoh e referenciando o item específico
lanche.remove('pizza')
# Verificando a existência do item antes de removê-lo
if 'pizza' in lanche:
    lanche.remove('pizza')

# Criando listas a partir de ranges
valores = list(range(4, 11))
# Pulando de 2 em 2
valores = list(range(4, 11, 2))

# Ordem crescente de itens em listas
valores = [8,2,5,4,9,3,0]
valores.sort()

# Ordem decrescente de itens em listas
valores = [8,2,5,4,9,3,0]
valores.sort(reverse=True)

# Quantidade de posições de uma lista
valores = [8,2,5,4,9,3,0]
len(valores)
