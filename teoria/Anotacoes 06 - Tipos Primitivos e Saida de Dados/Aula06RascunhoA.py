
# sem classificar o resultado do input como inteiro
# n1 = (input('Digite o primeiro valor: '))
# n2 = (input('Digite o segundo valor: '))
# s = n1 + n2
# concatenou ao invés de somar
# print('A soma dos valores digitados é',s)
# pois os tipos das variáveis estão como string
# print(type(n1),type(n2))



# classificando o resultado do input como inteiro
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1 + n2
# somou corretamente os valores
print('A soma dos valores digitados é',s)
# pois os tipos das variáveis estão como inteiro
print(type(n1),type(n2))
# como eu fiz para mostrar os valores somados com base no que sabia
# print('A soma entre',n1,'e',n2,'é',s)
# como eu aprendi a fazer nessa aula usando .format
print('Jeito Classico A soma entre {} e {} vale {}' .format(n1, n2, s))
# dei um vacilo enorme colocando vírgula antes do ponto e isso
# quebrou o código, porque format tem que fazer parte de print
# e não ser considerado como um módulo separado da string
# o Curso em Video é antigo, hoje em dia as f-strings estão mais
# para o formato abaixo, vou anotar for the records:
print(f'Com f-string A soma entre {n1} e {n2} é {s}')
