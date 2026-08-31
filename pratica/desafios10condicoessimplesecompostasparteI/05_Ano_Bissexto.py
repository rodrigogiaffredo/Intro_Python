# Fazer um programa que leia um ano qualquer e mostre se ele é bissexto
# (com base na teoria dos anos bissextos mesmo).


ano = int(input('Digite o ano e eu te digo se ele é bissexto (digite 0 se quiser o ano atual): '))

# Tem um macetinho que o professor ensinou, para perguntar se quer analisar o ano atual
# automaticamente, digitando 0 por exemplo.

from datetime import date
if ano == 0:
    ano = date.today().year

# Anos bissextos são divisíveis por 4, com exceção dos anos terminados em 00, que só
# são bissextos quando divisíveis por 400.
# Ou seja, para ser bissexto o ano:
# 1- É divisível por 4 e não é divisível por 100 (simultâneamente);
# 2- Ou é divisível por 400.

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')
print('--FIM--')
