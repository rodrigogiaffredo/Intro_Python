# Criar uma classe Controleremoto para simular o funcionamento de um controle simples
# (canal, volume e liga/desliga).

from rich import print
from rich.panel import Panel


class Controleremoto:
    canalminimo:int = 1
    canalmaximo:int = 5
    volumeminimo:int = 1
    volumemaximo:int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canalatual:int = canal
        self.volumeatual:int = volume
        self.ligado:bool = False

    def ligadesliga(self):
        # Desse modo, se estiver ligado, desliga - e vice-versa
        self.ligado = not self.ligado

    def canalmais(self):
        # Premissa básica: a TV deve estar ligada
        if self.ligado:
            # Sempre que estivermos no último canal e avançarmos, ele volta para o primeiro
            if self.canalatual == Controleremoto.canalmaximo:
                self.canalatual = Controleremoto.canalminimo
            else:
                self.canalatual += 1

    def canalmenos(self):
        # Premissa básica: a TV deve estar ligada
        if self.ligado:
            # Sempre que estivermos no primeiro canal e recuarmos, ele volta para o último
            if self.canalatual == Controleremoto.canalminimo:
                self.canalatual = Controleremoto.canalmaximo
            else:
                self.canalatual -= 1

    def volumemais(self):
        if self.ligado:
            # Quando o volume chega no máximo, ele para de aumentar
            if self.volumeatual != Controleremoto.volumemaximo:
                self.volumeatual += 1

    def volumemenos(self):
        if self.ligado:
            # Quando o volume chega no mínimo, ele para de diminuir
            if self.volumeatual != Controleremoto.volumeminimo:
                self.volumeatual -= 1

    def mostrartv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = ':prohibited: [red]TV DESLIGADA[/]'
        else:
            conteudo = 'CANAL  = '
            for canal in range(Controleremoto.canalminimo, Controleremoto.canalmaximo + 1):
                if canal == self.canalatual:
                    conteudo += f'[yellow on yellow] {canal} [/]'
                else:
                    conteudo += f' {canal} '
            conteudo += f'\nVOLUME = '
            for volume in range(Controleremoto.volumeminimo, Controleremoto.volumemaximo + 1):
                if volume <= self.volumeatual:
                    conteudo += '[black on cyan]   [/]'
                else:
                    conteudo += '[black on white]   [/]'
        tv = Panel(conteudo, title='[ TV ]', width=30)
        print(tv)


controle = Controleremoto()
while True:
    controle.mostrartv()
    comando = str(input(f' < CH{controle.canalatual} >   - VOL{controle.volumeatual} +   '))
    match comando:
        case '0':
            break
        case '@':
            controle.ligadesliga()
        case '>':
            controle.canalmais()
        case '<':
            controle.canalmenos()
        case '+':
            controle.volumemais()
        case '-':
            controle.volumemenos()
    print('\n' * 10)
