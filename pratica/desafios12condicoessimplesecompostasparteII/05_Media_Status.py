# Criar um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
# mensagem no final, de acordo com a média atingida: média abaixo de 5.0: REPROVADO média
# entre 5.0 e 6.9: RECUPERAÇÃO média 7.0 ou superior: APROVADO.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Média {media:.1f} - REPROVADO.')
elif media >= 5 and media <= 6.9:
    # Muito legal: o Python também aceita a notação 6.9 >= media > 5
    print(f'Média {media:.1f} - EM RECUPERAÇÃO.')
else:
    print(f'Média {media:.1f} - APROVADO!')
print('--- Fim do programa ---')
