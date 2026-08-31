# Criar um programa onde o usuário possa digitar 5 valores numéricos e cadastra-los numa
# lista porém já na posição correta de uma ordem crescente, sem usar o sort depois que a
# lista estiver pronta. No final, mostrar a lista em ordem crescente gerada sem o uso do
# sort. A cada número adicionado, digo onde ele foi inserido: último elemento da lista
# (o primeiro número e os maiores números digitados a partir do segundo) ou elemento x da
# lista (todos os outros de acordo com o ELEMENTO que eles assumirem), daí sim imprime
# a lista final.

print()
print('SOLUÇÃO DO PROFESSOR')
print()

lista = list()

for c in range(0, 5):
    n = int(input('Digite um número: '))
    # Após digitado, o valor tem 3 possibilidades de inserção na lista: ou ele é o primeiro,
    # ou ele é o último, ou ele está no meio.
    if c == 0 or n > lista[-1]: # Se ele for o primeiro ou se for maior que o último número
        lista.append(n)
        print('Número adicionado no final da lista.')
    else:
        posicao = 0
        while posicao < len(lista): # Precisamos varrer o vetor (lista) inteiro
            if n <= lista[posicao]: # Se o novo valor é menor ou igual ao valor varrido na lista
                lista.insert(posicao, n) # Ele o substitui em sua posição
                print(f'Número adicionado na posição {posicao} da lista.')
                break # Quebro, pois após inserido, o número não precisa mais ser verificado
            posicao += 1
print('-' * 30)
print(f'Valores digitados (organizados em ordem crescente): {lista}')









# O código abaixo é a gambiarra que eu fiz para solucionar o problema. Funcionou, mas atrasou
# minha aprendizagem num tema muito importante: aninhamento de estruturas de repetição com
# índice, valor e enumerate. Durante a aula 19 o prejuízo estava tão grande, que tive que
# voltar à aula 17 e recapitular, inclusive este exercício.


#lista = []

# Primeiro número

#num = int(input('Digite o 1o. número: '))
#lista.append(num)
#print('Número inserido na última posição.')

# Segundo número

#num = int(input('Digite o 2o. número: '))
#if num < lista[0]:
#    lista.insert(0, num)
#    print('Número inserido na posição zero.')
#else:
#    lista.append(num)
#    print('Numero inserido na posição um.')


# Terceiro número

#num = int(input('Digite o 3o. número: '))
#if num < lista[0]:
#    lista.insert(0, num)
#    print('Número inserido na posição zero.')
#elif num > lista[-1]:
#    lista.append(num)
#    print('Número inserido na posição 2.')
#else:
#    lista.insert(1, num)
#    print('Número inserido na posição 1.')

# Quarto número

#num = int(input('Digite o 4o. número: '))
#if num < lista[0]:
#    lista.insert(0, num)
#    print('Número inserido na posição zero.')
#elif num > lista[-1]:
#    lista.append(num)
#    print('Número inserido na posição 3.')
#elif num > lista[0] and num < lista[1]:
#    lista.insert(1, num)
#    print('Número inserido na posição 1.')
#elif num > lista[1] and num < lista[2]:
#    lista.insert(2, num)
#    print('Número inserido na posição 2.')

# Quinto número

#num = int(input('Digite o 5o. número: '))
#if num < lista[0]:
#    lista.insert(0, num)
#    print('Numero inserido na posição zero.')
#elif num > lista[-1]:
#    lista.append(num)
#    print('Número inserido na posição 4.')
#elif num > lista[0] and num < lista[1]:
#    lista.insert(1, num)
#    print('Número inserido na posição 1.')
#elif num > lista[1] and num < lista[2]:
#    lista.insert(2, num)
#    print('Número inserido na posição 2.')
#elif num > lista[2] and num < lista[3]:
#    lista.insert(3, num)
#    print('Número inserido na posição 3.')


#print('-' * 30)
#print(f'Lista final: {lista}.')
#print('-' * 30)
#print ('-- Fim do Programa--'.center(30))
