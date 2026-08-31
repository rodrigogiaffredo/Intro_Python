# Desenvolver uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e
# mostre seu status, de acordo com a tabela: abaixo de 18.5 - abaixo do peso; entre 18.5
# e 25 - peso ideal; 25 até 30 - sobrepeso; 30 até 40 - obesidade; acima de 40 - obesidade
# mórbida.

peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = (peso / (altura ** 2))

if imc < 18.5:
    print(f'Seu IMC está em {imc:.1f} e você está abaixo do peso ideal.')
elif imc <= 25:
    print(f'Seu IMC está em {imc:.1f} e você está no peso ideal.')
elif imc <= 30:
    print(f'Seu IMC está em {imc:.1f} e você está com sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC está em {imc:.1f} e você está obeso.')
else:
    print(f'Seu IMC está em {imc:.1f} e você está com obesidade mórbida.')
print('--- Cuide bem de sua saúde ---')
