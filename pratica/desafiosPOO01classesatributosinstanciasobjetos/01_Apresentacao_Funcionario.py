# Criar a classe Funcionário, onde podemos cadastrar nome, setor e cargo. Criar também um
# métodos que permita ao funcionário se apresentar.

from rich import print
from rich import inspect

# Declaração da CLASSE
class Funcionario:
    # ATRIBUTO da CLASSE
    empresa = 'SERPRO'  # Atributos de CLASSE impactam todos os métodos e objetos
    # Métodos CONSTRUTOR
    def __init__(self, nome, cargo, setor):
        # ATRIBUTOS da INSTÂNCIA
        self.nome = nome
        self.cargo = cargo
        self.setor = setor

    # Métodos de INSTÂNCIA
    def apresentacao(self) -> str:   # A junção '-> str' define o retorno como string
        return (f':handshake: Olá, eu sou [blue]{self.nome}[/] e estou {self.cargo} do setor de {self.setor} '
                f'da empresa {self.__class__.empresa}.') # Chama atributo da CLASSE

# Declaração de OBJETOS
f1 = Funcionario('Rodrigo', 'Diretor', 'Tecnologia' )
# inspect(f1, methods=True)
print(f1.apresentacao())
f2 = Funcionario('Bianca', 'Vice-Presidente', 'RH')
# inspect(f2, methods=True)
print(f2.apresentacao())
