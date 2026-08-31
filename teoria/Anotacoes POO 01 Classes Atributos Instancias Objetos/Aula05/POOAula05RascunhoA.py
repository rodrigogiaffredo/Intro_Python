# Resgatando a classe da POOAula04 e fazendo melhorias

# Declaração de classe
class Pessoa:
    # Criando a documentação (docstring) da classe
    """
A classe 'Pessoa' adiciona um item ao cadastro, detalhando nome e idade.
Para cadastrar um novo item, use:
variável = Pessoa(nome, idade)
    """
    def __init__(self, nome = '<não informado>', idade = 0): # Métodos CONSTRUTOR
                                                                      # com chamada de
                                                                      # parâmetros
        # Atributos de instância
        self.nome = nome # Agora recebendo o parâmetro
        self.idade = idade # Agora recebendo o parâmetro

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    # Seja lá o que definirmos no dunder method __str__, é isso que será mostrado
    # quando chamarmos apenas o objeto sem associação a qualquer outro métodos, por
    # exemplo print(p3) - ver execução mais abaixo

    def __str__(self):
        return f'A pessoa {self.nome} tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado atual: nome = {self.nome} | idade = {self.idade}'


# Declaração de objetos
p1 = Pessoa('Rodrigo', 49)
print(p1)
p1.aniversario()
print(p1)

p2 = Pessoa('Bianca', 48)
print(p2)
p2.aniversario()
print(p2)

p3 = Pessoa()
print(p3)

# Para mostrar a documentação de uma classe:
print(Pessoa.__doc__)  # --> 'doc' é um dos dunder attributes de uma classe

# Resultado do dunder method 'str' - ver explicações acima em def __str__:
print(p3)

# Outro dunder attribute é o 'dict', que mostra os dados de um determinado objeto em
# formato dicionário (nota: o dunder method __getstate__() faz a mesma coisa, mas com a
# vantagem de permitir formatação). Já  dunder attribute __clas__ mostra a classe de um
# referido objeto.

print(p1.__dict__)          # Dunder attribute para criação do dicionário (sem parênteses)
print(p3.__class__)         # Dunder attribute para mostrar a classe do objeto referido
print(p2.__getstate__())    # Dunder method (com parênteses), vantagem de poder formatar
