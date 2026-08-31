# Escrever um programa que pergunte o salário de um funcionário e calcule o valor do
# seu aumento. Para salários superiores a R$ 1.250,00 calcular um aumento de 10%.
# Para os iguais ou inferiores aumento de 15%.

nome = str(input('Digite o nome do funcionário: ')).strip()
salario = float(input(f'Digite o salário atual de {nome}: '))

if salario >= 1250:
    aumento = salario * 1.10
    print(f'O salário atual de {nome} lhe dá direito a um aumento de 10%.\nSeu novo salário passa a ser de R$ {aumento:.2f}.')
else:
    aumento = salario * 1.15
    print(f'O salário atual de {nome} lhe dá direito a um aumento de 15%.\nSeu novo salário passa a ser de R$ {aumento:.2f}.')
print('--FIM--')
