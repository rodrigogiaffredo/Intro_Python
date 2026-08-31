# importando o módulo matemático inteiro

#import math
#n = int(input('Digite um número: '))
# por eu ter importado a biblioteca math, consigo calcular raíz quadrada via função
#raiz = math.sqrt(n)
#print(f'A raiz quadrada de {n} é igual a {raiz:.2f}.')
# se eu quiser mostrar o número arredondado para cima
#print(f'A raiz quadrada de {n} arredondada para cima é igual a {math.ceil(raiz)}.')
# e se eu quiser mostrar o número arredondado para baixo
#print(f'A raiz quadrada de {n} arredondada para baixo é igual a {math.floor(raiz)}.')

# Porém existe também a possibilidade de importar fragmentos da biblioteca matemática:
# Dica: usando o from, basta digitar ctrl + espaço após a palavra import e a lista de funções
# é aberta para selecionarmos, caso não saibamos de cor.

# posso importar somente funções específicas dentro de uma biblioteca, inclusive mais de uma
# separadas por vírgula
from math import sqrt, floor
n = int(input('Digite um número: '))
# como agora importei somente as funções raiz quadrada e arredondamento para baixo, não peciso
# usar o sufixo math nem na variável, nem na f-string.
raiz = sqrt(n)
print(f'A raiz quadrada de {n} é igual a {raiz:.1f}.')
print(f'A raiz quadrada de {n} arredondada para baixo é igual a {floor(raiz)}.')

# A lista de bibliotecas disponíveis no Python está no site oficial python.org na seção
# documentação da versão específica que estamos usando (clicando aqui no PyCharm em Console
# a gente sabe qual é a versão certinha, passando o mouse sobre o markdown Python Console).
