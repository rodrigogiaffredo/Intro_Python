# lista:                Pessoas
# dado:                 Pedro 25    Maria 19    João 32
# elemento (em dados):   0    1       0   1      0   1
# ------------------------------------------------------
# elemento(em pessoas):     0           1           2
# item (em pessoas):        1           2           3


# Primeira lista
print('Criação da primeira lista:')
teste = list()
teste.append('Rodrigo')
teste.append(49)
print(teste)
print()

# Segunda lista por ligação ao invés de cópia
print('Criação da segunda lista a partir da primeira:')
galera = list()
galera.append(teste)
print(galera)
print()

# Mudando dados na primeira lista, porém com listas ligadas
print('Mudando dados na primeira lista com ligação ao invés de cópia:')
teste[0] = 'Maria'
teste[1] = 22
print(teste)
print()

# Como eu fiz uma ligação entre listas, e não uma cópia de uma para dentro da outra, as
# alterações dos dados são replicadas na origem, por isso vai aparecer 'Maria' 22 por 2
# vezes (a primeira referente a lista original, e a segunda referente ao novo append.
print('Listas ligadas, substituição do item na lista original ao invés de junção de listas:')
galera.append(teste)
print(galera)
print()

# Fazendo por cópia, ocorrerá a inclusão dos novos dados sem substituição dos anteriores

# Criando a primeira lista

print('Criação da nova primeira lista:')
novalista = list()
novalista.append('Bianca')
novalista.append(48)
print(novalista)
print()

# Segunda lista, agora sim por cópia
print('Criação da nova segunda lista a partir da primeira, só que com cópia ao invés de ligação:')
novagalera = list()
novagalera.append(novalista[:])
print(novagalera)
print()

# Mudando dados na primeira lista, agora com cópia ao invés de ligação
print('Mudando dados da primeira lista mas agora com cópia:')
novalista[0] = 'Maria'
novalista[1] = 22
print(novalista)
print()

# Conectando as 2 listas mas agora partindo de cópias, e não de ligações, agora sim chegando
# no resultado de juntar as 2 listas com dados diferentes
print('Conectando listas por cópia ao invés de por ligação:')
novagalera.append(novalista[:])
print(novagalera)
print()

# Declarando diversos valores numa nova lista (no exemplo são 4 estruturas compostas dentro de
# uma outra estrutura composta maior.
print('Declarando diversas estruturas compostas dentro de outra estrutura composta:')
turma = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(turma)
print()

# Mostrando só o elemento zero da nova estrutura composta
print('Mostrando o elemento 0 da nova estrutura composta:')
print(turma[0])
print()

# Mostrando o elemento 0 do elemento 0 da nova estrutura composta
print('Mostrando o elemento 0 DO elemento 0 da nova estrutura composta:')
print(turma[0][0])
print()

# Mostrando o elemento 1 do elemento 2 da nova estrutura composta
print('Mostrando o elemento 1 DO elemento 2 da nova estrutura composta:')
print(turma[2][1])
print()

# Imprimir os dados de cada pessoa usando estrutura de repetição FOR
print('Imprimindo os dados de cada pessoa da nova estrutura usando repetição FOR:')
for p in turma:
    print(p)
print()

# Imprimindo somente os nomes de cada pessoa usando estrutura de repetição FOR
print('Imprimindo somente os nomes de cada pessoa da nova estrutura usando repetição FOR:')
for p in turma:
    print(p[0])
print()

# Imprimindo somente as idades de cada pessoa usando estrutura de repetição FOR
print('Imprimindo somente as idades de cada pessoa da nova estrutura usando repetição FOR:')
for p in turma:
    print(p[1])
print()

# Imprimindo nome e idade em estrutura formatada f-string
print('Imprimindo os dados da nova estrutura formatados, usando f-string.')
for p in turma:
    print(f'{p[0]}, {p[1]} anos')
print()

# Capturando dados para uma lista através do teclado
print('Capturando novos dados para uma lista através do teclado:')
turmanova = list()
novodado = list()
for c in range(0, 3):
    novodado.append(str(input('Nome: ')))
    novodado.append(int(input('Idade: ')))
    # Atualizando a lista principal através do append com cópia
    turmanova.append(novodado[:]) # Sempre com cópia
    # Limpando a lista transitória para que ela possa receber a próxima entrada, e como
    # usamos cópia, ele não apaga o dado da lista original 'turmanova'.
    novodado.clear()
print(turmanova)
print()

# Mostrando dados a partir de condições especificadas no enunciado, por exemplo, separando
# pessoas maiores de 21 anos, das menores de 21 anos, e totalizar por faixa.
totmaior = totmenor = 0
for p in turmanova:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade pois tem {p[1]} anos.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade pois tem {p[1]} anos.')
        totmenor += 1
print(f'Portanto, a turma tem {totmaior} maior(es) de idade, e {totmenor} menor(es) de idade.')
print()



# Criando uma lista composta de largada, e atualizando valores diretamente nela, sem merge
# Por exemplo, uma lista que contenha números pares numa sublista alocada no elemento zero,
# e números ímpares numa sublista alocada no elemento 1.
print('Criação de listas aninhadas já na definição dos parâmetros:')
numeros = [[], []]
valor = 0
for c in range(0, 5):
    valor = int(input(f'Digite o {c + 1}o. valor: '))
    if valor % 2 == 0:
        # Posso fazer append dentro de uma coordenada, pois nela há uma sublista
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-' * 30)
print(f'Pares e ímpares agrupados na lista: {numeros}')
print()



# Ainda na lógica de lista completa na largada, criando matrizes (3 x 3 no exemplo) usando
# laços aninhados (um para linhas, outro para colunas) e listas
print('Usando laços aninhados e listas aninhadas já na definição dos parâmetros para contrução de matrizes:')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Laço das linhas
for l in range(0, 3):
    # Laço das colunas
    for c in range(0,3):
        # Entrada de dados
        matriz[l][c] = int(input(f'Digite o valor da coordenada [{l}, {c}]: '))
print('-' * 30)
# Impressão em formato de matriz
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    # Volta na identação da linha para fazer a quebra
    print()
print()






