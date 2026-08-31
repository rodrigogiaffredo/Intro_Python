# Criar um programa que mostre na tela todos os números pares que estão no intervalo entre
# 1 e 50.

for c in range(1, 50+1):
    if c % 2 == 0:
        print(c, end= ' ')
print()
print('-- Fim --')


# Sugestão do professor na correção do exercício:
# Outro modo de executar é pulando de 2 em 2 começando do 2, isso elimina a necessidade de
# teste lógico e deixa a performance do programa melhor por exigir menos processamento (os
# laços com if testam 2 condições por passagem, enquanto esse modo simplesmente pula e
# imprime).

print()
print('Com economia de processador:')
for c in range (2, 50+1, 2):
    print(c, end= ' ')
print()
print('-- Fim --')

