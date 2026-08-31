# Criar um programa que tenha a função leiaint() que vai funcionar de forma semelhante a
# função input() do Python, só que fazendo a validação para aceitar apenas um valor
# numérico. Ex: n = leiaint('Digite um n').

def leiaint(msg):
    # Entrada em formato string senão a função 'isdecimal()' falha
    val = str(input(msg))
    while True:
        if val.isdecimal(): #  --> Conversando com o LM descobri o .isdecimal()
            break
        else:
            val = str(input('\33[31mERRO! Digite apenas valores inteiros: \33[m'))
    return val


# Programa principal
print()
print('-' * 35)
n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')
