# Refazer o desafio 10 da aula 8 (desafio dos triângulos), daí se for possível formar
# um triângulo, acrescentar o recurso de mostrar que tipo de triângulo será formado:
# equilátero (todos os lados iguais), isósceles (dois lados iguais), escaleno (todos os
# lados diferentes).

# # Lembrando o Desafio 10 da aula 8:
# # Desenvolver um programa que leia o comprimento de 3 retas e diga ao usuário se
# # elas podem ou não formar um triângulo (estudar a teoria dos triângulos).
# # Pesquisei, e a regra geral é: a soma das medidas de dois lados quaisquer deve ser sempre
# # maior que a medida do terceiro lado.

l1 = int(input('Digite o valor do primeiro segmento de reta: '))
l2 = int(input('Digite o valor do segundo segmento de reta: '))
l3 = int(input('Digite o valor do terceiro segmento de reta: '))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print(f'Os segmentos de reta {l1, l2, l3} não formam um triângulo.')
elif l1 == l2 == l3:
    print(f'Os segmentos de reta {l1, l2, l3} formam um triângulo equilátero.')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print(f'Os segmentos de reta {l1, l2, l3} formam um triângulo isósceles.')
elif l1 != l2 != l3 != l1:
    print(f'Os segmentos de reta {l1, l2, l3} formam um triângulo escaleno.')
print('-- Fim do programa --')


