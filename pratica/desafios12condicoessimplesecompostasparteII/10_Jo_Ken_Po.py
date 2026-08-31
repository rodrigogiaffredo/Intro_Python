# Criar um programa que faça o computador jogar pedra / papel / tesoura comigo. Nota
# minha: as condições surgem das possíveis combinações de golpes (papel ganha de pedra,
# perde de tesoura, etc.). Eu digito o que escolhi, o computador me diz o que escolheu,
# o programa mostra quem ganhou ou se teve empate.

# Para deixar a prova de usuário, tenho que criar a escolha inválida, tinha esquecido e
# lembrei durante a correção. Tive que identar o miolo para pular para o fim de jogo após
# a escolha de uma opção errada, essa sacada eu tive.

# Daí ele meteu o macetinho do JO KEN PÔ com sleep e eu não aguentei e imitei kkkkk.

import random
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
random.choice(lista)
computador = random.choice(lista)


escolha = str(input('HORA DE JOGAR JOKENPÔ!\nVocê escolhe pedra, papel ou tesoura?: ').strip().title())
if escolha != 'Pedra' and escolha != 'Papel' and escolha != 'Tesoura':
    print('Opção inválida!')
else:
    print('JÔ')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print(f'Eu escolhi {computador}.')

    if computador == 'Pedra' and escolha == 'Papel':
        print('Você ganhou!')
    elif computador == 'Papel' and escolha == 'Tesoura':
        print('Você ganhou!')
    elif computador == 'Tesoura' and escolha == 'Pedra':
        print('Você ganhou!')
    elif computador == escolha:
        print('Deu empate!')
    else:
        print('Eu ganhei!')

print('-- Fim de jogo --')
