# Criar um programa que leia o nome completo de uma pessoa e mostre o nome completo em
# maiúsculas, o nome completo em minúsculas, quantas letras ao total (sem considerar espaços)
# e quantas letras tem o primeiro nome.

# Boa prática recomendada na correção do exercício: usar .strip() no final do input para
# garantir que, mesmo que o usuário adicione espaços desnecessários no começo e no final
# da digitação, eles não afetem os resultados do nosso programa.

nome = str(input('Digite o nome completo: ')).strip()

listado = nome.split()

# Aqui eu perguntei para o NotebookLM, mas o professor já tinha falado sobre o replace,
# eu só não liguei lé com cré, achei preguiça da minha parte, atenção, tem que pensar mais
# até chegar a uma conclusão por conta própria, só apelar se não tiver jeito mesmo.

semespaco = nome.replace(' ','')


print(f'Em maiúsculas: {nome.upper()}.')
print(f'Em minúsculas: {nome.lower()}.')
print(f'Total de letras (sem espaços): {len(semespaco)}.')
# Outro jeito de fazer a contagem de letras sem espaços recomendada na correção do
# exercício com o professor, usando subtraindo nome.count(' ') direto do len(nome):
print(f'Total de letras (sem espaços - versão professor) {len(nome) - nome.count(' ')}.')
print(f'O primeiro nome é {listado[0]} e ele tem {len(listado[0])} letras.')
# Outro jeito de achar o primeiro nome é procurando pelo primeiro espaço, já que tudo antes
# dele será o primeiro nome.
print(f'O primeiro nome (versão professor) tem {nome.find(' ')} letras.')
