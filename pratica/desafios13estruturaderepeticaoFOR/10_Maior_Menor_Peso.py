# Criar um programa que leia o peso de 5 pessoas e no final, mostre qual foi o maior,
# e qual foi o menor peso lido.

maior = 0
menor = 0

# Demorei muito para chegar a conclusão que o loop não poderia começar no primeiro peso,
# pois faltaria um parâmetro de comparação na variável 'menor' para os testes em loop.
# Por isso, tirei a primeira pergunta do loop e preenchi tanto maior quanto menor com o
# primeiro valor informado. Daí sim, fazendo mais 4 loops, bastou testar se o peso digitado
# era maior que o maior, ou menor que o menor. Sinapse nova, com certeza.

peso = float(input('Digite o peso da 1a. pessoa (kg): '))
maior = peso
menor = peso
for c in range(2, 5+1):
    peso = float(input(f'Digite o peso da {c}a. pessoa (kg): '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso digitado foi {maior}kg e o menor foi {menor}kg.')
