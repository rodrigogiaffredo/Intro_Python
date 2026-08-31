# agora vamos importar a biblioteca random, que permite a geração de números aleatórios
import random
# a opção abaixo gera um número aleatório entre zero e um
n = random.random()
print(n)
# já a opção abaixo gera um número aleatório inteiro dentro de um intervalo pré-definido
i = random.randint(1, 25)
print(i)
# Dica: para saber a lista completa de módulos disponíveis para importação no Python, basta
# digitar import e logo após o espaço, digito ctrl espaço, e a lista aparece

# Mostrando a data atual, mais especificamente o ano
from datetime import date

# Para o dia de hoje poderia ser também
# from datetime import datetime
# hoje = datetime.now().year

print('Mostrando o ano atual: dia; mês; ano; dia+mês+ano')
print(date.today().day)
print(date.today().month)
print(date.today().year)
print(date.today())

print()

