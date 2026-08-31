
from rich import print
# Importando o módulo que permite trabalhar abstrações no código (Abstract Base Classes)
from abc import ABC, abstractmethod


# GENERALIZAÇÃO
class Pessoa(ABC):  # Agora 'Pessoa' tem as funcionalidades das classes abstratas
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def fazeraniversario(self):
        self.idade += 1

    # O métodos abstrato 'estudar' passa a ser obrigatório para as subclasses
    # Se eu tentar executar o programa do arquivo POO03AbstracaoRascunhoB sem declarar o
    # métodos estudar() para Aluno, Professor e Funcionario, dará erro.
    @abstractmethod
    def estudar(self):
        pass


# ESPECIALIZAÇÃO
class Aluno(Pessoa):        # 'Aluno' ÉUM 'Pessoa'
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)  # Obrigatório chamar o __init__ da SUPERCLASSE
        self.curso = curso
        self.turma = turma

    def fazermatricula(self):
        print(f'{self.nome}, sua matrícula está confirmada.')

    def estudar(self):
        print(f'{self.nome} está estudando {self.curso} na turma {self.turma}')



class Professor(Pessoa):    # 'Professor' ÉUM 'Pessoa'
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)  # Obrigatório chamar o __init__ da SUPERCLASSE
        self.especialidade = especialidade
        self.nivel = nivel

    def daraula(self):
        print(f'Prof. {self.nome} começou a aula.')

    def estudar(self):
        print(f'{self.nome} é especialista em {self.especialidade} no nível de {self.nivel}')



class Funcionario(Pessoa):  # 'Funcionario' ÉUM 'Pessoa'
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)  # Obrigatório chamar o __init__ da SUPERCLASSE
        self.cargo = cargo
        self.setor = setor

    def baterponto(self):
        print(f'{self.nome} bateu o ponto com sucesso.')

    def estudar(self):
        print(f'{self.nome} se especializa para a área de {self.setor}')
