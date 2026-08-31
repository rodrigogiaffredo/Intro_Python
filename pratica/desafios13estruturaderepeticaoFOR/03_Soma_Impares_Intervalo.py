# Fazer um programa que calcule a soma entre todos os números ímpares que são múltiplos
# de 3 e que se encontram no intervalo de 1 até 500 (não queremos saber quais são, queremos
# só o resultado da soma).

soma = 0
cont = 0

for c in range(1, 500 + 1):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        cont += 1
print()
print(f'A soma dos {cont} números ímpares e múltiplos de 3, que estão entre 1 e 500, é igual a {soma}.')
print()

# Imprimindo a lista só de marra, e para testar também o modo com economia de processador
# que aprendi no desafio anterior (resolvendo a questão do ímpar no próprio range, começando
# no 1 e pulando de 2 em 2.)

print('São eles: ', end = '')
for c in range(1, 500 + 1, 2): # usando a economia de processador do desafio anterior
    if c % 3 == 0:
        print(f'{c}', end = ' ')
print()
print()
print('-- Fim --')
