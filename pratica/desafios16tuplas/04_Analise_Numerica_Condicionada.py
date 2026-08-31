# Desenvolver um programa que leia 4 valores pelo teclado e guarde-os numa tupla. No final,
# mostrar: 1- quantas vezes apareceu o número 9 2- em que posição foi digitado o número 3
# pela primeira vez 3- quais foram os números pares digitados. Programa a prova de usuário,
# ou seja, se os números 3 e 9 não forem digitados, um aviso especial.

v1 = int(input('Digite o 1o. número: '))
v2 = int(input('Digite o 2o. número: '))
v3 = int(input('Digite o 3o. número: '))
v4 = int(input('Digite o 4o. número: '))
tupla = (v1, v2, v3, v4)

# De novo, o professor ensinou um truque para que as quatro entradas alimentem a tupla direto,
# sem a etapa do de - para. Basicamente é preencher apenas uma variável, com 4 perguntas para
# o usuário.

#varprofessor = (int(input('Digite o 1o. número: ')), int(input('Digite o 2o. número: ')),
#                int(input('Digite o 3o. número: ')), int(input('Digite o 4o. número: ')))



print('-' * 30)
print(f'Você digitou os números {tupla}.')

if 9 in tupla:
    cont = tupla.count(9)
    print(f'O número 9 foi digitado {cont} vez(es).')
else:
    print('O número 9 não foi digitado.')

if 3 in tupla:
    tres = tupla.index(3) + 1
    print(f'O número 3 foi digitado pela 1a. vez na posição {tres}.')
else:
    print('O número 3 não foi digitado.')


print('Qual(is) número(s) par(es) foi(ram) digitado(s)?: ', end = '')
for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        print(tupla[c], end = '  ')
        c += 1
print()
print('-' * 30)
print('-- Fim --')



