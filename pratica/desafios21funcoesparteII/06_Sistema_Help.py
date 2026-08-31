# Fazer um mini-sistema que utilize interactive help do Python. O usuário vai digitar o
# comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM' o programa
# encerrará. Usar cores.

def cabecalho(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'{texto:^{tamanho}}')
    print('~' * tamanho)

def ajuda(funcao = 0):
    from time import sleep
    while funcao != 'fim':
        cabecalho('\33[97;42mSistema Help\33[m')
        funcao = str(input('Função da biblioteca > ')).lower().strip()
        if funcao == 'fim':
            sleep(0.5)
            cabecalho('\33[97;41mObrigado por utilizar o Sistema Help!\33[m')
            break
        else:
            sleep(0.5)
            cabecalho(f'\33[97;44mAcessando o manual da função {funcao}...\33[m')
            sleep(1.5)
            help(funcao)
            sleep(2.5)


# Programa principal
ajuda()


# A solução do professor é bem diferente da minha, vale a pena deixar no backlog a
# possibilidade de assistir a correção do exercício 106 (aula 21, módulo 3), pelo
# lance de criar uma lista global de cores que podem ser chamadas na execução do
# programa.