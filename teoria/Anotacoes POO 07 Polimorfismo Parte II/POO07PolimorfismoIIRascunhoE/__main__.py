
# DUCK TYPING

# Não é um tipo de polimorfismo, mas sim uma prática polimórfica que utiliza um método polimórfico de
# dentro de nossa biblioteca, o qual pode ser chamado independentemente de sua estrutura.

from dobradura import *

def main():
    pass

    a = Numero(200)
    b = Texto('Pessoa')
    c = Lista([1, 2, 3])
    d = Papel()
    e = Casa()

    # Por causa do DUCK TYPING, o ato de 'dobrar' gera resultados diferentes para cada tipo de objeto
    tente_dobrar(a)
    tente_dobrar(b)
    tente_dobrar(c)
    tente_dobrar(d)
    tente_dobrar(e)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


if __name__ == '__main__':
    main()
