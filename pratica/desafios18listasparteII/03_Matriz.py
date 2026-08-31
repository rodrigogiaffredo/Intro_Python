# Criar um programa que gere uma matriz de dimensão 3x3 e preencha com valores lidos pelo
# teclado. No final mostrar a matriz na tela, com a formatação correta. Na hora de entrar
# com valores ele já pergunta "Digite um valor para a posição [0,0], [0,1], [0,2], [1,0],
# [1,1], [1,2], [2,0], [2,1], [2,2]. Se preenchermos a matriz com os números 123456789,
# 123 na primeira linha, 456 na segunda, e 789 na terceira, tudo bem se os números aparecerem
# com colchetes. Os dados ficam numa estrutura única.
# -------------
# | A | B | C |
# -------------
# | D | E | F |
# -------------
# | G | H | I |
# -------------

# NOTA: O PROFESSOR UTILIZOU LISTAS ANINHADAS NA LARGADA, DESDE A DEFINIÇÃO DOS PARÂMETROS
# MATRIZ = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] E FEZ ANINHAMENTO DE LAÇOS LINHA / COLUNA PARA
# O PREENCHIMENTO SEM OS CICLOS DE 3 RODADAS QUE UTILIZEI. ANOTEI A SOLUÇÃO DELE NO
# RASCUNHO C PARA REFERÊNCIA.


# Lista transitória
transitoria = list()
# Listas por linha da matriz
linha1 = list()
linha2 = list()
linha3 = list()
# Lista consolidada
matriz = list()


# Entrada de valores por linha para automatizar as coordenadas:
for c in range(0, 3):
    transitoria.append(int(input(f'Digite o valor da posição [0, {c}]: ')))
    linha1.append(transitoria[:])
    transitoria.clear()

for c in range(0,3):
    transitoria.append(int(input(f'Digite o valor da posição [1, {c}]: ')))
    linha2.append(transitoria[:])
    transitoria.clear()

for c in range(0,3):
    transitoria.append(int(input(f'Digite o valor da posição [2, {c}]: ')))
    linha3.append(transitoria[:])
    transitoria.clear()

# Preenchimento da matriz considerando cada linha um elemento:
matriz.append(linha1[:])
matriz.append(linha2[:])
matriz.append(linha3[:])

# Imprimindo a matriz, um elemento por linha:
print('-' * 15)
print('Matriz'.center(15))
print('-' * 15)
for c in range(0, 3):
    print(matriz[c])
    print('-' * 15)

