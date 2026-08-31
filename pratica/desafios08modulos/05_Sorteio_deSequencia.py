# O mesmo professor do desafio anterior (04) quer sortear a ordem de apresentação
# de trabalhos dos 4 alunos. Fazer um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.

import random

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]


# Tive que acessar a documentação oficial do Python e conversar com o NotebookLM para
# entender meu erro. Estava colocando random.shuffle(lista) dentro da f-string, mas este
# comando reorganiza e substitui a lista original, portanto tenho que roda-lo antes do
# comando print, pois o conteúdo das variáveis será alterado.

random.shuffle (lista)

print(f'(Com shuffle) Segue a ordem de apresentação dos trabalhos de hoje:\n>>>{lista}')

# Caso eu queira usar a randomização diretamente na f-string, o ideal é outro comando:
# random.sample, este sim podendo ser chamado diretamente no print. Nele eu aponto o
# endereço atual da lista de nomes, e o tamanho da amostra final que deve ser gerada.
# Não há alteração no conteúdo das variáveis, apenas o embaralhamento na nova lista.

print(f'(Com sample) Segue a ordem de apresentação dos trabalhos de hoje:\n>>>{random.sample(lista,4)}')
