# Melhorar o jogo onde o computador pensa um número de 0 a 10 (aula 10 desafio 01). Mas
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
# Enunciado do desafio 01 da aula 10: Escrever um programa que faça o computador "pensar" um
# número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
comput = random.randint(0, 10)
print(comput)
tentativas = 1

print()
print('''Olá, sou seu computador.
Acabei de pensar um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

jogador = int(input('Digite seu palpite: '))

while comput != jogador:
    tentativas += 1

# Professor mostrou na resolução esse lance de maior ou menor, gostei e fiz antes dele.
    if jogador > comput:
        jogador = int(input('É menor que esse, escolhe outro: '))
    if jogador < comput:
        jogador = int(input('É maior que esse, escolhe outro: '))

if tentativas == 1:
    print('Acertou de primeira, parabéns!')
else:
    print(f'Acertou em {tentativas} tentativa(s), mandou bem!')

print('-- Fim --')
