# Fazer um programa que tenha uma função chamada contador(), que receba 3 parâmetros:
# início, fim e passo e realize a contagem. O programa tem que realizar 3 contagens através
# da função criada: 1- de 1 a 10 (1em1) 2- 10 a zero (2em2) 3- uma contagem personalizada
# pelo usuário.

from time import sleep

def contador(i, f, p):
    print('-' * 45)
    print(f'Contagem de {i} a {f} de {p} em {p} iniciada...')
    print('-' * 45)
    sleep(2.5)
    if p == 0:
        p = 1
    if i <= f:
        for c in range(i, f + 1, abs(p)):
            sleep(0.3)
            print(f'{c}', end = ' ')
    else:
        for c in range(i, f - 1, -abs(p)):
            sleep(0.3)
            print(f'{c}', end = ' ')
    print()

# Programa principal
contador(0, 10, 1)
contador(10, 0, -2)

print('-' * 45)
print('Sua vez de personalizar a contagem!')
inicio = int(input('Digite o primeiro número: '))
fim = int(input('Digite o último número: '))
passo = int(input('Quer que eu conte de quanto em quanto?: '))
contador(inicio, fim, passo)
