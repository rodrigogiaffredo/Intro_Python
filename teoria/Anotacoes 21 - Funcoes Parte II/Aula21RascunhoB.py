# Interactive Help, docstrings para documentação de funções, argumentos opcionais, escopo
# de variáveis, e retorno de resultados.

# DOCSTRING E PARÂMETROS OPCIONAIS

def somar(a=0, b=0, c=0):
    """
    --> Faz a soma de 3 valores e mostra o resultado na tela.
    :param a: opcional, primeiro valor
    :param b: opcional, segundo valor
    :param c: opcional terceiro valor
    :return: não retorna resultado
    --> função criada durante o treinamento Curso em Vídeo, junho/2026
    """
    s = a + b + c
    print(f'A soma vale {s}')

# Programa principal
print()
print('Docstring e parâmetros opcionais no mesmo exercício:')
somar(3, 2, 5)
somar(3, 2)
somar(199)
somar()
somar(c=4, b=2) # Não precisa informar em ordem


# ESCOPO DE VARIÁVEIS

# Variáveis com escopo global: se aplicam tanto ao programa principal, quanto ao escopo
# exclusivo da função, pois foram definidas no corpo do programa principal, podendo ser
# chamadas tanto pela função, quanto pelo programa principal.

def teste():
    print(f'No escopo da função, n vale {n}.')

# Programa principal
print()
print('Escopo global: variável válida tanto na função quanto no programa principal.')
n = 2
print(f'No programa principal, n vale {n}.')

teste()


# Variáveis com escopo LOCAL: definidas no corpo da função, tendo portanto aplicação restrita
# a ela. Se chamarmos uma variável local no corpo do programa principal diretamente, ocorrerá
# um erro. Porém se executarmos a função, ela funcionará normalmente.

def teste():
    x = 3
    print(f'No escopo da função, x vale {x}.')

# Programa principal
print()
print('Escopo local: variável válida exclusivamente na função.')

#print(f'No programa principal, x vale {x}') --> RETORNA UM ERRO (indefinição de variável)

teste() # Funciona normalmente


# Inclusive, a mesma variável pode ter valores diferentes dentro ou fora da função, pois o
# Python permite criação de variável com o mesmo nome, sem misturar os escopos.

def teste():
    n1 = 4 # n1 DENTRO da função, ou n1 de escopo LOCAL
    print(f'N1 dentro vale {n1}.')

# Programa principal
print()
print('A mesma variável criada dentro e fora da função, com valores diferentes.')
n1 = 2 # n1 FORA da função, ou n1 de escopo GLOBAL
print(f'N1 fora vale {n1}.')
teste()


# Permitindo que uma variável local atualize o valor de uma variável global: para isso
# usamos global [variável] no corpo da função para autorizar a substituição do valor da
# variável global pelo novo valor, sem a criação de uma variável local de mesmo nome.

def teste(b):
    global a   # --> Autorização para substituir o conteúdo de 'a' global
    a = 8
    b += 4
    c = 2
    print(f'a dentro vale {a}.')
    print(f'b dentro vale {b}.')
    print(f'c dentro vale {c}.')

# Programa principal
print()
print('Autorizando a substituição do valor de uma variável global pelo da local.')
a = 5   # --> Será substituído por 8 pois autorizamos via função
teste(a)
print(f'a fora vale {a}.')   # --> Imprime 8 ao invés de 5 pois executamos a função antes


# RETORNANDO VALORES DENTRO DAS FUNÇÕES

# Retornando valores em funções (return): são extremamente úteis sempre que precisarmos
# personalizar os resultados no programa principal.

def somar(a=0, b=0, c=0):    # --> Variáveis opcionais
    s = a + b + c
    return s

# Programa principal
print()
print('Retornando valores diretamente da função para o programa principal')
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'As operações solicitadas resultam respectivamente em {r1}, {r2} e {r3}.')

