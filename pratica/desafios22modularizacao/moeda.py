# Criar um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro(), e metade(). Fazer também um programa que importe esse módulo e use
# algumas dessas funções. O programa principal rodando abre um campo 'digite o preço R$: ',
# e mostro em linhas separadas 'a metade do preço é', 'o dobro do preço é', 'aumentando 10%
# temos', e 'reduzindo 13% temos' só que nenhuma das funções está no código, o código só
# tem o input  e os prints, tipo print('Reduzindo 13% temos {moeda.diminuir(preco, 13)}.
# Não é pra caprichar nos valores monetários, porque isso é missão do próximo desafio.

# Adaptar o código da Aula22Desafio01 criando uma função adicional chamada moeda() que
# consiga mostrar os valores como um valor monetário formatado. Vamos manter o arquivo
# anterior e criar um novo, com a atualização. Ou seja, se antes eu só aplicava
# moeda.metade, moeda.dobro, etc. agora vou aplicar moeda.moeda(moeda.metade(preco)) e os
# valores vão aparecer com R$ antes deles, e ,00 no final. Os nomes moeda.moeda e
# moeda.metade são de propósito pois vamos arrumar isso no próximo desafio.


# Solução do professor para o desafio 3, replicável para todos os cálculos:
# Ele criou uma variável 'res' ao invés de ir direto para o return, e aplicou as funções
# na variável, encurtando bem o código. Ficou assim:
# def aumentar(preco, taxa, formato = False):
#   res = preco + (preco * taxa/100))
#   return res if formato is False else return moeda(res)

def aumentar(preco, taxa, formato = False):
    if formato == True:
        return f'{moeda(preco + (preco * taxa/100))}'
    else:
        return preco + (preco * taxa/100)

def diminuir(preco, taxa, formato = False):
    if formato == True:
        return f'{moeda(preco - (preco * taxa/100))}'
    else:
        return preco - (preco * taxa/100)

def dobro(preco, formato = False):
    if formato == True:
        return f'{moeda(preco * 2)}'
    else:
        return preco * 2

def metade(preco, formato = False):
    if formato == True:
        return f'{moeda(preco / 2)}'
    else:
        return preco / 2

def moeda(preco, simbolo = 'R$ '):
    return f'{simbolo}{preco:.2f}'.replace('.', ',')

def resumo(preco, taxareducao, taxaaumento):
    print('-' * 40)
    print('ANÁLISE DO PREÇO'.center(40))
    print('-' * 40)
    print(f'{'Preço analisado':<25}{moeda(preco):>15}')
    print(f'{'Metade do preço':<25}{metade(preco, True):>15}')
    print(f'{'Dobro do preço':<25}{dobro(preco, True):>15}')
    print(f'{taxareducao}{'% de desconto':<23}{diminuir(preco, taxareducao, True):>15}')
    print(f'{taxaaumento}{'% de aumento':<23}{aumentar(preco, taxaaumento, True):>15}')
    print('-' * 40)
