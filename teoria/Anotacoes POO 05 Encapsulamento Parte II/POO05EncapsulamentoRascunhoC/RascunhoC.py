# Encapsulamento é um dos pilares da POO, o qual visa manter a integridade do sistema,
# protegendo o estado interno do objeto contra inteferência externa não regulamentada.


class Avaliacao:

    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome  # Atributo público
        self.disciplina = disciplina  # Atributo público
        self._nota = nota  # Atributo PROGEGIDO

    # ATRIBUTOS PASSÍVEIS DE VALIDAÇÃO (@PROPERTY)

    @property
    # Criação do caminho passível de validação para poder mexer em '_nota'
    def nota(self): # getter
        return self._nota

    # Definição do setter de @nota
    @nota.setter
    def nota(self, valor): # setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print()
            print('Nota inválida.')
