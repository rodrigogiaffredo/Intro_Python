# Criar um pequeno sistema modularizado que permita cadastrar pessoas em um arquivo de
# texto simples. O sistema só tem 2 opções: cadastrar uma pessoa e listar todas as pessoas
# cadastradas. Quando dá o play aparece pontilhada MENU PRINCIPAL pontilhada, um menu de 3
# opções (só os textos em azul, números na cor do sistema) 1- Ver pessoas cadastradas
# 2- Cadastrar nova pessoa 3- Sair do sistema, pontilhada, (em verde)'Sua opção: '
# Se clicar 1 aparece pontilhada PESSOAS CADASTRADAS pontilhada, e uma lista com nome
# completo e idade (X anos) arrumados estilo boletim. Daí mostra o menu de novo. Com aquele
# sleepzinho malandro. Se clicar em 2- pontilhada NOVO CADASTRO pontilhada, campo
# 'Nome: ', 'Idade: ' (so numero), dai mostra uma linha 'Cadastro de Fulano de tal
# confirmado.' dai escolhe 1 de novo e a nova pessoa já aparece na lista. Se digitar 3,
# pontilhada 'Programa finalizado, obrigado por utilizar' pontilhada. E se fechar o
# programa e abrir de novo, a ultima pessoa cadastrada continua cadastrada, porque não
# ficou na memoria o registro, mas sim num arquivo texto simples. Se digitar uma opção
# que não tem no menu, retorna em vermelho 'ERRO: digite uma opção válida: ' Outra coisa,
# se digitar a idade por extenso, mostra em vermelho 'ERRO: para idade digite um número
# inteiro' e pede idade de novo. Os novos nomes aparecem sempre no final da fila quando
# rodamos o cadastro de novo. Se o arquivo de texto não existir na execução do programa,
# o programa deve ser capaz de criar o arquivo pra mim.

# Aqui eu peidei gostoso, joguei a toalha e fui resolvendo durante a apresentação da solução


# PARTE B - SEGUNDO VÍDEO DE CORREÇÃO (USO DE ARQUIVOS .TXT)

from libdesafio03.interface import *


def arquivoexiste(arquivo):
    try:
        # Para verificar se o arquivo existe, vamos tentar abrí-lo e fecha-lo
        # Comando para abertura de arquivo como leitura ('rt' = read text)
        a = open(arquivo, 'rt')
        # Fechar o arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(arquivo):
    try:
        # Para criar um arquivo texto, usamos ('wt' = write text seguido do sinal de '+'
        # justamente para o caso de o arquivo ainda não existir - se existir ele apenas
        # escreve no arquivo, senão já cria um novo.)
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print(f'Erro ao criar o arquivo {arquivo}.')
    else:
        print(f'Arquivo {arquivo} criado com sucesso.')


def lerarquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print(f'Erro ao ler o arquivo {arquivo}.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        # Mostrando os dados do arquivo de forma estruturada
        for linha in a:
            # Como usei ';' de separador no arquivo 'txt', divido por ';' via 'split'
            dado = linha.split(';')
            # Removendo a quebra de linha (\n) que incluí ao cadastrar a pessoa
            dado[1] = dado[1].replace('\n', '')
            # Como o cadastro é uma lista, podemos usar formatação para melhorar a
            # apresentação dos dados
            print(f'{dado[0]:<35}{dado[1]:>3} anos')

    finally:
        a.close()



# PARTE C - TERCEIRO VÍDEO DE CORREÇÃO (CADASTRANDO DADOS NO ARQUIVO .TXT)

def cadastrar(file, nome = 'desconhecido', idade = 0):
    try:
        # Para atualizar o arquivo 'txt' usamos 'at' (append text)
        a = open(file, 'at')
    except:
        print(f'\033[31mERRO: não foi possível abrir o arquivo {file}.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\033[31mERRO: não foi possível atualizar o arquivo {file}.\033[m')
        else:
            print(f'Dados de {nome} adicionados com sucesso.')
            a.close()
