# Abstração também é um dos pilares da POO. Sua definição clássica é 'a prática de ignorar
# o irrelevante e manter o foco estritamente no essencial.'

from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario


def main():
    aluno1 = Aluno('Creitin', 24, 'Sociologia', 'T024')
    #inspect(aluno1, methods=True)
    aluno1.fazeraniversario() # GENERALIZAÇÃO
    aluno1.fazermatricula() # ESPECIALIZAÇÃO
    #inspect(aluno1)

    professor1 = Professor('Lupércio', 97, 'Física', 'Pós-Doutorado')
    #inspect(professor1, methods=True)
    professor1.fazeraniversario()
    professor1.daraula()
    #inspect(professor1)

    funcionario1 = Funcionario('Rose', 51, 'Analista', 'RH')
    #inspect(funcionario1, methods=True)
    funcionario1.fazeraniversario()
    funcionario1.baterponto()
    #inspect(funcionario1)

    aluno1.estudar()
    professor1.estudar()
    funcionario1.estudar()


if __name__ == '__main__':
    main()
