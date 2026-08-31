# Um programa que mostra o dobro, o triplo, e a raíz quadrada de
# um número informado.

n = int(input('Digite um número: '))
print(f'O dobro de {n} é {n*2}\nSeu triplo é {n*3}\nE sua raiz quadrada é {n**(1/2):.3}')
# Outra forma de apresentar, usando end
print(f'O dobro de {n} é {n*2}',end = ' >>> ')
print(f'Já o seu triplo é {n*3}')
print(f'Finalmente, sua raiz quadrada é {n**(1/2):.3}')
# outra forma de representar a raiz quadrada é usando a função para
# exponenciação pwr
print(f'Finalmente, a raiz quadrada de {n} é {pow(n,1/2):.2f}.')
