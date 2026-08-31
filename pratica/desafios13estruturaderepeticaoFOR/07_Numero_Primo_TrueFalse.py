# Fazer um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Número primo: divisível por 1 e por ele mesmo.

# Se o número for divisível por qualquer outro entre 2 e ele mesmo, não é primo.

# Vamos contar quantas vezes (V) o número é divisível por outro além de 1 e ele mesmo

m = 0 # quantidade de múltiplos do número digitado (primos só podem ter 2 -> 1 e eles mesmos).
n = int(input('Digite um número e eu te digo se ele é primo: '))

for c in range(1, n+1):
    if n % c == 0:
        m += 1

# O número 1, apesar de logicamente divisível por 1 e por ele mesmo, não é primo pois não
# tem 2 múltiplos entre 1 e ele mesmo, sendo assim tratamos como exceção.
if n == 1:
    print('Apesar de ser divisível por 1 e por ele mesmo, excepcionalmente o número 1 NÃO É primo.')

# Tirando o número 1, todos os outros números primos só possuem 2 múltiplos: 1 e eles mesmos.
elif m != 2:
    # O -2 do primeiro print se deve ao 1 e ao próprio número que devem ser subtraídos do
    # total de múltiplos para sabermos apenas a diferença, que é o que eu quis mostrar.
    print(f'O número {n} tem {m - 2} outro(s) múltiplo(s) além de 1 e dele mesmo, portanto NÃO é primo.')
    print(f'Outro(s) múltiplo(s) de {n}: ', end = ' ')

    # Range de 2 a n pois desconsideramos 1 e ele mesmo para fazer essa lista, quero mostrar
    # apenas os demais números além do 1 e dele mesmo.
    for c in range(2, n):
        if n % c == 0:
            print(f'{c}', end = ', ')

else:
    print(f'O número {n} só é divisível por 1 e por ele mesmo, portanto É primo.')


