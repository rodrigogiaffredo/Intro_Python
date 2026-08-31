# Criar um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar cadastrando. No final, mostrar: 1- qual o total gasto
# na compra 2 -quantos produtos custam mais de R$ 1.000,00 3- Qual é o nome do produto mais
# barato.

print('-' * 20)
print('ENCHA SEU CARRINHO')

totaldacompra = maisdemil = precomaisbarato = 0
nomemaisbarato = ()

print('-' * 20)
produto = str(input('Digite o nome do produto: ')).capitalize().strip()
preco = float(input(f'Digite o preço de {produto}: R$ '))
nomemaisbarato = produto
precomaisbarato = preco
totaldacompra += preco
if preco > 1000:
    maisdemil += 1

while True:

    print('-' * 20)
    decisao = str(input('Vai adicionar mais itens? [S/N]: ')).upper().strip()

    while decisao not in 'SN':
        decisao = str(input('Opção inválida, digite novamente: ')).upper().strip()

    if decisao == 'S':
        print('-' * 20)
        produto = str(input('Digite o nome do produto: ')).capitalize().strip()
        preco = float(input(f'Digite o preço de {produto}: R$ '))
        totaldacompra += preco
        if preco > 1000:
            maisdemil += 1
        if preco < precomaisbarato:
            nomemaisbarato = produto

    if decisao == 'N':
        break

print('-' * 20)
print(f'O total da compra ficou em R$ {totaldacompra:.2f}.')
print(f'Você comprou {maisdemil} produtos com preço acima de R$ 1.000,00.')
print(f'O produto mais barato que você comprou foi {nomemaisbarato}.')
