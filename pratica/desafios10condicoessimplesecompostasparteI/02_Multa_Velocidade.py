# Escrever um programa que leia a velocidade de um carro. Se ela ultrapassar 80km/h
# mostrar a mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 para cada
# km acima do limite.

velocidade = float(input('Você estava a quantos km/h? Não minta: '))
if velocidade > 80:
    print(f'Você excedeu o limite de 80km/h.\nVai pagar uma multa de R$ 7,00 por km excedido, equivalente a R$ {(velocidade - 80) * 7:.2f}.')
else:
    print(f'{velocidade}km/h está dentro do limite permitido, que é de 80km/h.\nPode seguir viagem.')
print('--FIM--')

# O professor resolveu usando uma condicional simples (sem o else), baseada somente na
# identação do código.

print()
print('Versão do professor')
if velocidade > 80:
    print(f'Você excedeu o limite de 80km/h.\nVai pagar uma multa de R$ 7,00 por km excedido equivalente a R$ {(velocidade - 80) * 7:.2f}.')
print('Você está dentro do limite permitido, pode seguir viagem.')
