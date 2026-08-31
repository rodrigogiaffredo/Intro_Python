# Criar uma classe que represente um retângulo pelas suas medidas e área. O diagrama da
# SUPERCLASSE Retangulo é:
# SUPERCLASSE
# Retangulo
# ATRIBUTOS
# # # _base
# # # _altura
# # # _área
# # + @base
# # + @altura
# # + @medidas
# # + @area

from retangulo import *


def main():

    r = Retangulo()
    try:
        r.base = 12
        r.altura = 4
        r.medidas = (8, 12)
    except Exception as e:
        print(f'Ocorreu um erro do tipo {type(e).__name__}: {e}')

    print(r.medidas)


if __name__ == '__main__':
    main()
