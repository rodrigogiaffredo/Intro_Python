# Nas entrelinhas o professor disse para nos acostumarmos com a expressão:
# OBJETO.COMANDO() - no exemplo dele era carro.siga(), carro.direita(), etc.
# Anotando para reforço de memória.

# Estruturas condicionais: identadas através da tecla TAB

# Sintaxe genérica                      Sintaxe Python (não esquece os dois pontos)

# se objeto.comando()                   if objeto.comando():
#   bloco_verdadeiro_                       bloco True
# senão                                 else:
#   bloco_falso_                            bloco False


# Exemplo para fixação: dizer se um carro é novo ou velho com base no ano de fabricação.

tempo = int(input('Quantos anos tem seu carro?: '))
if tempo <= 3:
    print('Aê leke, olha a nave zéra do maluko!')
else:
    print('Sai pra lá com essa bagaçêra maluko!')
print('--FIM--')


# Todoh comando fora da identação será executado sempre (tempo, if, else, print FIM)
# Já os comandos identados só serão executados de acordo com a escolha ou condição.

