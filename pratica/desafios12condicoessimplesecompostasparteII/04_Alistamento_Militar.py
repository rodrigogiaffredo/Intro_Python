# Fazer um programa que leia o ano de nascimento de um jovem e informe, de acordo com
# sua idade: se ele ainda vai se alistar ao serviço militar; se é a hora de se alistar; se
# já passou o tempo do alistamento. O programa também deverá mostrar o tempo que falta ou
# que passou do prazo.

# Olhei na minha colinha de desafios anteriores como puxar o ano atual.

# Na resolução do exercício o professor incluiu as menções tanto ao ano em que o alistamento
# vai ocorrer, quanto o ano em que deveria ter ocorrido, respectivamente nos casos de menor
# de idade, e maior de 19 anos.

# Incluímos também a verificação homem / mulher, já que no Brasil o alistamento é obrigatório
# somente para homens.

from datetime import date
hoje = date.today().year
nasceu = int(input('Em que ano você nasceu?: '))
sexo = str(input('Digite seu sexo [M / F]: ')).upper()
if (hoje - nasceu) == 18 and sexo == 'M':
    print(f'Você tem {(hoje - nasceu)} anos e deve se alistar o mais rápido possível.')
elif (hoje - nasceu) < 18 and sexo == 'M':
    print(f'Você tem {(hoje - nasceu)} anos e deve se alistar daqui a {18 - (hoje - nasceu)} anos.')
    print(f'Seu alistamento será no ano de {nasceu + 18}.')
elif (hoje - nasceu) > 18 and sexo == 'M':
    print(f'Você tem {(hoje - nasceu)} anos e deveria ter se alistado {(hoje - nasceu) - 18} anos atrás.')
    print(f'Seu alistamento foi em {nasceu + 18}.')
else:
    print('No brasil, alistamento é obrigatório somente para homens.')
print('--- Fim do programa ---')

