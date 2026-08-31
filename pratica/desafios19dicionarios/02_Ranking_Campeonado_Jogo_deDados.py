# Criar um programa onde 4 jogadores joguem um dado (números de 1 a 6) e tenham resultados
# aleatórios. Guardar os resultados num dicionário. No final, colocar o dicionário em ordem
# crescente, e revelar o vencedor, que é quem escolheu o maior número no dado. O dicionário
# tem 4 itens, cada um contendo um nome fictício e o número que o jogador tirou.


# Assisti novamente a resolução do exercício 80 da playlist, que trata de
# listas ordenadas sem uso de sort e peguei insights, sem isso não estava conseguindo.


import random
from time import sleep

ranking = list()

print('-' * 40)
print('PREPAREM-SE PARA LANÇAR OS DADOS'.center(40))
sleep(1)
print('VALENDO!'.center(40))
print('-' * 40)

# Randomização dos palpites e criação dos dicionários via loop finito
for c in range(1, 4 + 1):
    jogadas = {'nome':f'Jogador {c}', 'dado':random.randint(1, 6)}
    sleep(1)
    print(f'Jogador {c} tirou {jogadas['dado']}')
    # Posicionamento de final de lista (ou o primeiro lance, ou lance maior que o último)
    if c == 1 or jogadas['dado'] > ranking[-1]['dado']:
        ranking.append(jogadas.copy())
    else:
        # Contador da verificação
        posicao = 0
        # Comparando novas jogadas com cada item já presente na lista
        while posicao < len(ranking):
            # Sempre que for menor ou igual ao verificado, toma o lugar dele
            if jogadas['dado'] <= ranking[posicao]['dado']:
                ranking.insert(posicao, jogadas.copy())
                # Assim que o número é inserido definitivamente, interrompe a checagem
                break
            posicao += 1


sleep(1)
print('-' * 40)
print('RESULTADO DA RODADA'.center(40))
print('-' * 40)

# Colocando o ranking em ordem decrescente para a classificação final fazer sentido
# O professor não explicou em aula, tive que pesquisar
ranking.reverse()

cont = 1
for c, v in enumerate(ranking):
    sleep(1)
    print(f'{cont}o. colocado: {v['nome']} com {v['dado']} pontos.')
    cont += 1
print('-' * 40)


print('-- FIM DE JOGO --'.center(40))

print()
print('A solução do professor envolve colocar o dicionário em ordem decrescente:')
print('Obs.: eu coloquei os resultados numa lista e usei reverse para a ordenação.')
print()

# Criação do dicionário para guardar os resultados dos 4 jogadores:
jogo = {'Jogador1':random.randint(1, 6),
        'Jogador2':random.randint(1, 6),
        'Jogador3':random.randint(1, 6),
        'Jogador4':random.randint(1, 6)}
# Para conferência
#print(jogo)

# Para colocar os itens em ordem decrescente, tenho que criar um novo dicionário
final = dict()
# E temos que importar o módulo operator, para usar a função itemgetter
from operator import itemgetter

print('Valores sorteados:')
# Varremos o dicionário com um FOR de itens que traga chave e valor
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    # Aquele draminha com espera de 1 segundo
    sleep(1)

# Para colocar o dicionário em ordem decrescente, criamos um novo, o qual será preenchido
# com uma varredura do primeiro dicionário criado após as jogadas do dado, usando a função
# itemgetter associada ao v do FOR que é o valor tirado no dado (por isso o 1 entre
# parênteses, se fosse ordenar por jogador pegaria o 0 que equivale ao k)
# Isso não foi ensinado em aula, somente na correção do exercício.

final = sorted(jogo.items(), key = itemgetter(1))

# Para conferência, ainda sem ordenar de forma decrescente
#print(final)

# Mas para ficar com aparência de ranking (do primeiro para o último), precisamos usar um
# outro argumento aprendido na aula de tuplas, que é o reverse = True, resultando em:

final = sorted(jogo.items(), key = itemgetter(1), reverse = True)

# Para conferência, antes de usar o FOR e deixar esteticamente melhor
#print(final)
# Note que o resultado será uma lista, contendo 4 tuplas (comentário meu: as listas são
# espetaculares).

# Agora sim podemos partir para o FOR que construirá o ranking, a partir do novo dicionário
# chamado 'final'. E como o resultado final é uma lista com tuplas, podemos usar o enumerate
# e facilitar o processo de exibição dos dados com estética versátil.

# Finalmente, o FOR com chave e valor, lembrando que traremos os 2 valores contidos
# nas tuplas: tanto o nome do jogador [0], quanto o número que ele tirou no dado [1].
print('-' * 40)
for k, v in enumerate(final):
    print(f'{k + 1}o. colocado: {v[0]} com {v[1]} pontos.')
    sleep(1)










