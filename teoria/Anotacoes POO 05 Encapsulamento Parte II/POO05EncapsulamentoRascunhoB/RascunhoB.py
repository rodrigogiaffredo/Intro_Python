# Encapsulamento é um dos pilares da POO, o qual visa manter a integridade do sistema,
# protegendo o estado interno do objeto contra inteferência externa não regulamentada.


class Avaliacao:

    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome # Atributo público
        self.disciplina = disciplina # Atributo público
        self._nota = nota # Atributo PROGEGIDO

    # MÉTODOS ACESSORES

    def get_nota(self): # Métodos GETTER
        return self._nota

    def set_nota(self, valor): # Métodos SETTER
        if valor <= 10:
            self._nota = valor
        else:
            print()
            print('Nota inválida.')
