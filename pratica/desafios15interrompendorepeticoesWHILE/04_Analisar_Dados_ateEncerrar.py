# Criar um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, ele deve mostrar:
# 1- quantas pessoas são maiores de 18 anos 2- quantos homens foram cadastrados 3- quantas
# mulheres tem menos de 20 anos.

print('-' * 20)
print('CADASTRO DE DADOS')

pessoamaiordezoito = 0
homem = 0
mulhermenosdevinte = 0

while True:
    print('-' * 20)
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        pessoamaiordezoito += 1

    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    while True:
        if sexo not in 'MF':
            sexo = str(input('Opção inválida. Digite novamente: ')).upper().strip()
        else:
            break

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        mulhermenosdevinte +=1

    print('-' * 20)
    print('Dados cadastrados com sucesso.')

    decisao = str(input('Quer continuar? [S/N]: ')).upper().strip()
    print('-' * 20)
    print()
    while True:
        if decisao not in 'SN':
            decisao = str(input('Opção inválida, digite novamente: ')).upper().strip()
        else:
            break

    if decisao == 'N':
        break

print('-' * 20)
print(f'Foram cadastradas {pessoamaiordezoito} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {mulhermenosdevinte} mulheres com menos de 20 anos.')
print('-' * 20)
print('-- Fim do Programa --')
