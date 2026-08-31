# Aprimorar o desafio da performance do jogador de futebol para que ele funcione com
# vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de
# cada jogador. Pede nome do jogador, pergunta quantas partidas fulano jogou,
# pergunta quantos gols fez na 'tal', pergunta se quer continuar.

# No final, todas as informações são guardadas num dicionário, incluindo o total de gols
# feitos durante o campeonato. O aproveitamento é uma lista com os gols por partida. Daí o
# dicionário vai conter o nome, o número de partidas, e o total de gols do jogador.

# Parou de cadastrar, mostra: resumo contendo ID, nome, gols p partida
# (a lista de gols), total de gols (em 4 colunas diferentes) e aprofunda a análise de um
# jogador específico a escolha do usuário. A prova de usuário em todos os passos e
# perguntas, inclusive na hora de escolher ID de jogador.


performance = dict() # Nome, Lista de gols e Saldo de gols do jogador
lista_gols = list() # Gols por partida do jogador
nro_partidas = list() # Partidas disputadas pelo jogador
tot_gols = 0 # Contagem para preenchimento da lista saldo_gols
ranking = list() # Lista com os dicionários de todos os jogadores

# Entrada de dados do jogador
while True:
    performance['Nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    performance['Partidas_disputadas'] = int(input(f'Quantas partidas {performance['Nome']} jogou?: '))
    nro_partidas.append(performance['Partidas_disputadas'])
    for c in range(0, performance['Partidas_disputadas']):
        gols = int(input(f'Quantos gols {performance['Nome']} fez na {c + 1}a. partida?: '))
        # Atualização da lista de gols por partida do jogador
        lista_gols.append(gols)
        tot_gols += gols
        performance['Gols_por_partida'] = lista_gols.copy()
        # Atualização do total de gols do jogador
        performance['Saldo_de_gols'] = tot_gols

    ranking.append(performance.copy())
    lista_gols.clear()
    tot_gols = 0


    escolha = str(input('Cadastrar outro jogador? S/N: '))
    while escolha not in 'SsNn':
        escolha = str(input('Opção inválida, digite novamente: '))

    if escolha in 'Nn':
        break

#print(ranking) - PARA CONFERÊNCIA APENAS


# MINHA SOLUÇÃO PARA RANKING DOS JOGADORES

# Cabeçalho montado manualmente
print('-' * 55)
print('RANKING DOS JOGADORES'.center(55))
print('-' * 55)
print(f'{'|ID':<5}', f'{'|Nome':<10}', f'{'|Gols por Partida':<20}', f'{'|Saldo de Gols'}')
print('-' * 55)
# Primeiro tenho que entrar na lista chamada ranking, composta por dicionários, o tamanho
# dela é len(ranking).
# Depois tenho que entrar nos dicionários (que são as posições 0, 1, etc. da lista ranking)
# e vasculhar os campos que contém os dados pedidos pelas colunas da tabela.
for c in range(0, len(ranking)):
    print(f'|{c:^5}', end = '')
    print(f'|{ranking[c]['Nome']:<10}', end = '')
    # Tive que converter os itens abaixo do dicionário para str senão o alinhamento não
    # funcionaria.
    print(f'|{str(ranking[c]['Gols_por_partida']):^20}', end = '')
    print(f'|{str(ranking[c]['Saldo_de_gols']):^13}')
    print('-' * 55)



# SOLUÇÃO DO PROFESSOR PARA RANKING DOS JOGADORES

# A solução do professor foi muito interessante, pois não temos que mencionar os campos
# do dicionário durante o FOR, mas apenas coordenadas k (chave) e v (valor).
# Porém da forma como ele fez, trazemos todos os campos do dicionário para exibição, e no
# meu jeito de fazer, pude omitir a coluna de partidas disputadas, por exemplo. Mais manual,
# porém mais personalizável.
print('Solução do professor para ranking:')
# Primeiro um ID no cabeçalho, o qual não é um item de dicionário
print(f'{'ID':<5}', end = '')
# Depois as chaves do dicionário 'performance', que são as colunas do ranking
for i in performance.keys():
    print(f'{i:<25}', end = '')
print()
# Para começar o preenchimento, primeiro vasculhamos chave (k) e valor (v) da lista grande
# enumerada
for k, v in enumerate(ranking):
    # Para pegarmos os IDs dos jogadores imprimimos a chave (k)
    print(f'{k:<5}', end = '')
    # Em seguida, vasculhamos os valores (d) do item da lista em que o FOR estiver (v)
    for d in v.values():
        print(f'{str(d):<25}', end = '')
    print()

print('-' * 55)


# Mostrar gols por partida do jogador selecionado
while True:
    detalhes = int(input('Detalhar performance de qual jogador? (999 para encerrar): '))
    print('-' * 55)
    while detalhes not in range(0, len(ranking)) and detalhes != 999:
        detalhes = int(input('Opção inválida, digite novamente: '))
        print('-' * 55)
    if detalhes == 999:
        print('-- Programa Encerrado --')
        break



    # MINHA SOLUÇÃO PARA DETALHAMENTO POR JOGADOR

    # Quebrei muito a cabeça, e cheguei a essa conclusão: criar uma lista transitória fora
    # do dicionário com os gols por partida, para poder percorrê-la e mostrar os dados em
    # linhas separadas.
    transitoria = list()
    # Transferi para a lista somente os dados de gols por partida
    transitoria.append(ranking[detalhes]['Gols_por_partida'])

    # Criei um cabeçalho com o nome do jogador
    print(f'DESEMPENHO POR PARTIDA - {ranking[detalhes]['Nome'].upper()} '
          f'(DISPUTOU {ranking[detalhes]['Partidas_disputadas']} PARTIDAS)')
    print('-' * 55)

    # E percorri a largura do elemento 0 da lista transitória
    for c in range(0, len(transitoria[0])):
        print(f'{c + 1}a. partida: fez {transitoria[0][c]} gols')
    print('-' * 55)
    print(f'Total de gols marcados por {ranking[detalhes]['Nome'].upper()}: '
          f'{ranking[detalhes]['Saldo_de_gols']}')
    print('-' * 55)


    # SOLUÇÃO DO PROFESSOR PARA DETALHAMENTO POR JOGADOR

    # Replicando a aprendizagem da Aula19Desafio05 para vasculhar a lista de gols contida
    # no dicionário do jogador, que por sua vez estão ambos dentro de outra lista
    # Tentei sozinho e não consegui, daí acompanhei a correção e copiei o que o professor fez
    # A grande diferença foi que, ao invés de extrair os dados para uma lista transitória como
    # eu fiz, o professor acessou os dados diretamente.
    print('Replicando a solução aprendida no desafio 05:')
    # Vasculhamos chave (k) e valor (v) no item escolhido da lista, diretamente no campo
    # 'Gols_por_partida" do jogador mencionado em 'detalhes'
    for k, v in enumerate(ranking[detalhes]['Gols_por_partida']):
        print(f'{k + 1}a. partida: {v} gols')


    print('-' * 55)
    print('-- Fim do Programa --')







