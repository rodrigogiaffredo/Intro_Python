# Listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura
# os quais são acessíveis por chaves individuais.

# Ao contrário das tuplas, as listas são variáveis compostas MUTÁVEIS, e são caracterizadas
# pelo uso de colchetes [].

# Sintaxe genérica: lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
# elemento:                         0           1       2       3
# posição:                          1           2       3       4

# Agora, caso eu queira por exemplo substituir o elemento [3] por sorvete, consigo usar
# lanche[3] = 'sorvete'
# Isso fará com que a lista seja alterada para lanche = ['hamburguer', 'suco', 'pizza',
#                                                        'sorvete']

# Essa é a principal diferença entre listas e tuplas: listas são MUTÁVEIS, tuplas não.

# Fora isso, a estrutura de ambas é muito semelhante.

# Porém, existem métodos e comandos que não se aplicam a tuplas, e que se aplicam a listas.

# Por exemplo: como são mutáveis, listas podem ser aumentadas sempre que necessário. Para isso,
# uso o métodoh append. Suponhamos que queira colocar mais um item na lista 'lanche':

# lanche.append('cookie') incluirá 'cookie' na posição 5 da lista, e 'cookie' passará a ser
# o elemento 4 dela.

# É possível também inserir um novo item no lugar já ocupado por algum outro elemento, por
# exemplo, quero empurrar os elementos para a direita, a fim de que 'hotdog' passe a ser o
# elemento 0. Para isso uso lanche.insert(0, 'hotdog')

# É possível também apagar itens da lista, seja por comando, seja por métodoh. O comando
# 'del'pode ser usado assim: del lanche[3] para apagar o elemento 3. Igualmente, podemos usar
# o métodoh 'pop' assim: lanche.pop(3) para obter o mesmo resultado.

# Normalmente, usa-se o métodoh 'pop' para eliminar o último item de uma lista, mas é possível
# também passar parâmetro, como fiz acima.

# Outra forma interessante de remoção de elementos é o uso do métodoh 'remove' e nesse caso
# não faço menção do elemento, mas do item específico que desejo remover. Ficaria algo assim
# lanche.remove('pizza').

# Vale notar que independentemente do comando ou métodoh utilizado para remoção, a lista
# se auto organizará para que não haja nenhuma lacuna, ou seja, será automaticamente
# reindexada (sempre bom dar um print nela após alterações para ver como ficou). Mas o ideal
# é resolver essa questão no código, usando a condicional 'if' 'in', ou seja, pergunto se o
# item está na lista, e se estiver, removo. Exemplo:

# if 'pizza' in lanche
#   lanche.remove('pizza')

# É possível criar listas a partir de ranges. Por exemplo, quero criar uma lista 'valores'
# a partir de um range que vai do elemento 4 até a posição 11. Para isso, uso 'list(range)'.

# valores = list(range(4, 11))

# Posso também colocar elementos em ordem crescente dentro de uma lista usando o métodoh
# 'sort'. Por exemplo, se tenho uma lista chamada 'valores' e quero ordená-la, devo usar

# valores = [8,2,5,4,9,3,0]
# valores.sort()
# Resultará na lista valores = [0,2,3,4,5,8,9]

# Já no caso de ser necessário ordenar os valores em ordem decrescente (ou inversa), uso
# o métodoh 'sort' com o parâmetro 'reverse':

# valores.sort(reverse=True)
# Resultando em valores = [9,8,5,4,3,2,0]

# Podemos também conhecer o tamanho de uma lista usando o comando 'len'. Por exemplo, o
# tamanho (quantidade de posições) da lista 'valores' é descoberto usando len(valores).

# valores = [8,2,5,4,9,3,0]
# len(valores)
# resultará em 7
