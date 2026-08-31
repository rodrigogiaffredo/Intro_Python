# Fazer um programa que mostre na tela uma contagem regressiva para estouro de fogos de
# artifício. Indo de 10 até 0. Incluir uma pausa de 1 segundo entre cada número.

from time import sleep
print('A queima de fogos vai começar em...')
sleep(1)
for c in range (10, 0-1, -1):
    print(c)
    sleep(1)
print('Começoooooouuuu!!! Aeeeeeeeee!!!')
print('-- Fim --')
