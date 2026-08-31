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

# PARTE A - PRIMEIRO VÍDEO DE CORREÇÃO

def leiaint(msg):
    while True:
        try:
            opcao = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: opção inválida, digite novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[31mPrograma encerrado pelo usuário.\033[m')
            return 3
        else:
            return opcao


def linha(tam = 45):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(45))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opcao = leiaint('\033[32mSua opção:\033[m ')
    return opcao
