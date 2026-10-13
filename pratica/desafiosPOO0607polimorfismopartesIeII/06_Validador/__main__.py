

# Criar classes para validadores de dados, com os exemplos a seguir, seguindo certas regras:


# SUPERCLASSE

# -----------
# Validador {abstract}
# -----------
# -----------
# + validar()
# -----------


# SUBCLASSES

# ----------            --------------          ------------
# Usuario               Email                   Senha
# ----------            --------------          ------------
# ----------            --------------          ------------
# ----------            --------------          ------------


# Regras de usuário:
# - de 5 a 20 caracteres
# - letras minúsculas
# - números
# - símbolo de sublinhado


# Regras de senha:
# - pelo menos 8 caracteres
# - pelo menos uma maíuscula
# - pelo menos um símbolo


# Regras de e-mail:
# - deve conter uma única @
# - usuário pode conter letras, números e alguns símbolos
# - os domínios contém pontos
# - o TLD (top level domain) encerra com ponto e pelo menos duas letras




from validador import *

def main():

    print()
    print('Validando usuário')
    print()

    validar_dado(Usuario(), 'Dostoyewsky_123')
    validar_dado(Usuario(), 'dostoyewsky_456')
    validar_dado(Usuario(), 'DosToyEwsky 789')

    print()
    print('Validando e-mail')
    print()
    
    validar_dado(Email(), 'dostoyewsky@yahoo.com.br')
    validar_dado(Email(), 'dostoyewsky@yahoo')
    validar_dado(Email(), 'dostoyewsky@yahoo,com')
    validar_dado(Email(), 'dosto yewsky@yahoo.com.br')
    validar_dado(Email(), 'dosto+yewsky@yahoo.com.br')
    validar_dado(Email(), 'dostoyewskyyahoo.com.br')
    validar_dado(Email(), '@dostoyewsky@yahoo.com.br')

    print()
    print('Validando senha')
    print()

    validar_dado(Senha(), 'dosto123')
    validar_dado(Senha(), 'doSto1#23')
    validar_dado(Senha(), 'Dos%3')
    validar_dado(Senha(), 'doSto1^23')
    validar_dado(Senha(), 'DOSTO1#23')
    validar_dado(Senha(), 'DOSTOy1#23')
        
        

    print()






if __name__ == '__main__':
    main()

