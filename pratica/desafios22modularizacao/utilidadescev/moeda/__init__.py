# Criar um pacote chamado utilidadescev que tenha dois módulos internos chamados moeda e
# dado. Transferir todas as funções utilizadas em Aula22Desafio01, Aula22Desafio02,
# Aula22Desafio03 e Aula22Desafio04 para o primeiro pacote e manter tudo funcionando no
# programa principal. O código a ser utilizado é exatamente o mesmo da Aula22Desafio04
# mas com o novo import.

# Solução do professor para o desafio 3, replicável para todos os cálculos:
# Ele criou uma variável 'res' ao invés de ir direto para o return, e aplicou as funções
# na variável, encurtando bem o código. Ficou assim:
# def aumentar(preco, taxa, formato = False):
#   res = preco + (preco * taxa/100))
#   return res if formato is False else return moeda(res)

def aumentar(preco, taxa, formato = False):
    """
    --> Aumenta o valor digitado pelo usuário aplicando uma taxa
    :param preco: valor digitado pelo usuário
    :param taxa: taxa % de aumento
    :param formato: (opcional), True para formatação monetária, False sem formatação
    :return: valor digitado acrescido da taxa, formatado ou não
    """
    if formato == True:
        return f'{moeda(preco + (preco * taxa/100))}'
    else:
        return preco + (preco * taxa/100)

def diminuir(preco, taxa, formato = False):
    """
    --> Diminui o valor digitado pelo usuário aplicando uma taxa
    :param preco: valor digitado pelo usuário
    :param taxa: taxa% de redução
    :param formato: (opcional), True para formatação monetária, False sem formatação
    :return: valor digitado reduzido da taxa, formatado ou não
    """
    if formato == True:
        return f'{moeda(preco - (preco * taxa/100))}'
    else:
        return preco - (preco * taxa/100)

def dobro(preco, formato = False):
    """
    --> Dobra o valor digitado pelo usuário
    :param preco: valor digitado pelo usuário
    :param formato: (opcional), True para formatação monetária, False sem formatação
    :return: o dobro do valor digitado
    """
    if formato == True:
        return f'{moeda(preco * 2)}'
    else:
        return preco * 2

def metade(preco, formato = False):
    """
    --> Divide o valor digitado pelo usuário pela metade
    :param preco: valor digitado pelo usuário
    :param formato: (opcional), True para formatação monetária, False sem formatação
    :return: a metade do valor digitado
    """
    if formato == True:
        return f'{moeda(preco / 2)}'
    else:
        return preco / 2

def moeda(preco, simbolo = 'R$ '):
    """
    --> Formata o valor digitado pelo usuário para o padrão moeda
    :param preco: valor digitado pelo usuário
    :param simbolo: (opcional), default 'R$' (Reais brasileiros)
    :return: valores formatados em padrão monetário
    """
    return f'{simbolo}{preco:.2f}'.replace('.', ',')

def resumo(preco, taxareducao, taxaaumento):
    """
    --> Cria tabela valor, dobro, metade, aumento e redução, a partir de entrada do usuário
    :param preco: valor digitado pelo usuário
    :param taxareducao: % de desconto
    :param taxaaumento: % de acréscimo
    :return: não se aplica (é um procedimento)
    """
    print('-' * 40)
    print('ANÁLISE DO PREÇO'.center(40))
    print('-' * 40)
    print(f'{'Preço analisado':<25}{moeda(preco):>15}')
    print(f'{'Metade do preço':<25}{metade(preco, True):>15}')
    print(f'{'Dobro do preço':<25}{dobro(preco, True):>15}')
    print(f'{taxareducao}{'% de desconto':<23}{diminuir(preco, taxareducao, True):>15}')
    print(f'{taxaaumento}{'% de aumento':<23}{aumentar(preco, taxaaumento, True):>15}')
    print('-' * 40)