# Criar uma classe Caneta, que simule o funcionamento de uma caneta colorida, podendo
# escrever frases na cor selecionada.

from rich import print

class Caneta:
    def __init__(self, cor = 'azul'):
        # Combinar ('match') caso a caso (essa é nova, não tinha aprendido até hoje)
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case _: # Qualquer coisa diferente das opções anteriores ('_:')
                escolha = '[white]'
        self.cor = escolha
        # No exercício, toda caneta criada começa a história tampada
        self.tampada = True

    def escrever (self, msg):
        if self.tampada:     # Equivale a dizer que a caneta está tampada pois ela começa True
            print(f':prohibited: A {self.cor}caneta[/] está tampada.')
        else:
            print(f'{self.cor}{msg}[/]', end=' ')

    def quebrarlinha(self, qtd=1):
        print('\n' * qtd, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


caneta1 = Caneta('azul')
caneta2 = Caneta('vermelha')
caneta3 = Caneta('verde')
caneta1.destampar()
caneta2.destampar()

caneta1.escrever('Hello World!')
caneta2.escrever('Hello World!')
caneta2.quebrarlinha(3)     # Quebrei 3 linhas
caneta3.escrever('Hello World!')
caneta3.quebrarlinha(2)     # Quebrei 2 linhas
#caneta1.tampar()     # Se eu tampo a caneta ela deixa de funcionar
caneta1.escrever('Será que funciona?')
