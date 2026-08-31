# Um programa que calcula a média de um aluno com base nas notas
# informadas e no nome.

nome = input('Digite o nome do aluno(a): ')
n1 = float(input(f'Digite a primeira nota de {nome}: '))
n2 = float(input(f'Digite a segunda nota de {nome}: '))
m = (n1+n2)/2
print(f'Com base nas informações prestadas (n1 = {n1:.1f} e n2 = {n2:.1f}):\nA média de {nome} é {m:.1f}.')
