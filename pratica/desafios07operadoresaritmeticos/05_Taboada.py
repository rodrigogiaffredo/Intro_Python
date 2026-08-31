# Um programa que mostra a taboada de um número escolhido

n = int(input('Escreva um número e eu te digo a taboada dele: '))

# Criando barrinhas usando operadores aritméticos
print('-' * 20)

# Tanto o múltiplo quanto a resposta sendo mostrados com 2 casas para
# que haja alinhamento

print(f'>>> {n} x {1:2} = {n*1:2}')
print(f'>>> {n} x {2:2} = {n*2:2}')
print(f'>>> {n} x {3:2} = {n*3:2}')
print(f'>>> {n} x {4:2} = {n*4:2}')
print(f'>>> {n} x {5:2} = {n*5:2}')
print(f'>>> {n} x {6:2} = {n*6:2}')
print(f'>>> {n} x {7:2} = {n*7:2}')
print(f'>>> {n} x {8:2} = {n*8:2}')
print(f'>>> {n} x {9:2} = {n*9:2}')
print(f'>>> {n} x {10:2} = {n*10:2}')
print('-' * 20)
