# Criar um programa que tenha uma função fatorial() que receba 2 parâmetros: o primeiro
# que indique o número a calcular e o outro chamado 'show', que será um valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param n: O número cujo Fatorial será calculado.
    :param show: (opcional) Mostrar ou não o detalhamento do cálculo.
    :return: O valor do fatorial do número n.
    """
    fatorial = 1
    for c in range(n, 0, -1):
        fatorial *= c
        if show == True:
            if c > 1:
                print(f'{c} x ', end = '')
            else:
                print(f'{c} = ', end = '')
    return fatorial

# Programa principal
print()
print(fatorial(5, show = True))
print()
print('\33[97;43mInteractive Help da função << fatorial >>\33[m')
print()
help(fatorial)

