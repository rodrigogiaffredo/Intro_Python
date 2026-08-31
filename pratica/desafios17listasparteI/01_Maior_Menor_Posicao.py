# Fazer um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostrar
# qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for c in range(1, 5+1):
    lista.append(int(input(f'Digite o {c}o. número: ')))
print('-' * 30)
print(f'Você digitou os números {lista}')


# Tive que correlacionar elemento (c) com item (v)
print(f'O maior valor digitado foi {max(lista)}, o qual apareceu na(s) posição(ões):', end = '')
for c, v in enumerate(lista):
    if v == max(lista):
        print(f' {c + 1} ', end = '')
print()

# Novamente, correlacionei elemento (c) com item (v)
print(f'O menor valor digitado foi {min(lista)}, o qual apareceu na(s) posição(ões):', end = '')
for c, v in enumerate(lista):
    if v == min(lista):
        print(f' {c + 1} ', end = '')
print()

print('-- Fim do Programa --')





#print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}.')



