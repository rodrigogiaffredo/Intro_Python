# Listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura
# os quais são acessíveis por chaves individuais.

# Ao contrário das tuplas, as listas são variáveis compostas MUTÁVEIS, e são caracterizadas
# pelo uso de colchetes [].

print('Lista original')
num = [2, 5, 9, 1]
print(num)

print('Substituindo o elemento 2')
num[2] = 3
print(num)

print('Adicionando valor ao final')
num.append(7)
print(num)

print('Ordenando de forma crescente')
num.sort()
print(num)

print('Ordenando de forma decrescente')
num.sort(reverse=True)
print(num)

print(f'Quantidade de elementos da lista: {len(num)}.')

print('Adicionando item definindo seu elemento')
num.insert(2, 0)
print(num)

print('Removendo o último ELEMENTO da lista')
num.pop()
print(num)

print('Removendo ELEMENTO específico')
num.pop(2)
print(num)

print('Inserindo ITEM em ELEMENTO específico')
num.insert(2, 2)
#           elemento    item
print(num)

print('Removendo ITEM específico')
num.remove(2)
print(num)

print('Se o ITEM existir, remova')
if 4 in num:
    num.remove(4)
else:
    print('ITEM não encontrado.')
print()
print()

print('Criando nova lista usando append')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

print('Imprimindo ITEM com estilo e formatação diferenciada')
for v in valores:
    print(f'Item {v}')

print('Imprimindo ITEM e ELEMENTO')
for c, v in enumerate(valores):
    print(f'Item {v} é o elemento {c}')

print('Lendo valores pelo teclado e criando lista')
novosvalores = []
for cont in range(1, 5+1):
    novosvalores.append(int(input(f'Digite o {cont}o. valor: ')))
print(novosvalores)

print('Ligação entre listas (confunde porque parece que criou uma lista nova)')
a = [2, 3, 4, 7]
b = a
print(a)
print(b)
b[2] = 8 # Não vai mudar apenas a lista b, mas ambas, porque estão ligadas.
print(a)
print(b)

print('Criando cópia de uma lista')
a = [2, 3, 4, 7]
b = a[:]
print(a)
print(b)
b[2] = 8 # Agora sim mudou apenas a lista b
print(a)
print(b)

