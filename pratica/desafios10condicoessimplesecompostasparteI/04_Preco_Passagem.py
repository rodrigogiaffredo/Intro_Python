# Desenvolver um programa que pergunte a distância de uma viagem em km. Calcular
# o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e
# R$ 0,45 para viagens mais longas.

percurso = float(input('Quantos km você vai percorrer na sua viagem?: '))
print('Tabela de preços:\n>>> Trajetos de até 200km: R$ 0,50 por km percorrido.\n>>> Trajetos acima de 200km: R$ 0,45 por km percorrido.')
if percurso <= 200:
    print(f'Numa viagem de {percurso}km você vai pagar R$ {(percurso * 0.50):.2f}.')
else:
    print(f'Numa viagem de {percurso}km você vai pagar R$ {(percurso * 0.45):.2f}')
print('--Fim--')

# O professor usou a simplificada aqui também, que nem eu usei no par ou ímpar.
