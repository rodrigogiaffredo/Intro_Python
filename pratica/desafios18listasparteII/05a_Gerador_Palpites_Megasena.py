# Fazer um programa que ajude um jogador da megasena a criar palpites. O programa vai
# perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta. Ou seja, cada palpite de 6 dezenas é um elemento
# de uma lista maior. Lembrando que os números não podem ser repetidos no mesmo jogo.

# Para geração de números aleatórios
import random

# Para o sleep entre sugestões
import time

# Variável transitória para armazenamento de dezena
dezena = 0

# Cada grupo de 6 dezenas
conjunto = list()

#Cada conjunto de 6 dezenas será um elemento de uma lista maior com 'n' elementos
listadejogos = list()

# Número de elementos que a lista maior conterá, definido pelo usuário como qtd. palpites
palpites = 0
# Para poder manter a contagem de palpites na hora de imprimir as sugestões
backuppalpites = 0


# Definindo a quantidade de palpites

print('-' * 35)
print('GERADOR DE PALPITES - MEGASENA'.center(35))
print('-' * 35)
palpites = int(input('Quantos palpites você quer gerar?: '))
backuppalpites = palpites


while palpites > 0:
    # Gerando 6 números para formar o primeiro palpite
    for c in range(0, 6):
        dezena = (random.randint(1, 60))
        # Garantindo que não haja repetições
        if dezena in conjunto:
            dezena = (random.randint(1, 60))
            conjunto.append(dezena)
        else:
            conjunto.append(dezena)
    # Guardando 6 dezenas como 1 elemento da lista maior
    listadejogos.append(sorted(conjunto))
    # Reduzindo o total de palpites disponíveis para loop
    palpites -= 1
    # Limpando a lista de dezenas para não poluir a próxima rodada
    conjunto.clear()


# Tenho que usar backuppalpites pois nos comandos anteriores a variável palpites foi zerada
for c in range(0, backuppalpites):
    print('-' * 35)
    print(f'Gerando {c + 1}o. palpite...')
    time.sleep(1)
    print(f'{listadejogos[c]}')
    time.sleep(1)

print('-' * 35)
print('BOA SORTE!'.center(35))
print('-' * 35)
