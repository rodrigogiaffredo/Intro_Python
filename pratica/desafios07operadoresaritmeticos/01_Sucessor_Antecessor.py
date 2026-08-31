# Um programa que lê um número inteiro e mostra na tela seu
# sucessor e seu antecessor.

n = int(input('Digite um número: '))
ant = n - 1
suc = n + 1
print(f'A sequência antecessor, número, sucessor é: {ant} >>> {n} >>> {suc}.')
# outra forma de fazer caso não queiramos guardar variáveis ant e suc
print(f'A sequência antecessor, número, sucessor é {n-1} >>> {n} >>> {n+1}')
