# Criar um pequeno sistema modularizado que permita cadastrar pessoas em um arquivo de
# texto simples. O sistema só tem 2 opções: cadastrar uma pessoa e listar todas as pessoas
# cadastradas, a prova de usuário. Os novos nomes aparecem sempre no final da fila quando
# rodamos o cadastro de novo. Se o arquivo de texto não existir na execução do programa,
# o programa deve ser capaz de criar o arquivo pra mim.



from libdesafio03.interface import *
from libdesafio03.arquivo import *
from time import sleep

# PARTE B - (USO DE ARQUIVOS .TXT)
file = 'Aula23Desafio03.txt'
if not arquivoexiste(file):
    criararquivo(file)


# PARTE A - (MENU)
while True:
    resp = menu(['\033[34mVer pessoas cadastradas\033[m',
                 '\033[34mCadastrar nova pessoa\033[m',
                 '\033[34mSair do sistema\033[m'])
    if resp == 1:
        lerarquivo(file)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        # PARTE C - (CADASTRANDO DADOS NO ARQUIVO TXT)
        cadastrar(file, nome, idade)
    elif resp == 3:
        cabecalho('>>>>> FIM <<<<<')
        break
    else:
        print('\033[31mERRO: digite uma opção válida\033[m')
    sleep(1)






