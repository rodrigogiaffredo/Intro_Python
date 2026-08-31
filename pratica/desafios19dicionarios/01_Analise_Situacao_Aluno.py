# Fazer um programa que leia nome e média de um aluno, guardando também a situação em um
# dicionário. No final, mostrar o conteúdo da estrutura na tela. Média 7 ou mais aluno
# aprovado, mas não vamos perguntar, vamos aferir depois de o usuário entrar com o valor.

aluno = dict()

aluno['Nome'] = str(input('Digite o nome do aluno: ')).capitalize().strip()
aluno['Média'] = float(input(f'Digite a média de {aluno['Nome'].capitalize()}: '))
if aluno['Média'] >= 7:
    aluno['Status'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Status'] = 'Recuperação'
else:
    aluno['Status'] = 'Reprovado'
print('-' * 30)
print(aluno) # Para simples conferência
print('-' * 30)
print(f'O nome do aluno é {aluno['Nome']}.')
print(f'A média de {aluno['Nome']} é {aluno['Média']:.2f}.')
print(f'Situação de {aluno['Nome']}: {aluno['Status']}.')
print('-' * 30)
print('-- Fim do Programa --')
print()

# A solução do professor é mais elegante, e treina o FOR com chave e valor, lembrando que
# para dicionários não precisamos do enumerate (usado em listas).
# Importante notar também que os nomes das chaves de dicionários podem conter acentos, então
# dá para acelerar a visualização dos dados sem perda de qualidade.
print('-' * 30)
print('O professor usou um FOR para mostrar os dados:')

for k, v in aluno.items():
    print(f'{k}: {v}')




