nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer, {nome}!')
# Aumentando o espaço ocupado pela variável,
# no caso ocupando 20 espaços
print(f'Prazer em te conhecer, {nome:20}!')
# Usando alinhamentos (> à direita, < à esquerda, ^ centralizado
# em X espaços, e se houver um símbolo entre os 2 pontos e o sinal
# estético, ele preenche os espaços vazios com tal símbolo no meu
# exemplo usei * .)
print(f'Prazer em te conhecer, {nome:>20}!')
print(f'Prazer em te conhecer, {nome:*^20}')
