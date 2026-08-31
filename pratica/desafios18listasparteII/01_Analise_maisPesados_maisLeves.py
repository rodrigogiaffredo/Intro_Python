# Fazer um programa que leia o nome e o peso de várias pessoas guardando tudo em uma lista,
# mostrando no final: 1- quantas pessoas foram cadastradas 2- uma listagem com as pessoas
# mais pesadas 3- uma listagem com as pessoas mais leves.


# Lista oficial
cadastro = list()
# Lista transitória para agrupar nome e peso num elemento só
pessoasnovas = list()
# Listas para pesados e leves
pesados = list()
leves = list()


# Entrada de dados
while True:
    pessoasnovas.append(str(input('Nome: ')))
    pessoasnovas.append(float(input('Peso: ')))
    # Trasição do dado entre listas
    cadastro.append(pessoasnovas[:])
    pessoasnovas.clear()

    # Blindagem contra erro do usuário
    escolha = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while True:
        if escolha not in 'SN':
            escolha = str(input('Opção inválida, digite novamente: ')).upper().strip()
        else:
            break

    # Fim do loop de cadastramento
    if escolha == 'N':
        break

# Para checagem
#print(cadastro)



# Medição do peso
maior = menor = 0
for p in range(0, len(cadastro)):
    if p == 0:
        maior = menor = cadastro[p][1]
    else:
        if cadastro[p][1] > maior:
            maior = cadastro[p][1]
        elif cadastro[p][1] < menor:
            menor = cadastro[p][1]



# Montagem da lista dos pesados
for p in range (0, len(cadastro)):
    if cadastro[p][1] == maior:
        pesados.append(cadastro[p])

# Para checagem
#print(pesados)

# Montagem da lista dos leves
for p in range (0, len(cadastro)):
    if cadastro[p][1] == menor:
        leves.append(cadastro[p])

# Para checagem
#print(leves)


# Análises

print('-' * 50)

# Quantidade de pessoas cadastradas
print(f'Foram cadastradas {len(cadastro)} pessoas.')

# Maior peso
print(f'Pessoas mais pesadas ({maior}kg):', end = '   ')
for p in range(0, len(pesados)):
    print(f'{pesados[p][0]}', end = '   ')
print()

#Menor peso
print(f'Pessoas mais leves ({menor}kg):', end = '   ')
for p in range(0, len(leves)):
    print(f'{leves[p][0]}', end = '   ')
print()



print('-- Fim do Programa--')
