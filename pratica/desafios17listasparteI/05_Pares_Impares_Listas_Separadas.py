# Criar um programa que leia vários números (ate o usuario parar) e coloque numa lista.
# Em seguida criar duas listas extras contendo apenas os valores pares numa, e apenas os
# impares na outra. No final, mostrar o conteudo das 3 listas geradas. Proposta do exercício
# é no primeiro loop montar a lista. E so depois fazer as analises. Não emendar direto a
# inserção dos valores nas listas de cara assim que digitar. O proposito é treinar análise.

lista = []
par = []
impar = []

# Entrada de valores à prova de usuário

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opcao = str(input('Quer digitar outro número? S/N: ')).upper().strip()
    while opcao not in 'SN':
        opcao = str(input('Opção inválida, digite novamente: ')).upper().strip()
    if opcao == 'N':
        break

print('-' * 40)
print(f'Lista de números digitados: {lista}')

# Vasculhar a lista usando um for len(lista)
# Se o número for par, par.append
# Se for ímpar, impar.append

for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])


print(f'Lista de números pares digitados: {par}')
print(f'Lista de números ímpares digitados: {impar}')

print('-' * 40)
print('-- Fim do Programa --')
