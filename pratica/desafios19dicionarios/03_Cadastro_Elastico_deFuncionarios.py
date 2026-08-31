# Criar um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
# (com idade, não quero guardar o ano de nascimento e sim a idade) num dicionário e a ctps
# for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcular e acrescentar, além da idade, com quantos anos a pessoa vai se aposentar. No
# dicionário estarão nome, idade (e não ano de nascimento) e carteira de trabalho, e se o
# número da ctps for diferente de zero tem que perguntar e cadastrar no dicionário também o
# ano de contratação e o salário dela, e também vai incluir no dicionário mas não como
# entrada e sim como cálculo com quantos anos ela vai se aposentar - considerando
# aposentadoria após 35 anos de contribuição a partir da data da primeira assinatura em
# carteira (dicionário pode ter de 3 a 6 chaves dependendo de ter ou não ctps).

from datetime import date
hoje = date.today().year

# Poderia ser também from datetime import datetime
# hoje = datetime.now().year

cadastro = dict()
# Lembrando que podemos chamar o input diretamente para dentro do item do dicionário, não
# é preciso por exemplo criar a variável 'nome' e depois inserí-la no cadastro['nome']
cadastro['Nome'] = str(input('Digite o nome do funcionário: ')).capitalize().strip()
nasc = int(input(f'Digite o ano de nascimento de {cadastro['Nome']}: '))
idade = hoje - nasc
cadastro['Idade'] = idade
cadastro['CTPS'] = int(input(f'Digite o número da CTPS de {cadastro['Nome']} (0 se não houver): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input(f'Digite o ano de contratação de {cadastro['Nome']}: '))
    cadastro['Salário'] = float(input(f'Digite o salário atual de {cadastro['Nome']}: R$ '))
    idade_aposent = (cadastro['Contratação'] + 35) - nasc
    cadastro['Aposentadoria'] = idade_aposent


print('-' * 50)
print(cadastro)
print('-' * 50)

for k, v in cadastro.items():
    print(f'{k}: {v}')





