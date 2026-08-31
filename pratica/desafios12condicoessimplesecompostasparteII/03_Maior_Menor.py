# Escrever um programa que leia dois números inteiros e compare-os, mostrando na tela
# uma mensagem. O primeiro valor é maior; O segundo valor é maior; Não existe valor maior,
# os dois são iguais.

prim = int(input('Digite o primeiro número: '))
seg = int(input('Digite o segundo número: '))
if prim > seg:
    print(f'O primeiro número digitado ({prim}) é maior que o segundo ({seg}).')
elif seg > prim:
    print (f'O segundo número digitado ({seg}) é maior que o primeiro ({prim}).')
else:
    print(f'Os números digitados são iguais ({prim}, {seg}).')
print('--- Fim do programa ---')

