# Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Fazer um
# programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))

# Por se tratar da escolha de um str usamos random.choice (fui na tentativa e erro e no
# bom senso, e na hora da sintaxe o autocomplete ajudou com os [].

s = choice([n1, n2, n3, n4])

print(f'O(a) aluno(a) sorteado(a) para apagar a lousa foi {s}')
