# Neste exercício, "algo" é um objeto, e sempre o objeto tem
# características e realiza funcionalidades (atributos e métodos)
# Conceito de objeto não aprofundado ainda, será tema de aulas mais
# avançadas conforme aviso do professor.

algo = input('Digite algo: ')
print('O tipo primitivo de',(algo), 'é',type(algo))
print(f'{algo} é um número: ',algo.isnumeric())
print(f'{algo} é uma palavra: ',algo.isalpha())
print(f'{algo} está em minúsculas: ',algo.islower())
print(f'{algo} é alfanumérico: ',algo.isalnum())
print(f'{algo} está capitalizado: ',algo.istitle())
print(f'{algo} é somente espaços: ',algo.isspace())
