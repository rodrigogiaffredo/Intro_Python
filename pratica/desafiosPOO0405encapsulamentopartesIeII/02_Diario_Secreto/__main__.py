# Simular um diário secreto orientado a objetos. O diagrama da SUPERCLASSE Diario é:
# SUPERCLASSE
# Diario
# ATRIBUTOS
# # - __segredos[]
# # - __ senha
# MÉTODOS
# # + escrever(msg)
# # + ler(msg)

from rich import print, inspect
from diario import *


def main():
    meudiario = Diario()
    meudiario.escrever('Não é fácil aprender Encapsulamento.')
    meudiario.escrever('Foco e disciplina são fundamentais.')
    meudiario.escrever('E exercícios, muitos exercícios.')
    print()
    # Garantindo restrição de acesso se não passar a senha, ou se passar senha errada
    try:
        meudiario.ler()
    except Exception as e:
        print(f'Acesso negado. {e}')
    try:
        meudiario.ler('123')
    except Exception as e:
        print(f'Acesso negado. {e}')

    # Agora com senha correta
    meudiario.ler('BdZ!@')


    inspect(meudiario, private=True)


if __name__ == '__main__':
    main()
