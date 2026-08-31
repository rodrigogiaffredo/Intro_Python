# Criar um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
# cada pessoa num dicionário e todos os dicionários em uma lista. No final, mostrar:
# 1- quantas pessoas foram cadastradas 2- a média de idade do grupo 3- uma lista de todas
# as mulheres 4- uma lista com todas as pessoas com idade acima da média.

# O dicionário 'ficha' conterá listas
ficha = dict()
# Listas contidas no dicionário
mulheres = list() # Mais adiante o professor revelou uma forma de não ter que usar essa lista
cadastro = list()
# Variáveis para cálculo da média de idade
tot_pessoas = 0
soma_idade = 0


print('-' * 35)
print('FICHA DE CADASTRO'.center(35))
print('-' * 35)

# Entrada de dados com nome, sexo e idade
while True:
    ficha['Nome'] = str(input('Nome: ')).capitalize().strip()
    ficha['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()

    while ficha['Sexo'] not in 'MmFf':
        ficha['Sexo'] = str(input('Opção inválida, digite novamente: ')).upper().strip()
    # Adição das mulheres na lista 'mulheres'
    if ficha['Sexo'] in 'Ff':
        mulheres.append(ficha['Nome'])

    ficha['Idade'] = int(input('Idade: '))
    soma_idade += ficha['Idade']
    print(f'{ficha['Nome']} cadastrado com sucesso.')

    # Totalização de pessoas - o professor revelou mais a frente um modo de não precisar dela
    tot_pessoas += 1
    # Adição dos dicionários à lista de cadastro
    cadastro.append(ficha.copy())

    # Continuação ou não do cadastramento
    continuar = str(input(f'Deseja continuar [S/N]?: ')).upper().strip()
    while continuar not in 'SsNn':
        continuar = str(input('Opção inválida, digite novamente: '))
    if continuar in 'Nn':
        break

print()

# Cálculo da média de idade após cadastro finalizado, e criação da lista das pessoas com
# idade acima da média
# Mais abaixo o professor sugeriu outro modo de calcular a média, gostei bastante
media_idade = soma_idade / tot_pessoas
# Inclusive abolindo a necessidade dessa lista com idades acima da media
acima_media = list()

# Atualização da lista de pessoas com idade acima da média (desnecessário, o professor revelou
# um jeito muito interessante mais adiante
for k, v in enumerate(cadastro):
    if v['Idade'] >= media_idade:
        acima_media.append(cadastro[k])

# Início da análise dos dados da base de cadastros
print('-' * 35)
print('ANÁLISE DO CADASTRO'.center(35))
print('-' * 35)

# Total de pessoas cadastradas (será a quantidade de dicionários contidos na lista 'cadastro')
print(f'O cadastro contém os dados de {len(cadastro)} pessoas.')
# Média de idade das pessoas cadastradas (soma das idades dividida pela quantidade de dicionários
# da lista 'cadastro'
print(f'A média de idade das pessoas cadastradas é de {(soma_idade/len(cadastro)):.2f} anos.')


# MINHA SOLUÇÃO
# Mulheres cadastradas, varrendo chaves e valores, e retornando apenas valores da
# lista 'mulheres'
print(f'As mulheres cadastradas até agora foram:', end = ' ')
for k, v in enumerate(mulheres):
    print(f' {v}', end = '  ')
print()

# SOLUÇÃO DO PROFESSOR (TREINA MAIS O LANCE DE VASCULHAR CAMPOS DE DICIONÁRIOS EM LISTAS)
# O professor usou uma solução bastante interessante e prática para imprimir as mulheres
# sem ter que criar outra lista
print('-' * 35)
print('Solução do professor para imprimir os nomes das mulheres:')
# Ele vasculhou a lista 'cadastro' a qual conté os dicionários, em busca dos itens 'F':
for c in cadastro:
    if c['Sexo'] == 'F':
        print(f'{c['Nome']}', end = '  ')
print()
print('-' * 35)


# MINHA SOLUÇÃO
# Pessoas com idade acima da média, varrendo chaves e valores, e retornando apenas valores
# da lista 'acima_media', especificamente dos itens nome e idade dos dicionários contidos
# na lista
print('Pessoas com idade acima da média:')
for k, v in enumerate(acima_media):
    print(f'- {v['Nome']} (sexo {v['Sexo']}), com {v['Idade']} anos')


# TREINEI A SOLUÇÃO QUE O PROFESSOR PASSOU ANTERIORMENTE, E CONSEGUI FAZER
# Replicando a ideia que o professor usou para encontrar as mulheres cadastradas, agora
# para as pessoas com idade acima da média
print('-' * 35)
print('Replicando a solução do professor, agora para idades acima da média:')
for c in cadastro:
    if c['Idade'] > (soma_idade / len(cadastro)):
        print(f'- {c['Nome']} (sexo {c['Sexo']}), com {c['Idade']} anos')
print()

# Fim do programa
print('-' * 35)
print('-- Fim do Programa --'.center(35))



#print(cadastro) # Para conferência
#print(mulheres) # Para conferência
#print(media_idade) # Para conferência
#print(acima_media) # Para conferência
#print()







