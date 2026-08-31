# Um programa que pergunta a quilometragem rodada, e os dias alugados
# e calcula o custo total da locação do veículo.
# O carro custa R$ 60 por dia e R$ 0.15 por km rodado.

d = int(input('Quantos dias você ficou com o carro?: '))
k = float(input('Quantos km você rodou ao todo?: '))
pagar = (d * 60) + (k * 0.15)
print('>>> Custo unitário da diária: R$ 60,00\n>>> Custo unitário do km rodado: R$ 0,15')
print(f'>>> Total a pagar: R$ {pagar:.2f}')
