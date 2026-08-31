# Refazer o exercício da aula 07 sobre tabuada, mas agora utilizando o laço de repetição
# FOR. Enunciado do desafio 05 da aula 07: Criar um programa que mostra a tabuada de um
# número escolhido.


num = int(input('Digite um número e eu calculo a tabuada dele: '))
for c in range (0, 10+1):
    print(f'{num} x {c:>2} = {c * num:>3}')
print('-- Fim --')

