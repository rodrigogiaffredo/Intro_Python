# Criar um programa onde o usuário possa digitar sete valores numéricos e cadastra-los numa
# lista única que mantenha separados os valores pares e ímpares. No final mostrar os valores
# pares e ímpares em ordem crescente.

# NOTA: NAS ANOTAÇÕES DA AULA, INCLUÍ A RESPOSTA DO PROFESSOR, A QUAL PARTIU DE LISTAS
# ANINHADAS DESDE A DEFINIÇÃO DE VARIÁVEIS (NUMERO = [[], []]), SENDO A PRIMEIRA SUBLISTA
# PARA PARES, E A SEGUNDA PARA ÍMPARES (CÓDIGO BEM ELEGANTE).

# Lista transitória para uso durante o FOR
transitoria = list()
# Listas de pares e de ímpares
pares = list()
impares = list()
# Listona final
final = list()


# A listona conterá 2 outras listas, uma de números pares (elemento 0) em ordem crescente,
# outra de números ímpares (elemento 1) em ordem crescente.

for p in range(0, 7):
    transitoria.append(int(input(f'Digite o {p + 1}o. número: ')))
    if transitoria[0] % 2 == 0:
        pares.append(transitoria[0])
    else:
        impares.append(transitoria[0])
    transitoria.clear()

# Fiz uma graça e criei uma lista final com 2 elementos: o conjunto dos pares em ordem
# crescente, e o conjunto dos ímpares em ordem crescente.
final.append(sorted(pares[:]))
final.append(sorted(impares[:]))


print('-' * 40)
print(f'Os valores pares digitados foram: {final[0]}')
print(f'Os valores ímpares digitados foram: {final[1]}')
print(f'Lista final de pares e ímpares agrupados e em ordem crescente: {final}')









