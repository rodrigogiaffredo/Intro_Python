# Escrever um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal, 3 para
# hexadecimal (pesquisar se algum módulo já resolve nativamente).

# Durante minhas pesquisas descobri que o Python tem funções nativas para esses cálculos.
# Aprendi também que é boa prática excluir os 3 primeiros caracteres que o Python traz na
# função, para dar aparência matemática comum ao resultado. E por questão estética, deixei
# o hexadecimal em maiúsculas.

num = int(input('Digite um número inteiro: '))
print(f'Escolha uma das opções abaixo: \n>>> 1- Para saber o binário de {num}\n>>> 2- Para saber o octal de {num}\n>>> 3- Para saber o hexadecimal de {num}')
escolha = int(input('Opção escolhida: '))
bina = bin(num)
octa = oct(num)
hexa = hex(num)
if escolha == 1:
    print(f'O número {num} em formato binário é igual a {bina[2:]}.')
elif escolha == 2:
    print(f'O número {num} em formato octal é igual a {octa[2:]}.')
elif escolha ==3:
    print(f'O número {num} em formato hexadecimal é igual a {hexa[2:].upper()}.')
else:
    print('Opção inválida. Execute o programa novamente.')
print('-- Obrigado por participar --')





