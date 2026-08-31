# A confederação nacional de natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos
# MIRIM, até 14 anos INFANTIL, até 19 anos JÚNIOR, até 25 anos SÊNIOR, acima MASTER.

# Dica do professor: como as categorias se sobrepõem, não precisei da primeira parte
# do teste lógico. Ex.: ao invés de 9 < idade <= 14 pode ser só idade <= 14 pois o teste
# de idade > 9 já tinha ocorrido no passo anterior do programa.

from datetime import date
hoje = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta (9999): '))
idade = hoje - nasc

if idade <= 9:
    print(f'O atleta tem {idade} anos e sua categoria é MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e sua categoria é INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e sua categoria é JÚNIOR.')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e sua categoria é SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos e sua categoria é MASTER.')
print('--- Fim do programa ---')
