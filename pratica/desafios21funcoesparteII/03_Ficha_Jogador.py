# Fazer um programa que tenha uma função chamada ficha() que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
# de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = False, gols = 0):
    print()
    print('-' * 35)
    nome = str(input('Digite o nome do jogador: ')).title().strip()
    if nome == '':
        nome = '<desconhecido>'
    gols = str(input(f'Total de gols: '))
    # Na correção o professor falou sobre se o usuário digitar três ao invés de 3
    # por exemplo, ou seja, palavras ao invés de números para total de gols
    if gols.strip() == '' or gols.isdecimal() not in [True]:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

# Programa principal
print(ficha())


