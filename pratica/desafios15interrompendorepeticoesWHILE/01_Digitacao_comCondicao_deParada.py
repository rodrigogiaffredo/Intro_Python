# Criar um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles, desconsiderando o flag. O flag deve
# ser mencionado entre parênteses no texto do input.

cont = soma = 0

while True:
    n = int(input('Digite um número [999 para sair do programa]: '))
    if n == 999:
        break # O break fica antes das contagens, para não considerar o 999 no resultado.
    cont += 1
    soma += n

print()
print(f'Você digitou {cont} números.')
print(f'A soma dos {cont} números digitados é igual a {soma}.')
