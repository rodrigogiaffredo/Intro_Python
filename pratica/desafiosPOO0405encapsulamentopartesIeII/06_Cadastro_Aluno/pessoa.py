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

from abc import ABC, abstractmethod
from datetime import date


# SUPERCLASSE
class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int):
        # ATRIBUTOS DA CLASSE
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc


    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f'Ano {ano} inválido.')


    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError('Mudança de idade não permitida, ' \
        'altere o ano de nascimento para recálculo automático.')



# SUBCLASSE HERDEIRA     
class Aluno(Pessoa):

    # ATRIBUTO DA CLASSE
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']

    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__(nome, nasc)
        # ATRIBUTO DO OBJETO
        self._curso = None
        self.curso = curso
        

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f'O curso {curso} não é oferecido na instituição.')


    # MÉTODO
    def add_curso(self, curso:str):
        curso = curso.strip().upper()

        if 3 <= len(curso) <= 5:
            Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError(f'Curso não cadastrado: a sigla {curso} está fora do padrão ' \
                             'permitido para cadastramento de novos cursos.')


