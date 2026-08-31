# Criar um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta (inclusive a média calculada a seguir). No final, mostrar um boletim contendo a
# média de cada um com a possibilidade de o usuário mostrar as notas de cada aluno
# individualmente.

# Lista contendo todos os nomes, os pares de notas, e as médias
listageral = list()

# Lista contendo os dados individualizados por aluno (nome, notas e média)
listaaluno = list()

# Lista contendo apenas os pares de notas dos alunos
listanotas = list()



while True:
    nome = str(input('Digite o nome do aluno: ')).title().strip()
    # Lista contendo dados individualizados por aluno recebe nome como elemento único
    listaaluno.append(nome)
    nota1 = float(input(f'Digite a primeira nota de {nome}: '))
    nota2 = float(input(f'Digite a segunda nota de {nome}: '))
    # Lista contendo os pares de notas dos alunos recebe notas individualmente
    listanotas.append(nota1)
    listanotas.append(nota2)
    # Lista contendo dados individualizados por aluno recebe cópia de ambas as notas como elemento único
    listaaluno.append(listanotas[:])
    media = (nota1 + nota2) / 2
    # Lista contendo dados invididualizados por aluno recebe média como elemento único
    listaaluno.append(media)
    # Lista geral recebe cópia de todos os dados do aluno como um só elemento
    listageral.append(listaaluno[:])
    # Limpamos a lista de notas para preparar o novo ciclo
    listanotas.clear()
    # Limpamos a lista de alunos para preparar o novo ciclo
    listaaluno.clear()

    # Loop a prova de usuário para continuar preenchendo o boletim ou mostrar resultado
    opcao = str(input('Cadastrar outro aluno? [S/N]: ')).upper().strip()
    while opcao not in 'SN':
        opcao = str(input('Opção inválida, digite novamente: ')).upper().strip()
    if opcao == 'N':
        break

# Mostrando médias por aluno, após encerramento do primeiro ciclo do programa
print('-' * 25)
print('MÉDIAS FINAIS'.center(25))
print('-' * 25)
print(' ID|','NOME'.center(10),' | MÉDIA'.center(5))
print('-' * 25)

for i, n in enumerate(listageral):
    print(f' {i} | ',f'{listageral[i][0]}'.center(10),f'| {listageral[i][2]}'.center(5))
print('-' * 25)
print()


# Mostrando as notas individuais dos alunos, com base na escolha do usuário
while True:
    notasabertas = int(input('Digite o ID do aluno para detalhes (999 para encerrar): '))
    while notasabertas >= len(listageral) and notasabertas != 999:
        notasabertas = int(input('Opção inválida, digite novamente: '))
    if notasabertas == 999:
        break
    else:
        print('-' * 30)
        print(f'Notas de {listageral[notasabertas][0]}: {listageral[notasabertas][1]}')
        print('-' * 30)

print('-' * 30)
print('-- Fim do Programa --'.center(30))
print('-' * 30)


