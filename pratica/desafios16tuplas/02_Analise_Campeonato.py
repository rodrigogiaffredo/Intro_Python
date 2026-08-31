# Criar uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato
# brasileiro de futebol, na ordem de colocação. Mostrar: 1- apenas os 5 primeiros colocados
# 2- os últimos 4 colocados 3- uma lista com os times em ordem alfabética 4- em que posição
# na tabela está o time da Chapecoense.

tabela = ('palmeiras', 'flamengo', 'fluminense', 'athletico pr', 'bragantino', 'bahia',
          'coritiba', 'sao paulo', 'atletico mg', 'corinthians', 'cruzeiro', 'botafogo',
          'vitoria', 'internacional', 'santos', 'gremio', 'vasco', 'remo', 'mirassol',
          'chapecoense')

c = 1

print('-' * 31)
print('CAMPEONATO BRASILEIRO - SÉRIE A')
print('-' * 31)
print('Classificação Geral - Top 5')
print('-' * 31)

while c <= 5:
    print(f'{c}o. colocado: ',tabela[c-1].title())
    c += 1

print('-' * 31)


c = -4
print('Últimos 4 colocados:')
print('-' * 31)

while c <= -1:
    if c != -1:
        print(tabela[c].title())
    else:
        print('E na lanterna:', tabela[c].title())
    c += 1

print('-' * 31)
print('Tabela em ordem alfabética:')
print('-' * 31)

ordenada = sorted(tabela)

for c in range(0, len(ordenada)):
    print(ordenada[c].title())
    c += 1




print('-' * 31)

print(f'Posição atual da Chapecoense: {(tabela.index('chapecoense')+1)}o. lugar')

print('-' * 31)





