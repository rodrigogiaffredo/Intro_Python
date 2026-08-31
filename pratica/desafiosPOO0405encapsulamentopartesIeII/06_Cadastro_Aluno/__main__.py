# Implementar a seguinte estrutura de diagrama de classes:

# SUPERCLASSE
# Pessoa
# ATRIBUTOS
# # _nome
# # _nascimento
# + @idade

# SUBCLASSE
# Aluno
# ATRIBUTOS
# + cursos_oficiais
# # _curso
# + @curso
# MÉTODO
# + add_curso(nome)


from pessoa import *

def main():

    # Verificando o funcionamento da SUPERCLASSE
    p = Pessoa('Rodrigo', 1976)
    print(p.idade)

    # Se eu tentar alterar a idade diretamente, o programa dá erro e me impede
#   p.idade = 90

    # Mas se eu alterar o ano de nascimento, ele faz o recálculo e permite a mudança
    p.nascimento = 1995
    print(p.idade)


    # Verificando o funcionamento da SUBCLASSE
    a = Aluno('Marquin', 2011, 'ADM')
    print(a.__dict__)
    
    # Se eu tento criar o registro com um curso inválido (fora da lista), dá erro
#   a = Aluno('Creitin', 2005, 'LAMBDA')

    # Criação de novo curso lista respeitando as regras definidas na função
    a.add_curso('MODA')
    print(a.cursos_oficiais)

    # E como o atributo 'cursos_oficiais' é da classe Aluno, e não do objeto, mesmo que eu 
    # crie outro aluno, o curso novo aparece na lista dele também.
    b = Aluno('Creuza', 1954, 'CONT')
    print(b.__dict__)
    print(b.cursos_oficiais)




if __name__ == '__main__':
    main()
