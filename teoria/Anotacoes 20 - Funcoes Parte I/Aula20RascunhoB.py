# Funções (ou rotinas) são trechos de código que podem ser executados em momentos diferentes
# seja com parâmetros simples, seja com parâmetros múltiplos.

# Em exercícios, é difícil dimensionar o valor das funções, já que os códigos geralmente são
# pequenos. Mas ao desenvolver programas maiores, o valor delas aparece.

# Situação onde valores diferentes são somados
# Sem funções
print('Digitando tudo 3x na unha:')
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
print()
# Com funções (criando uma função soma)
print('Criando a função e chamando 3x no código principal:')
def soma(a, b):
    s = a + b
    print(s)
# Código principal
soma(4, 5) # Passando os parâmetros 4 e 5 para a recém-criada função 'soma'
soma(8, 9) # Passando os parâmetros 8 e 9 para a recém-criada função 'soma'
soma(2, 1) # Passando os parâmetros 2 e 1 para a recém-criada função 'soma'
print()

# Nota importante: na definição da função, eu disse que serão necessários 2 parâmetros
# portanto se eu colocar por exemplo 1 ou 3 parâmetros, o programa dá erro.

# Deixando mais explícito qual valor se refere a qual parâmetro
print('Especificando na chamada da função qual a variável preenchida por certo valor:')
soma(a=4, b=5)
soma(a=8, b=9)
soma(a=2, b=1)
print()

# Podemos também alterar a ordem dos valores na execução da função, apenas alterando a
# variável a que o valor se refere.
# Note que sempre que explicitamos a variável de uma função que, como no nosso exemplo,
# exige 2 parâmetros ('a' e 'b'), ambos devem ser mencionados, não podemos por exemplo
# chamar a função assim: soma(a=4, 5) e supor que o Python associará o 5 ao 'b', pois isso
# não vai acontecer e o programa vai dar erro.
# Porém, caso não explicite nenhum dos parâmetros, por default o primeiro será sempre o 'a'
# e o segundo será sempre o 'b' (no nosso exemplo).
print('Alternando valores através da referência à variável da função:')
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
# Programa principal
soma(a=4, b=5) # Referenciando 'a' e 'b'
soma(b=4, a=5) # Referenciando 'b' e 'a'
soma(7, 2) # Sem ambas as referências
print()

# EMPACOTAMENTO de parâmetros

# O símbolo '*', quando usado associado a um parâmetro na definição de uma função, abre o
# precedente da indefinição de quantos parâmetros ela deve executar. Ele desempacota
# todos os parâmetros passados na chamada da função, sejam eles quantos forem.

# Por exemplo, uma função 'contador' que imprima os números que foram passados pelo usuário.
# Mesmo que a quantidade de números passados seja diferente em cada chamada da função 'contador'
# o Python conseguirá executá-la pois '*' antes da variável aciona esse poder.
print('Empacotamento / desempacotamento de parâmetros:')
def contador(* num): # Aqui eu digo ao Python 'vou receber não sei quantos parâmetros)
    print(num)
# Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print()


# O resultado é a criação de 3 tuplas, cada uma contendo os respectivos valores, e a partir
# daí posso trabalhar com elas, como se trabalha com tuplas. Podemos por exemplo usar FOR:
print('Usando FOR nas tuplas resultantes através de função:')
def contadorfor(* numb):
    for v in numb:
        print(f'{v}', end = '  ')
    print('--Fim--')
# Programa principal
contadorfor(2, 1, 7)
contadorfor(8, 0)
contadorfor(4, 4, 7, 6, 2)
print()


# Consigo também trabalhar a relação entre os conteúdos de uma tupla, por exemplo, somar
# todos os números que a compõem
print('Somando os valores de uma tupla e mostrando o total via funções:')
def somatupla(* numeros):
    s = 0
    for val in numeros:
        s += val
    # Cuidado com a identação, dei alguns moles daí imprimiu 'n' vezes a frase, então
    # quando acontecer de novo já sabe, a pista é identar
    print(f'Recebi os valores {numeros} e a soma deles deu {s}.')
#Programa principal
# Não importa quantos elementos a tupla contenha, ele desempacota por causa do '*'
somatupla(2, 1, 7) # Desempacota e soma os 3 elementos
somatupla(8, 0) # Desempacota e soma os 2 elementos
print()



# Consigo também mostrar quantos elementos tenho em cada tupla resultante da execução da
# função recém-criada
print('Descobrindo o tamanho das tuplas resultantes da função:')
def contadortam(* nume):
    tam = len(nume)
    print(f'Recebi os valores {nume}, ao todo são {tam}.')
# Programa principal
contadortam(2, 1, 7)
contadortam(8, 0)
contadortam(4, 4, 7, 6, 2)
contadortam(0)
print()


# Agora o poder das funções é extrapolado verdadeiramente quando trabalhamos com as listas,
# já que as tuplas são imutáveis, ao contrário das listas que são mutáveis e abrem muitas
# possibilidades.
print('Funções utilizadas para trabalhar com listas (super-poder, no exemplo, de dobrar valores):')
def dobra(listinha): # Como a lista é uma variável composta mutável, não preciso empacotar
    posicao = 0 # Crio a variável contadora 'posicao'
    while posicao < len(listinha): # Enquanto ela for menor que o tamanho da lista
        listinha[posicao] *= 2 # Passo dobrando valor por valor
        posicao += 1 # E adiciono 1 à posicao
# Programa principal
valores = [7, 2, 5, 0, 4]
# Digamos que por qualquer motivo, rotineiramente precisemos dobrar os valores da lista
print(valores) # Impressão da lista inicial
dobra(valores) # Execução da função
print(valores) # Impressão da nova lista
print()
