# Aprimorar o desafio anterior, mostrando no final: 1- a soma de todos os valores pares
# digitados 2- a soma dos valores da terceira coluna 3- o maior valor da segunda linha.
# Ou seja, entramos com os números, montamos a matriz, e respondemos a analise em 3 linhas.
# 'A soma dos valores pares é X.' 'A soma dos valores da terceira coluna é Y'. 'O maior
# valor da segunda linha é Z.'

# Enunciado anterior

# # Criar um programa que gere uma matriz de dimensão 3x3 e preencha com valores lidos pelo
# # teclado. No final mostrar a matriz na tela, com a formatação correta. Na hora de entrar
# # com valores ele já pergunta "Digite um valor para a posição [0,0], [0,1], [0,2], [1,0],
# # [1,1], [1,2], [2,0], [2,1], [2,2]. Se preenchermos a matriz com os números 123456789,
# # 123 na primeira linha, 456 na segunda, e 789 na terceira, tudo bem se os números aparecerem
# # com colchetes. Os dados ficam numa estrutura única.
# # -------------
# # | A | B | C |
# # -------------
# # | D | E | F |
# # -------------
# # | G | H | I |
# # -------------


# NOTA: VIDE OBSERVAÇÕES DO DESAFIO ANTERIOR SOBRE LISTAS AGRUPADAS
# NA DEFINIÇÃO DOS PARÂMETROS, E SOBRE LAÇOS ANINHADOS PARA PREENCHIMENTO DE LINHAS E
# COLUNAS SEM INTERRUPÇÕES. TRATA-SE DE UMA SOLUÇÃO MAIS ELEGANTE.


# Lista transitória para entrada de valores
transitoria = list()
# Lista de valores por linha:
linha1 = list()
linha2 = list()
linha3 = list()
# Matriz consolidada
matriz = list()
# Variáveis de cálculo
somapares = 0
somaterceiracol = 0


# Entrada de valores

for c in range(0, 3):
    transitoria.append(int(input(f'Digite o valor da posição [0, {c}]: ')))
    linha1.append(transitoria[:])
    # Verificando e somando entradas pares
    if transitoria[0] % 2 == 0:
        somapares += transitoria[0]
    # Somando terceira coluna
    if c == 2:
        somaterceiracol += transitoria[0]
    transitoria.clear()

for c in range(0, 3):
    transitoria.append(int(input(f'Digite o valor da posição [1, {c}]: ')))
    linha2.append(transitoria[:])
    # Verificando e somando entradas pares
    if transitoria[0] % 2 == 0:
        somapares += transitoria[0]
    # Somando terceira coluna
    if c == 2:
        somaterceiracol += transitoria[0]
    transitoria.clear()

for c in range(0, 3):
    transitoria.append(int(input(f'Digite o valor da posição [2, {c}]: ')))
    linha3.append(transitoria[:])
    # Verificando e somando entradas pares
    if transitoria[0] % 2 == 0:
        somapares += transitoria[0]
    # Somando terceira coluna
    if c == 2:
        somaterceiracol += transitoria[0]
    transitoria.clear()


# Montando e imprimindo a matriz
matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)

print()
print('-' * 20)
print('Matriz'.center(20))
print('-' * 20)
for c in range(0, 3):
    print(matriz[c])
    print('-' * 20)



# Montando e imprimindo a análise
print()
print('-' * 50)
print('Análise'.center(50))
print('-' * 50)

print(f'A soma dos valores pares digitados é igual a {somapares}')
print(f'A soma dos valores da terceira coluna é igual a {somaterceiracol}')
print(f'O maior valor digitado na linha 2 foi {max(linha2)}')

print('-' * 50)
print('-- Fim do Programa --')


