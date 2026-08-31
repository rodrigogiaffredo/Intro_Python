# Tuplas() (juntamente com as listas[] e dicionários{}) são uma das possibilidades chamadas de
# variáveis COMPOSTAS. As tuplas, além de compostas, são IMUTÁVEIS. Permitem armazenar vários
# valores em uma mesma estrutura, as quais são acessíveis por chaves individuais.

# Muito parecida com o conceito de vetor que aprendi no curso de algoritmos, porém no Python
# ela aceita str, int, float, etc. tudo na mesma tupla, não precisa usar um tipo de dado
# apenas.

# Por analogia, uma tupla pode ser considerada uma string, e por isso todas as regras vistas
# na aula 09 - Manipulando Textos se aplicam também aqui.

# Tuplas são caracterizadas por parênteses ().

# Por exemplo: tenho uma variável composta chamada 'lanche' com 4 espaços:

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
#              0          1        2        3

# Imprimindo a tupla inteira
print(lanche)

# Imprimindo o segundo item da tupla (delimitador é [], vamos fixar isso de uma vez.),
# lembrando que a contagem começa no zero.
print(lanche[2])

# Imprimindo até o segundo item a partir do elemento 0
print(lanche[0:2])

# Imprimindo até o último item a partir do elemento 1
print(lanche[1:])

# Imprimindo o último item da tupla
print(lanche[-1])

# Imprimindo a tupla com a sequência invertida
print(lanche[::-1])

# Imprimindo a quantidade de elementos dentro da tupla
print(len(lanche))

# É possível utilizar estruturas de repetição dentro das tuplas, recurso bastante poderoso.
# Posso imprimir todos os itens de uma tupla da seguinte maneira:
for c in lanche:
    print(c)

# Dada a importância do conceito, vale repetir: tuplas são IMUTÁVEIS através do programa.
# Só conseguimos mudar informações dentro de uma tupla parando o programa e indo até os
# elementos para alterá-los manualmente.

# Não poderia por exemplo trocar pudim por sorvete dentro da tupla usando um replace, teria
# que digitar sorvete no lugar de pudim com o programa parado.



