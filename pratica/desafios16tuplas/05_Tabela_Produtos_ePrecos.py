# Criar um programa que tenha uma tupla única com nomes de produtos e seus respectivos
# preços em sequência. Mostrar uma listagem de preços organizando os dados em forma tabular.
# Listagem decorada, alinhada, preços com R$ e duas casas decimais, pontos entre o nome do
# produto e o preço, tabelinha maneira mesmo.

cardapio = ('Pão', 2, 'Leite', 4.5, 'Manteiga', 11, 'Presunto', 15, 'Queijo', 10, 'Café', 5.5)
organizado = cardapio

print('=' * 40)
# Esse center para centralizado foi sugestão autocomplete do PyCharm, e eu aderi porque o
# acento ^ simplesmente não funciona ahahahahah.
print('TABELA DE PREÇOS - PADARIA'.center(40))
print('=' * 40)

c = 0
while c < len(organizado):
    # A minha sacada foi usar os pares como gatilho, e pular de 2 em 2. Exatamente o que o
    # professor mostrou na correção.
    if c % 2 == 0:
        print(f'{organizado[c]:.<31} R$ {organizado[c + 1]:>5.2f}')
        c += 2 # Artifício para pular de 2 em 2.
print('-' * 40)



