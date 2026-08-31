# Prática de interactive help, docstring, parâmetros opcionais, escopos globais e locais,
# e retorno de valores.

# Vamos calcular o fatorial de um número usando RETURN na função

def fatorial(n = 1):   # Deixei opcional, caso não seja informado será sempre 1.
    f = 1   # --> Variável 'f' é local
    for c in range(n, 0, -1):  # --> Lembrando o cálculo do fatorial (ex.: 3! = 3x2x1)
        f *= c
    return f   # --> O resultado do cálculo contido na função

# Programa principal
print()
print('Usando return para calcular o fatorial de um número indicado pelo usuário.')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')
# Fatorial de números pré-definidos, sem entrada do usuário, usando o resultado da função
print('Usando return para calcular o fatorial de variáveis associadas à função com '
      'valores pré-definidos.')
f1 = fatorial(6)
f2 = fatorial(4)
f3 = fatorial()   # --> Se não houver parâmetro, usará 1 (definição opcional que fiz na função).
print(f'Os resultados de fatoração solicitados são {f1}, {f2} e {f3}.')


# Vamos retornar VALORES LÓGICOS, mostrando se um valor é ou não é par

def parouimpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

# Programa principal
print()
print('Retornando valores lógicos de respostas geradas dentro da função.')
num = int(input('Digite um número: '))
print(f'O número digitado é par? R: {parouimpar(num)}')

# Outro jeito de apresentar a resposta:
if parouimpar(num) == True:
    print(f'O número {num} É par.')
else:
    print(f'O número {num} NÃO É par.')