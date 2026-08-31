# tipo reais
#n = float(input('Digite um valor: '))
#print(n)
#print(type(n))
# tipo inteiros
#n = int(input('Digite um valor: '))
#print(n)
#print(type(n))
# tipo booleano (como digitei um valor, retornou True (tem algo).
# se deixasse em branco e desse enter, retornaria False (não tem algo).
#n = bool(input('Digite um valor: '))
#print(n)
#print(type(n))
# tipo caracteres
#n = str(input('Digite um valor: '))
#print(n)
#print(type(n))
# um bom uso das booleanas
# quando digito número retorna True, senão retorna False
n = input('Digite algo: ')
print(n.isnumeric())
# para saber se é uma letra
print(n.isalpha())
# para saber se é alfanumérico
print(n.isalnum())
# para saber se está tudo maiúsculo
print(n.isupper())
# vale a pena clicar is e analisar as opções de métodos testes de tipo