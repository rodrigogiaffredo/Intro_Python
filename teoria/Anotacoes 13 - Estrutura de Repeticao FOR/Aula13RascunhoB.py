# Repetindo um print N vezes (lembrando que se quero repetir 5x, posso usar tanto o range
# (0, 5) quanto o range (1, 5 + 1) pois o primeiro número do range é onde ela se inicia,
# e o último é onde ela se encerra.

for c in range (0, 5):
    print('Hello, world!')
print('-- Fim --')
print()

# Sobre a importância da identação. Exatamente os mesmos comandos, porém com o print fim dentro
# do laço de repetição, resultado totalmente diferente.

for c in range (0, 5):
    print('Hello, world!')
    print('-- Fim --')
print()

# Se quiser imprimir o valor da variável de controle, simples também, lembrando que uso
# a letra 'c' porque é de contador (e counter), e a associação fica fácil, mas podia ser
# qualquer letra minúscula.

for c in range (1, 6):
    print (c)
print('-- Fim --')
print()

# Contagem regressiva tem um argumento a mais dentro dos parênteses do range, que é o
# passo negativo (X, Y, -1).

for c in range (5, 0, -1):
    print(c)
print('-- Fim --')
print()

# Este argumento a mais serve também para os pulos de casa na contagem, por exemplo, uma
# contagem progressiva de 2 em 2 será repersentada por (X, Y, 2).

for c in range (0, 11, 2):
    print(c)
print('-- Fim --')
print()

# O range também aceita definição de início e / ou limite através de variáveis com entrada
# dinâmica (atualizadas com input). No exemplo abaixo, o limite de repetições será definido
# pelo usuário (o +1 dará esse efeito para quem lê o output pois eu não quis começar no zero).

n = int(input('Digite um número: '))
for c in range (1, n+1):
    print(c)
print('-- Fim --')
print()

# Outro exemplo, delimitando ambas as coordenadas e os passos com dados inseridos pelo
# usuário ( o + 1 garante que inclusive a posição final seja impressa):

i = int(input('Digite a posição de início da contagem: '))
f = int(input('Digite a posição do fim da contagem: '))
p = int(input('Conto de quanto em quanto?: '))
for c in range (i, f + 1, p):
    print(c)
print('-- Fim --')
print()

# Outro exemplo legal, vou repetir a pergunta por um certo número de vezes.

for c in range (0, 3):
    n = input('Digite um valor: ')
print('-- Fim --')
print()

# Agora vamos somar os valores digitados a cada iteração, e mostrar o resultado da soma
# no final do programa.

s = 0
for c in range (0, 3):
    n = int(input('Digite um valor: '))
    # Outro jeito de escrever s = s + n é s += n (só serve para números, tem que tipificar
    # a variável com int.
    s += n
print(f'A soma dos números digitados é igual a {s}.')
print('-- Fim --')
print()
