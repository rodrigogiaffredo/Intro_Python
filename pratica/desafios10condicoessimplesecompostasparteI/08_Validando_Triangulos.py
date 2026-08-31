# Desenvolver um programa que leia o comprimento de 3 retas e diga ao usuário se
# elas podem ou não formar um triângulo (estudar a teoria dos triângulos).
# Pesquisei, e a regra geral é: a soma das medidas de dois lados quaisquer deve ser sempre
# maior que a medida do terceiro lado.

r1 = float(input('Digite a medida do 1o. segmento (cm): '))
r2 = float(input('Digite a medida do 2o. segmento (cm): '))
r3 = float(input('Digite a medida do 3o. segmento (cm): '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print(f'Os segmentos medindo respectivamente {r1}, {r2} e {r3} cm PODEM formar um triângulo.')
else:
    print(f'Os segmentos medindo respectivamente {r1}, {r2} e {r3} cm NÃO PODEM formar um triângulo.')
print('--FIM--')
