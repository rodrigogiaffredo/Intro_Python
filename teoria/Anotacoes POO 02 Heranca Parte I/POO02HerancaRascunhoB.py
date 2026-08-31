# HERANÇA

# Herança é um relacionamento entre itens gerais (ancestrais) e tipos mais específicos
# (descendentes) desses itens, que herdam ATRIBUTOS e MÉTODOS dos níveis superiores. É
# como herdar características e comportamentos dos pais. Assim como não há necessidade
# dos herdeiros serem exclusivamente cópias parciais dos pais, os itens descendentes
# podem ter seus próprios métodos e atributos, ideia que será aprofundada quando falarmos
# em especialização.

# Outros nomes do mecanismo de herança: GENERALIZAÇÃO, RELAÇÃO TIPO 'É UM'

from rich import print, inspect

# GENERALIZAÇÃO
class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def fazeraniversario(self):
        self.idade += 1

# A relação de herança com a classe 'Pessoa' é estabelecida quando colocamos ela entre
# parênteses logo após o nome da subclasse com a qual queremos estabelecer o vínculo.
# Neste exemplo, para cada aluno, professor e funcionário que eu criar, os atributos
# 'nome' e 'idade' e o métodos 'fazeraniversario' já estão incluídos no pacote.


# ESPECIALIZAÇÃO
class Aluno(Pessoa):        # 'Aluno' ÉUM 'Pessoa'
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)  # Obrigatório chamar o __init__ da SUPERCLASSE
        self.curso = curso
        self.turma = turma

    def fazermatricula(self):
        print(f'{self.nome}, sua matrícula está confirmada.')


class Professor(Pessoa):    # 'Professor' ÉUM 'Pessoa'
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)  # Obrigatório chamar o __init__ da SUPERCLASSE
        self.especialidade = especialidade
        self.nivel = nivel

    def daraula(self):
        print(f'Prof. {self.nome} começou a aula.')


class Funcionario(Pessoa):  # 'Funcionario' ÉUM 'Pessoa'
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)  # Obrigatório chamar o __init__ da SUPERCLASSE
        self.cargo = cargo
        self.setor = setor

    def baterponto(self):
        print(f'{self.nome} bateu o ponto com sucesso.')


aluno1 = Aluno('Creitin', 24, 'Sociologia', 'T024')
# O 'inspect' mostra a lista de atributos contendo não somente os diretamente associados
# ao objeto 'aluno', mas também os associados à superclasse 'pessoa'. O mesmo acontece
# para os métodos.
inspect(aluno1, methods=True)
# Se eu mando 'aluno1' fazer aniversário, a idade muda pois ele herda o métodos
# 'fazeraniversario() da superclasse, assim como herdou os atributos 'nome' e 'idade'.
aluno1.fazeraniversario() # GENERALIZAÇÃO
aluno1.fazermatricula() # ESPECIALIZAÇÃO
inspect(aluno1)


professor1 = Professor('Lupércio', 97, 'Física', 'Pós-Doutorado')
inspect(professor1, methods=True)
professor1.fazeraniversario()
professor1.daraula()
inspect(professor1)

funcionario1 = Funcionario('Rose', 51, 'Analista', 'RH')
inspect(funcionario1, methods=True)
funcionario1.fazeraniversario()
funcionario1.baterponto()
inspect(funcionario1)
