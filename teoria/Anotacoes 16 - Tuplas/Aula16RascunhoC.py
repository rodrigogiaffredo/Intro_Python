# Criando a tupla (sempre usando parênteses, isso caracteriza uma variável composta tupla).
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

# tupla     hamburguer  suco    pizza   pudim
# elemento  0           1       2       3
# posição   1           2       3       4

# Sempre lembrando: Tuplas são IMUTÁVEIS via programa.
# Ou seja, o comando abaixo daria erro:
# lanche[1] = 'Refrigerante'


# Imprimindo o conteúdo da tupla sem aspas nem parênteses
print('Tupla simples:')
for item in lanche:
    print((item), end = ' ')
print()

# Imprimindo a quantidade de posições da tupla
print()
print('Comprimento da tupla:')
print(len(lanche))

# Outro modo de imprimir os elementos da tupla sem virgulas e parênteses. Ela diz que vamos
# imprimir o range que vai do elemento 0 até a posição 'comprimento da tupla', no nosso caso
# vamos do elemento zero até a posição 4 (já que o 'comprimento' de lanche é igual a 4 itens).
print()
print('Tupla usando range e comprimento:')
for item in range(0, len(lanche)):
    print(lanche[item], end = ' ')
print()
print()

# Mostrando elemento e posição numa mesma string de texto
print('Elemento e item usando range:')
for item in range(0, len(lanche)):
    print(f'{(lanche[item]).capitalize()} é o elemento {item} da minha tupla.')
print()

# Outro jeito de chegar no mesmo resultado, mostrando elemento e posição numa string de texto
# O enumerate é muito usado quando, além do dado em si, queremos também saber a posição do
# dado dentro de uma tupla. Daí a necessidade de adicionar mais um argumento logo após o for
# que é justamente a referência ao conteúdo do item, deixa de ser apenas um contador.
print('Elemento e item usando enumerate:')
for item, elemento in enumerate(lanche):
    print(f'{elemento.capitalize()} é o elemento {item} da minha tupla.')
print()

# Imprimindo em ordem crescente (sorted)
# Note que esse comando não muda a ordem dos elementos dentro da tupla, ele apenas os imprime
# em ordem crescente. Nos bastidores, o Python cria uma lista, reorganiza, e imprime.
print('Elementos em ordem crescente (sorted):')
print(sorted(lanche))
print()

# Trabalhando com tuplas numéricas
a = (2, 5, 4)
b = (5, 8, 1, 2)
print('Mostrando as tuplas numéricas:')
print(a)
print(b)
print()

# Juntando os conteúdos de 2 tuplas numéricas numa terceira
c = a + b
print('Juntando duas tuplas numéricas a + b:')
print(c)
print()

# Note que a + b é diferente de b + a
c = b + a
print('Juntando b + a ao invés de a + b:')
print(c)
print()

# Mostrando o comprimento de 'c'
print('Comprimento da tupla resultante:')
print(len(c))
print()

# Contando o número de ocorrências de determinado item dentro de uma tupla
print('Contagem de ocorrências do número 5:')
print(c.count(5))
print()

# Informando um conteúdo e perguntando qual elemento ele é (primeira ocorrência):
print('Identificando um elemento:')
print(c)
print(c.index(8))
print()

# Usando dados de tipos diferentes numa tupla
print('Diferentes tipos de dados na mesma tupla:')
dados = ('Rodrigo', 'M', 49, 72.8, 1.73)
print(dados)
print()

# Não podemos mudar tuplas nem apagar elementos dentro dela, mas podemos apagá-las totalmente
# com o comando del. O comando del(pessoa) faz com que o comando print(dados) não tenha mais
# o que imprimir.
print('Apagando os dados da tupla:')
dados = ('Rodrigo', 'M', 49, 72.8, 1.73)
del(dados)
print(dados)
print()
