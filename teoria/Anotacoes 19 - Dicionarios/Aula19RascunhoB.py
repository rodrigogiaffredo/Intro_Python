# Dicionários são variáveis compostas que permitem armazenar vários valores numa mesma
# estrutura, acessíveis por chaves literais (ao invés de coordenadas numéricas).

# Formas de declarar um dicionário chamado 'dados' no exemplo:

# dados = {}
# dados = dict()
# dados = {'nome':'Pedro', 'idade':25}

# Estrutura padrão de um dicionário
# dados     =   {'nome':'Pedro', 'idade':25}
# elemento                nome         idade     (nome ao invés de 0, idade ao invés de 1)
# item                     1             1


# DECLARAÇÃO de dicionário simples
print('Declaração de dicionário simples:')
pessoas = {'nome':'Rodrigo', 'sexo':'M', 'idade':49}
print(pessoas)
print()

# Imprimindo valor de um elemento (chave a partir de agora) ESPECÍFICO do dicionário
print('Impressão do valor do elemento (chave a partir de agora) NOME:')
print(pessoas['nome'])
print()

# Impressão FORMATADA (f-string)
print('Impressão formatada via f-string (chaves NOME e IDADE):')
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
print()

# Impressão de todas as CHAVES de um dicionário
print('Impressão das chaves de um dicionário:')
print(pessoas.keys())
print()

# Impressão de todos os VALORES de um dicionário
print('Impressão dos valores de um dicionário:')
print(pessoas.values())
print()

# Impressão de todos os ITENS (CHAVES + VALORES) de um dicionário (resulta numa lista com
# três tuplas - basta olhar (parênteses) e [colchetes] no resultado para chegar a essa conclusão.)
print('Impressão dos itens (chaves + valores) de um dicionário:')
print(pessoas.items())
print()

# Acessando chaves, valores e itens através de LAÇOS
print('Acesso à chaves, valores e itens usando laços:')
for chave in pessoas.keys():
    print(chave)
for valores in pessoas.values():
    print(valores)
for itens in pessoas.items():
    print(itens)
print()

# Acessando chaves e valores ASSOCIADOS através de laços
# Ao contrário do que acontece em tuplas e listas, em dicionários não precisamos de 'enumerate'
print('Acesso à combinação chaves + valores através de laços:')
for chave, valores in pessoas.items():
    print(f'{chave}: {valores}')
print()

# APAGANDO a chave 'sexo' e seu conteúdo
print('Apagando uma chave e seu conteúdo:')
del pessoas['sexo']
print(pessoas)
print()

# SUBSTITUINDO VALOR de uma determinada chave
print('Substituindo valor de uma chave:')
pessoas['nome'] = 'Bianca'
print(pessoas)
print()

# ADICIONANDO CHAVE E VALOR em um dicionário (não é necessário usar append)
print('Adicionando chave e valor ao dicionário:')
pessoas['peso'] = 85.3
print(pessoas)
print()

# CRIANDO dicionário dentro de lista
print('Criando um dicionário dentro de uma lista:')
brasil = []                                         # Lista 'brasil'
estado1 = {'uf':'São Paulo', 'sigla':'SP'}          # Dicionário 'estado1'
estado2 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}     # Dicionário 'estado2'
brasil.append(estado1)          # Por 'brasil' ser lista, uso append
brasil.append(estado2)          # Por 'brasil' ser lista, uso append
print(estado1)                  # Imprime o dicionário 'estado1'
print(estado2)                  # Imprime o dicionário 'estado2'
print(brasil)                   # Imprime a lista 'brasil' com 2 elementos (dicionários)
print(brasil[0])                # Imprime o elemento (dicionário) zero da lista
print(brasil[1])                # Imprime o elemento (dicionário) 1 da lista
print()

# Imprimindo o VALOR de uma CHAVE do dicionário contido num ELEMENTO da lista
print('Imprimindo o valor de uma chave, contido num elemento da lista:')
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print()


# ADICIONANDO VALORES ao dicionário via ENTRADA DE USUÁRIO (adicionando por exemplo 3 estados
# ao dicionário 'estado'
print('Adicionando 3 valores ao dicionário via entrada de usuário:')
estado = dict()
federacao = list()
for c in range(0, 3):
    estado['uf'] = str(input('Digite o nome do estado: '))
    estado['sigla'] = str(input('Digite a sigla do estado: '))
    federacao.append(estado.copy()) # No caso de dicionários, não é possível fazer fatiamento
print(federacao)                    # portanto não usamos [:] para copias, mas sim o métodoh
                                    # .copy()

# Imprimindo CHAVES e VALORES de um dicionário contido numa lista usando laços de
# repetição ANINHADOS
print('Imprimindo chaves e valores usando laços de repetição aninhados:')
for estado in federacao:                    # Para cada estado cadastrado (para - dicionário na lista)
    for chave, valor in estado.items():     # Para cada chave e valor do estado cadastrado (para - chave e valor no dicionário)
        print(f'{chave}: {valor}')          # Imprimo chave e valor
print()

# Imprimindo SOMENTE VALORES de um dicionário contido numa lista usando laços de repetição
# ANINHADOS
print('Imprimindo valores usando laços de repetição aninhados:')
for estado in federacao:            # Laço externo para a lista (para - dicionário na lista)
    for valor in estado.values():   # Laço interno para o dicionário (para - valor no dicionário)
        print(valor, end = ' ')
    print()
print()

# Ordenando dicionários de maneira crescente e decrescente
import random
from operator import itemgetter
print('Ordenando dicionários de forma crescente e decrescente:')
jogo = {'Player1':random.randint(1, 6),
        'Player2':random.randint(1, 6),
        'Player3':random.randint(1, 6),
        'Player4':random.randint(1, 6)}
print(f'Dicionário original após randomização:\n{jogo}')
# Para ordenação, criamos um novo dicionário, e o preenchemos com os dados do anterior
# usando a estrutura de repetição FOR, importamos a função itemgetter do módulo operator
# Como a ordenação será baseada no resultado das jogadas de dado, uso (1) após itemgetter
# o qual se refere ao v (valor). Se quisesse ordenar por jogador, usaria (0) que equivale
# ao k (chave).
print('Dicionário ordenado de forma crescente:')
ranking = sorted(jogo.items(), key = itemgetter(1))
print(ranking)
# Finalmente, para ordenar de forma decrescente, usamos o métodoh reverse = True aprendido
# na aula de tuplas
print('Dicionário ordenado de forma decrescente:')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print(ranking)
# Obs.: o resultado final em ambos os casos será uma lista com 4 tuplas (comentário meu: as
# listas são espetaculares de trabalhar, muito mais versáteis).
print()







