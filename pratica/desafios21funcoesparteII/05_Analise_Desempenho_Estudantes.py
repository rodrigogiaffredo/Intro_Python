# Fazer um programa que tenha uma função notas() que pode receber várias notas de alunos e
# retorne um dicionário com as seguintes informações: 1- quantidade de notas 2- a maior nota
# 3- a menor nota 4- a media da turma 5- a situação (opcional, tem que passar sim ou não).
# Adicionar também as docstrings da função.

#   -> Função para analisar notas e situações de vários alunos.
# param n: uma ou mais notas dos alunos (aceita várias)
# param sit: valor opcional, indicando se deve ou não adicionar a situação
# return: dicionário com várias informações sobre a situação da turma

def notas(*nota, sit = False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação da turma.
    :return: Dicionário com várias informações sobre a turma.
    """
    resp = dict()
    resp['total'] = len(nota)
    resp['maior'] = max(nota)
    resp['menor'] = min(nota)
    resp['media'] = f'{(sum(nota)/len(nota)):.2f}'
    if sit == True:
        if str(resp['media']) >= '7':
            resp['situacao'] = 'BOA'
        elif str(resp['media']) >= '5':
            resp['situacao'] = 'RAZOÁVEL'
        else:
            resp['situacao'] = 'RUIM'
    return resp


# Programa principal
print()
resp = notas(4.6, 9.4, 5.7, 6.5, 7.75, 1.6, 5.8, sit = True)
print(resp)
print()
print(f'\33[97;44mInteractive Help da função << notas >>\33[m')
help(notas)
