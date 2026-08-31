# Escrever um programa que faça o computador "pensar" um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Tem um lance legal que o professor fez que foi simular o computador pensando antes de
# responder, ele importou o módulo 'time' e usou o comando 'sleep'

from time import sleep
import random

segredo = random.randint(0,5)
escolha = int(input('Tente adivinhar o número de 0 a 5 no qual eu estou pensando: '))
# Daí aqui eu dei o miguézinho de esperar 3 segundos
print(f'Processando...')
sleep(2)
print(f'Escolhi {segredo}, o fiadamãe acertou!' if escolha == segredo else f'Escolhi {segredo}, errou ahahahah')
print('--FIM--')
