
# DUCK TYPING

# Não é um tipo de polimorfismo, mas sim uma prática polimórfica que utiliza um método polimórfico de
# dentro de nossa biblioteca, o qual pode ser chamado independentemente de sua estrutura.

from abrir import *

def main():

    a = Porta()
    b = Empresa()
    c = Ovo()
    d = Pedra()

    # Executando o método polimórfico DUCK TYPING exclusivo do Python
    tentar_abrir(a)
    tentar_abrir(b)
    tentar_abrir(c)
    tentar_abrir(d)


if __name__ == '__main__':
    main()

