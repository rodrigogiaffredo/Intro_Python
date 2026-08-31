# Arquivo 'Numeros' da aula de modularização

#def fatorial(n):
#    f = 1
#    for c in range(1, n+1):
#        f *= c
#    return f

#def dobro(n):
#    return n * 2

#def triplo(n):
#    return n * 3

# Programa principal

#import uteis22   # --> 'uteis22' é o MÓDULO que criei, com as
                  #      funções fatorial, dobro, triplo

from muitouteis22 import numbers22  # --> 'muitouteis22' é o PACOTE que criei para estudo
                                    #      o qual contém o MÓDULO numbers22 onde passei a
                                    #      hospedar as funções fatorial, dobro e triplo


# Note que seria possível importar só uma função, por exemplo from uteis22 import fatorial
# ou 2 das 3 funções usando from uteis22 import fatorial, triplo
# Mas a recomendação dos criadores do Python é, no caso de módulos que eu mesmo criei,
# importar sempre o módulo inteiro, pois eventualmente posso ter criado por exemplo outra
# função chamada 'triplo' em outro módulo, pode haver conflito e erro no programa.

num = int(input('Digite um valor: '))
fat = numbers22.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numbers22.dobro(num)}.')
print(f'O triplo de {num} é {numbers22.triplo(num)}.')

# Note que criamos 3 funções num mesmo arquivo.

# Para fins de aprendizagem, vou criar um arquivo chamado uteis22.py e transferir
# todas as funções para lá.

# O código resultante que ficará no arquivo numeros22.py ficou bem menor.

# O arquivo uteis22.py é exatamente um MÓDULO.

# E para fazer as funções voltarem a funcionar dentro desse arquivo com o código principal,
# basta usar o já conhecido 'import' (ver linha 16).
