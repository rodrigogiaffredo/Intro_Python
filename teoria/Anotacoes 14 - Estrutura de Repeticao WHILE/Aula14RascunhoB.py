# Imprimindo uma sequência de números (os 10 primeiros)
c = 0
while c != 10:
    c += 1
    print(c)
print('-- Fim --')
print()

# Enquanto o valor digitado não for 0, não pare de perguntar
n = ()
while n != 0:
    n = int(input('Digite um valor: '))
print('Finalmente você digitou 0.')
print('-- Fim --')
print()

# Enquanto a resposta for sim, continua executando o programa
resp = 'S'
num = ()
while resp == 'S':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar jogando? S / N: ')).upper().strip()
print('-- Fim --')
print()

# Enquanto a resposta for diferente de 0, digite um número e conte pares e ímpares
num = ()
par = 0
impar = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0: # excluindo o zero da análise, pois ele não é par nem ímpar.
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares, e {impar} números ímpares.')
print('-- Fim --')
print()
