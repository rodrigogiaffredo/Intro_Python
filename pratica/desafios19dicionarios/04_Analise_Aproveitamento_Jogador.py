# Criar um programa que gerencie o aproveitamento de um jogador de futebol. O programa lê
# o nome do jogador e quantas partidas ele jogou. Depois o programa pergunta a quantidade de
# gols feitos em cada partida. No final, todas as informações são guardadas num dicionário,
# incluindo o total de gols feitos durante o campeonato. O aproveitamento é uma lista com os
# gols por partida. Daí o dicionário vai conter o nome, o número de partidas, e o total de
# gols do jogador.

aproveitamento = dict()
gols = list()

aproveitamento['Jogador'] = str(input('Digite o nome do jogador: ')).capitalize().strip()
partidas = int(input(f'Quantas partidas {aproveitamento['Jogador']} jogou?: '))

for c in range(0, partidas):
    # Lembrando que podemos declarar direto o conteúdo do dicionário referenciando o item
    # na captura do dado, e essa lógica serve para append também (no caso vou suar append
    # pois o dado vai para uma lista contida no dicionário).
    gols.append(int(input(f'Quantos gols {aproveitamento['Jogador']} marcou na {c + 1}a. '
                          f'partida?: ')))

aproveitamento['Gols_por_partida'] = gols

# Para totalizar os gols, basta somar o conteúdo da lista 'gols' usando a função sum.
aproveitamento['Total_de_gols'] = sum(gols)

print('-' * 45)
print(aproveitamento)
print('-' * 45)

for k, v in aproveitamento.items():
    print(f'{k}: {v}')

print('-' * 45)
# Para saber o número de partidas, o professor usou o len(gols) pois esta lista registra
# quantos gols o jogador fez por partida, portanto o número de partidas está implícito.
# Isso é particularmente útil quando precisar entrar com mais de um jogador, como eu vi
# adiante no desafio 06, quebrei bem a cabeça.
print(f'{aproveitamento['Jogador']} jogou {len(aproveitamento['Gols_por_partida'])} partidas'.upper().center(45))
print('Desempenho por partida'.upper().center(45))
print('-' * 45)


for g in range(0, len(gols)):
    print(f'{g + 1}a. partida: {gols[g]} gols')

print('-' * 45)
# O professor usou um FOR com chave e valor na correção, acessando a lista diretamente
# resultando no mesmo funcionamento.
print('O professor usou chave e valor na correção (acessando a lista diretamente), mesmo funcionamento.')
for k, v in enumerate(gols):
    print(f'Na {k + 1}a. partida {aproveitamento['Jogador']} fez {v} gols.')

print('-' * 45)
print(f'Total de gols marcados por {aproveitamento['Jogador']}: {sum(gols)}'.upper())

print('-' * 45)
print('-- Fim do Programa --')

