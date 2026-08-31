# Um programa que pergunta nome e salário de um funcionário e
# informa o novo salário após aumento de 15%

nome = str(input('Qual o nome do funcionário que receberá aumento? '))
atual = float(input(f'Qual o salário atual de {nome}? R$: '))
aumento = atual + (atual * 15/100)
print(f'Após o aumento de 15%, o salário de {nome} passará',end=' ')
print(f'a ser de R$ {aumento:.2f}')
