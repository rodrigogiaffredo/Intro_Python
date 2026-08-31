# Dicionários são variáveis compostas que permitem armazenar vários valores numa mesma
# estrutura, acessíveis por chaves literais (ao invés de coordenadas numéricas).

# São semelhantes a tuplas e listas, porém a possibilidade de dar nome aos elementos, ao
# invés de ter que trabalhar com a indexação numérica padrão, auxilia na montagem dos algoritmos
# e na chamada dos dados nos campos da variável durante o desenvolvimento do programa.

# Tuplas são identificadas por (parênteses), listas por [colchetes], e os dicionários são
# identificados pelo uso de {chaves}.

# Formas de declarar um dicionário chamado 'dados' no exemplo:

# dados = {}
# dados = dict()
# dados = {'nome':'Pedro', 'idade':25}

# Estrutura padrão de um dicionário
# dados     =   {'nome':'Pedro', 'idade':25}
# elemento                nome         idade     (nome ao invés de 0, idade ao invés de 1)
# item                     1             1

# Isso faz com que:

# print(dados['nome']) resulte em 'Pedro'
# print(dados['idade']) resulte em 25

# Para CRIAR UM NOVO ELEMENTO no dicionário 'dados', basta declará-lo normalmente ao longo
# do programa. Por exemplo, vamos inserir o elemento 'sexo' no dicionário 'dados':

# dados['sexo'] = 'M'

# Isso atualiza o dicionário 'dados' para:

# dados     =   {'nome':'Pedro', 'idade':25, 'sexo':'M'}
# elemento               nome            idade       sexo
# item                     1              1            1

# Para REMOVER ELEMENTOS no dicionário 'dados', usamos o comando 'del' assim como nas listas.
# Esse comando remove tanto a estrutura quanto os valores contidos nela. Vamos por exemplo
# remover o elemento 'idade':

# del dados['idade']

# O dicionário 'dados' será então atualizado para:

# dados     =   {'nome':'Pedro', 'sexo':'M'}
# elemento               nome            sexo
# item                     1               1

# Outra forma de declarar dicionários, que esteticamente facilita a organização dos elementos
# e itens. Vamos por exemplo declarar o dicionário 'filmes':

# filmes = {'titulo':'Star Wars',
#           'ano':1977,
#           'diretor':'George Lucas'
#           }

# Resultando na estrutura de dados:

# filme     =    {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}
# elemento                    titulo           ano                diretor
# item                           1              1                    1


# Em dicionários, os elemento são chamados de keys (chaves), portanto a partir de agora vamos
# referenciá-los assim nas próximas estruturas de dados demonstradas.

# A qualquer momento, podemos acessar itens, chaves, e valores.

# Imprimindo somente os VALORES:

# print(filme.values()) retornará os VALORES: 'Star Wars', 1977, 'George Lucas'

# Imprimindo somente as CHAVES:

# print(filme.keys()) retornará as KEYS (CHAVES): titulo, ano, diretor

# Imprimindo os ITENS (resultantes da combinação de keys e values):

# print(filme.items()) retornará: 'titulo''Star Wars', 'ano'1977, 'diretor''George Lucas'

# Semelhante ao que fazíamos com enumerate em tuplas e listas, podemos usar a combinação
# KEYS e VALUES dentro de laços de repetição ao criarmos nossos programas.

# for k, v in filme.items()
#       print(f'O {k} é {v}.')      Resultando em: 'O titulo é Star Wars.'      (laço 1)
#                                                  'O ano é 1977.'              (laço 2)
#                                                  'O diretor é George Lucas.'  (laço 3)

# Os temas tuplas, listas e dicionários estão intimamente relacionados, e podemos utilizar os
# comandos e métodos vistos nas aulas 17 e 18, agora na aula 19 também.

# Suponha que eu tenha uma locadora de vídeos. Eu posso criar uma grande lista chamada
# 'locadora', e armazenar 'dicionários' de filmes dentro dela como elementos. Por exemplo:

# locadora.append(filme[:]) resultará em:

# locadora  =    [{'Star Wars', 1977, 'George Lucas'}, {'Platoon', 1986, 'Oliver Strone'}]
# key dicionário     titulo     ano      diretor        titulo     ano       diretor
# item dicionário       1        1          1              2        2           2
# elemento lista                 0                                      1
# item lista                     1                                      2


# Se eu quiser por exemplo, saber o ANO do PRIMEIRO filme da lista:

# print(locadora[0]['ano'])     Resultará em '1977'
# print(locadora[1]['titulo])   Resultará em 'Platoon'
