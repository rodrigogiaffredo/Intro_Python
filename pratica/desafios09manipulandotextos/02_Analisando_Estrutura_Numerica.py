# Criar um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
# dígitos separados (fazer matematicamente e com strings para exercitar)
# Ex: se o número for 1834 o resultado final deve ser unidade: 4 dezena : 3,
# centena: 8, milhar: 1.


# Na hora da correção o professor mostrou que se o usuário digitar um número que não é
# milhar, a casa de milhar fica zero. Tive que pesquisar para chegar ao .zfill(4) que
# dita que o resultado do input str deve ter 4 caracteres, e se não tiver, preenche os
# faltantes com zero. Mas só fui para esse caminho depois de ver ele apresentando o
# resultado dele antes de começar a correção.

n = input(str('Digite um número de 0 a 9999: ')).zfill(4)
print()
print('Separando o número na lógica de string...')
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')

# Tem também o jeito matemático de fazer, que é pegando o número, dividindo por 1, 10,
# 100 e 1000, e aplicando os módulos de 10, pois os restos serão exatamente os números
# digitados nas respectivas casas de unidade, dezena, centena e milhar (versão professor):

num = int(n)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print()
print('Separando o número matematicamente...')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
