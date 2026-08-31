# Fazer um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo: '))

#while sexo != 'M' and sexo != 'F':
while sexo not in 'MF': # (o professor usou essa configuração, gostei também)
    print('Opção inválida, digite novamente.')
    sexo = str(input('Digite o sexo: ')).upper().strip()

print('Sexo cadastrado com sucesso.')
print('-- Fim --')
