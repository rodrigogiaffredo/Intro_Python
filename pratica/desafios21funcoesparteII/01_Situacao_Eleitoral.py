# Criar um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
# voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições. A função calcula a idade da pessoa,
# e a função retorna um valor literal, uma frase, sobre o perfil de eleitor.

def voto(idade):
    from datetime import datetime
    ano = datetime.today().year
    idade = ano - nasc
    if idade < 16:
        # Eu tinha usado print, mas o exercício é para retornar texto, então uso 'return'.
        return f'Você tem {idade} anos, ainda NÃO PODE VOTAR.'
    elif idade >= 65 or idade < 18:
        return f'Você tem {idade} anos, voto OPCIONAL.'
    else:
        return f'Você tem {idade} anos, voto OBRIGATÓRIO.'


# Programa principal
print('-' * 35)
print('PERFIL DE ELEITOR')
nasc = int(input('Em que ano você nasceu?: '))
print(voto(nasc))