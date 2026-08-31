# Criar um programa onde o usuário digite uma expressão matemática qualquer que use
# parênteses. O programa deverá analisar se a expressão está com os parênteses abertos e
# fechados na ordem certa. Ou seja, para cada parêntese aberto, tem que ter um fechado, e
# na posição certa. Já pensando aqui, cada item da expressão pode ser um item de lista.
# Tanto se usar parênteses a mais, quanto a menos, quanto abrir sem fechar e fechar sem
# abrir, enfim, qualquer erro deve resultar no status Expressão invalida. Senão Expressão
# valida.


# Entrada e quebra da expressão, montagem de lista só com parênteses, e contagem de
# parênteses abertos e fechados.

expressao = str(input('Digite uma expressão com parênteses: ')).strip()
quebrada = list(expressao)
parenteses = []
par_aberto = 0
par_fechado = 0


# Montando lista só com parênteses na ordem de ocorrência, e contando separadamente
# parênteses abertos e fechados

for c in range(0, len(quebrada)):
    if '(' in quebrada[c]:
        parenteses.append(quebrada[c])
        par_aberto += 1
    if ')' in quebrada[c]:
        parenteses.append(quebrada[c])
        par_fechado += 1

# Verificando se a expressão contém parênteses, e se sim, verificando se o primeiro
# parêntese é aberto, e se o número de abertos é igual ao de fechados. Qualquer coisa
# diferente disso torna a expressão inválida.

if parenteses == []:
    print('Expressão inválida.')
else:
    if '(' not in parenteses[0]:
        print('Expressão inválida.')

    elif par_aberto != par_fechado:
        print('Expressão inválida.')

    else:
        print('Expressão válida.')

print('-- Fim do programa --')
print('-' * 40)


# Validação visual durante a escrita do código
#print(expressao)
#print(quebrada)
#print(parenteses)
#print(par_aberto)
#print(par_fechado)











