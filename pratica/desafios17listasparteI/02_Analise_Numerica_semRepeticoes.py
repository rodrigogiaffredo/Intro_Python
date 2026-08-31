# Criar um programa onde o usuário possa digitar vários valores numéricos e cadastrar
# numa lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
# exibir todos os valores únicos digitados em ordem crescente. A cada valor digitado,
# dizer que foi adicionado com sucesso e perguntar se quer continuar. Se digitar um
# valor que já existe, mandar o aviso 'Valor duplicado, digite outro número'. Quando
# for escolhida a opção NAO, mostrar 'Você digitou os valores [ tal tal tal] mas em ordem
# crescente e não na ordem digitada.

print('-' * 30)
print('CADASTRO DE VALORES ÚNICOS'.center(30))
print('-' * 30)



lista = []
num = ()


# Entrada de número validando repetição
while True:
    num = (int(input('Digite um valor: ')))

    while num in lista:
        num = (int(input('Número repetido, digite outro: ')))

    lista.append(num)
    # Peguei esse print na resposta do professor.
    print('Valor adicionado.')

# Escolha por continuar ou encerrar o programa à prova de usuário
    opcao = str(input('Quer digitar outro valor? S/N: ')).upper().strip()
    while opcao not in 'SN':
        opcao = str(input('Opção inválida, digite novamente: ')).upper().strip()

    if opcao == 'N':
        break

# Impressão da lista em ordem crescente
print(f'Você digitou os valores {sorted(lista)}.')
