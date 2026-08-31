# Implementar um termostato orientado a objetos. Mínimo de 16o.C, máximo de 30o.C, quando liga
# fica em 24o.C e quando gira a temperatura varia de 0.5 em 0.5o.C. O diagrama de classes da
# SUPERCLASSE Termostato é:

# SUPERCLASSE
# Termostato
# ATRIBUTOS
# # - __temperatura (privado)
# # + @temperatura (validável, limita mínima e máxima e só permite variações inteiras ou de 0.5 em 0.5)
# # + @ftemperatura (validável, retorna temperatura formatada em o.C)

from termostato import *

def main():
    t = Termostato()
    # Validando temperatura mínima em 16
    t.temperatura = 10
    print(t.ftemperatura)
    # Validando temperatura máxima em 30
    t.temperatura = 45
    print(t.ftemperatura)
    # Validando temperatura com valor quebrado autorizado
    t.temperatura = 25.5
    print(t.ftemperatura)

    # Validando temperatura valor quebrado não autorizado
    #t.temperatura = 22.3
    #print(t.ftemperatura)

    # Melhorando a forma de apresentar o erro, através de tratamento de exceção
    try:
        t.temperatura = 22.3
    except Exception as e:
        # Retorna uma mensagem de erro limpa
        print(f'Erro: {e}')
    # Informa a temperatura atual sem a alteração, já que ela não é permitida
    print(f'Temperatura atual: {t.ftemperatura}')


if __name__ == '__main__':
    main()
