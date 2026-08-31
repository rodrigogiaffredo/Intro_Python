# Criar a classe Churrasco, onde possa informar quantas pessoas vão participar e mostre
# quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.

from rich import print
from rich.panel import Panel


class Churrasco:
    # Atributos de CLASSE
    consumopadrao:float = 0.4 # Cada pessoa come 400g de carne, formato já atribuído
    precokilo:float = 82.4 # Preço do kg de carne R$ 82,40, com formato já atribuído

    def __init__(self, titulo, quant):
        # Atributos de INSTÂNCIA
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f'Edição {self.titulo} com {self.participantes} convidados'

    def qtdcarne(self) -> float:
        return self.participantes * Churrasco.consumopadrao

    def custototal(self) -> float:
        return self.qtdcarne() * self.__class__.precokilo

    def custopessoa(self) -> float:
        return self.custototal() / self.participantes

    def analisar(self):
        # É possível adicionar strings ao painel usando '+=' conforme abaixo
        conteudo = (f'Analisando [green]{self.titulo}[/] com [blue]{self.participantes}'
                    f' convidados[/]\n')
        conteudo += (f'Cada participante consumirá {Churrasco.consumopadrao:,.2f}kg, e o custo '
                     f'por kg de carne é de R$ {Churrasco.precokilo:,.2f}\n')
        conteudo += f'Serão necessários [blue]{self.qtdcarne():,.2f} kg[/] de carne\n'
        conteudo += f'O custo total será de [green]R$ {self.custototal():,.2f}[/]\n'
        conteudo += (f'Cada participante deve contribuir com '
                     f'[yellow]R$ {self.custopessoa():,.2f}[/]')

        painel = Panel(conteudo, title=self.titulo)
        print(painel)


# Declaração de OBJETO
churr1 = Churrasco('Churras na Praia', 1500)
churr1.analisar()

churr2 = Churrasco('Costelada Gaúcha', 19)
churr2.analisar()
