# Criar a classe Gamer, onde posso cadastrar nome, nick e jogos favoritos de alguém. Criar
# também um métodos que permita mostrar a ficha desse gamer.

from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        # Atributo em formato de LISTA para poder guardar e trabalhar as informações
        # O truque do exercício é esse, unindo LISTAS e OBJETOS, e isso vale para todos os
        # conceitos aprendidos anteriormente (estruturas de repetição, variáveis compostas,
        # etc.)
        self.favoritos = list()

    def adicionarfavoritos(self, jogo):
        self.favoritos.append(jogo)
        # Adiciona o jogo e já coloca na ordem alfabética em seguida
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f'Nome real: [black on blue]{self.nome}[/]'
        conteudo += f'\nJogos Favoritos:'
        # Trabalhando o atributo lista no métodos de instância ficha
        for numero, jogo in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [blue]{jogo}[/]'
        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', width=45)
        print(painel)



jogador1 = Gamer('Ricardo Augusto', 'lordfolk_mor')
jogador1.adicionarfavoritos('Tomb Rider')
jogador1.adicionarfavoritos('Mario Bros')
jogador1.adicionarfavoritos('Sonic')
jogador1.adicionarfavoritos('League of Legends')
jogador1.adicionarfavoritos('Fortnite')
jogador1.ficha()

jogador2 = Gamer('Josileide Mariane', 'tombrider_br')
jogador2.adicionarfavoritos('Call of Duty')
jogador2.adicionarfavoritos('Minecraft')
jogador2.adicionarfavoritos('Mario Kart')
jogador2.adicionarfavoritos('Ursinhos Carinhosos')
jogador2.adicionarfavoritos('Meninas Super-Poderosas')
jogador2.ficha()
