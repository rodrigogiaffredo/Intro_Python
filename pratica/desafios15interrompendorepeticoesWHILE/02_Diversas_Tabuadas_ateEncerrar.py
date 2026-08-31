# Fazer um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
# Fazer decoração de cabeçalho e rodapé, e fazer aviso de programa finalizado.


while True:

    cont = 0

    print('-' * 18)
    print('CALCULANDO TABUADA')
    print('-' * 18)

    tab = int(input('Agora você quer ver a taboada de qual número?: '))

    if tab < 0:
        break

    for c in range(0, 10+1):
        print(f'{tab:>2} x {cont:>2} = {cont * tab:>3}')
        cont += 1

    print('-' * 18)

print('-' * 18)
print('-- Número negativo encerra o exercício --')
print('-- Fim do Programa --')
print('-' * 18)
