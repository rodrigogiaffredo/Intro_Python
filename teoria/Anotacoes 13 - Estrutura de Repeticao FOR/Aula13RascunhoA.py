# Repetições também são chamadas de iterações ou laços.

# A estrutura de repetição FOR é um laço com variável de controle (contador no caso).

# Sintaxe genérica: laço 'c' no intervalo (x, y)
#                       <comando no laço>
#                   <comando fora do laço>
# onde C é a variável de controle; X, Y são respectivamente de / até na contagem da repetição;
# <comando no laço> é o conjunto de ações que será executado no intervalo de repetições, e
# <comando fora do laço> é o que acontece após o fim das repetições.

# Sintaxe do Python: num exemplo onde o range de contagem vá de 1 a 10, e a variável de
# controle se chame 'c', de contador (não esquecer dos dois pontos no final).

# for c in range (1, 10):
#   comando no laço
# comando fora do laço

# É possível executar mais de um comando dentro do laço, o que é razoável apenas se o número
# de repetições dos N comandos for idêntico. No exemplo abaixo, ambos os comandos (A e B)
# serão executados 3x:

# for c in range (0,3):
#   comando A no laço
#   comando B no laço
# comando fora do laço

# Fora do laço também não há limite de comandos, mas basicamente porque se trata da continuidade
# do programa em si.


# Uma possibilidade interessantíssima é o uso de estruturas condicionais dentro das de
# repetição. Imagine que tenhamos um comando C no laço, que somente será executado em alguma
# condição específica dentro da estrutura de repetição. A identação é o fator chave para
# organizar onde a condição será testada. No exemplo abaixo, uma ação a mais será imposta
# somente se uma determinada condição for atendida, enquanto as outras ações ocorrerão N
# vezes de acordo com o que for instruído no range.

# for c in range (1, 10):
#   if CONDICAO == ATENDIDA:
#       comando C no laço
#   comando A no laço
#   comando B no laço
# comando fora do laço

