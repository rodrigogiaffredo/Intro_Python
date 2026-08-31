# Fazer um programa que leia o nome completo de uma pessoa e mostre em seguida o
# primeiro e o último nome separadamente. Ex. Ana Maria de Souza ficaria
# primeiro = Ana último = Souza (rfind lfind listas)

nome = str(input('Digite o nome completo da pessoa: ')).strip().title()
quebra = nome.split()

# Aqui eu apelei para o lance do último nome, porque a lógica de listas é diferente
# da de strings, portanto não podemos usar .rfind daí sempre que usarmos o -1 a contagem
# será do final para o começo (-2 seria o próximo da direita para a esquerda, e assim
# sucessivamente).

print(f'O primeiro nome da pessoa é {quebra[0]} e o último é {quebra[-1]}.')
