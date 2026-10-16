

# Implementar um exportador de dados funcional para JSON e XML.

# CLASSES

# ----------            ------------
# ALUNO                 USUARIO
# ----------            ------------
# + nome                + nome
# + curso               + email
# + serie               ------------
# ----------            ------------
# ----------


# As classes ALUNO e USUARIO usam serviços das classes JSON e XML (dependência)


# -------------         ------------
# JSON                  XML
# -------------         ------------
# -------------         ------------
# + exportar()          + exportar()
# -------------         ------------



from exportador import *

def main():
    
    u = [Usuario('Creitin', 'creitin@hotmail.com'), Usuario('Marquin', 'marquin@bol.com.br')]

    a = [Aluno('Neide', 'Mecatrônica', '5o. ano'), Aluno('Cleide', 'Sociologia', '1o. ano')]


    exportar_dados(JSON(), u)

    print()

    exportar_dados(XML(), a)




if __name__ == '__main__':
    main()

