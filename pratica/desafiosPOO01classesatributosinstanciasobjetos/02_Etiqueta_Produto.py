# Criar a classe Produto, onde será possível cadastrar nome e preço. Criar também um
# métodos que mostre a etiqueta de preço do produto.
# ------ Produto ---------
# |	      Tal            |
# ------------------------
# |........ X ...........|
# ------------------------

from rich import print
from rich.panel import Panel


# Declaração da CLASSE
class Produto:
    # Métodos CONSTRUTOR
    def __init__(self, nome, preco):
        # ATRIBUTOS de INSTÂNCIAS
        self.nome = nome
        self.preco = preco

    #Métodos de INSTÂNCIA
    def __str__(self):
        return f'{self.nome} custa R$ {self.preco:,.2f}'

    def etiqueta(self):
        # A variável 'conteudo' da CLASSE 'Panel' recebe as strings de texto
        conteudo = f'{self.nome.center(30, ' ')}'
        conteudo += f'{'-'*30}'
        precoformatado = f'R$ {self.preco:,.2f}'
        conteudo += f'{precoformatado.center(30, '.')}'
        etiqueta = Panel(conteudo, title='Produto', width = 34)
        print(etiqueta)


# Declaração de objetos
prod1 = Produto('Mercedes-AMG série G', 3_000_000)
prod1.etiqueta()

prod2 = Produto('Audi A5', 1_200_000)
prod2.etiqueta()
