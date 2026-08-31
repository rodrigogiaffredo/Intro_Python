# Desenvolver um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostrar: a média de idade do grupo; o nome do homem mais velho; quantas mulheres tem menos
# de 20 anos.

idades = 0 # Soma das idades para cálculo da média
ihmv = 0 # Idade do homem mais velho
nhmv = () # Nome do homem mais velho
mmv = 0 # Contagem de mulheres com menos de 20 anos

for c in range(1, 4+1):

    print(f'Dados da {c}a. pessoa')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).strip().upper()

    idades += idade

    if sexo == 'M' and idade > ihmv:
        ihmv = idade
        nhmv = nome

    if sexo == 'F' and idade < 20:
        mmv += 1

print(f'A média de idade do grupo é de {(idades / 4):.1f} anos.')
print(f'O nome do homem mais velho é {nhmv} e ele tem {ihmv} anos.')
print(f'A lista contém {mmv} mulher(es) com menos de 20 anos.')
print()
print('-- Fim --')
