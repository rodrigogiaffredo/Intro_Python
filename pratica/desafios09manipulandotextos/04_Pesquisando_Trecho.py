# Criar um programa que leia o nome de uma pessoa e diga se ela tem "Silva" em
# qualquer lugar do nome.

nome = str(input('Digite seu nome completo: ')).strip()

# Aprendi no exercício anterior a deixar o programa a prova de usuário, ou seja, não importa
# como ele digite o nome, eu normalizo para formato título e só depois aplico a busca.
nomeajust = nome.title()

print(f'O nome digitado contém o sobrenome Silva?: {'Silva' in nomeajust}')
# Como o in é um operador (e não um method) eu consigo associar ele a uma string.
print(f'Jeito do professor - tem Silva?: {'Silva' in nome.title()}')
