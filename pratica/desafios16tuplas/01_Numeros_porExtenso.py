# Criar um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até 20. O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
# por extenso. Ou seja, dentro da tupla estarão os conteúdos extenso = ('um', 'dois', 'três',
# etc.) e a resposta será o número escolhido, escrito por extenso. Se o usuário escolher 10,
# eu retorno 'Você escolheu o número dez.' Programa à prova de usuário.

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

print('-' * 30)
numero = int(input('Digite um número entre 0 e 20: '))

while numero not in range(0, 20+1):
    numero = int(input('Opção inválida, digite um número entre 0 e 20: '))

print(f'Você digitou o número {extenso[numero]}.')
print()

# Durante a correção o professor sugeriu a criação do loop infinito para continuar ou não
# jogando.

while True:
    opcao = str(input('Quer digitar novamente? [S/N]: ')).strip().upper()
    while opcao not in 'SN':
        opcao = str(input('Opção inválida, digite novamente: ')).strip().upper()

    if opcao == 'S':
        print('-' * 30)
        numero = int(input('Digite um número entre 0 e 20: '))

        while numero not in range(0, 20 + 1):
            numero = int(input('Opção inválida, digite um número entre 0 e 20: '))

        print(f'Você digitou o número {extenso[numero]}.')
        print()
    else:
        break

print('-- Fim --')
