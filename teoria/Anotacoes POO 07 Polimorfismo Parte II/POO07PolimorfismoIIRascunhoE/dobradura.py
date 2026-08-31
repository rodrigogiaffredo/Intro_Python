
# DUCK TYPING

# Não é um tipo de polimorfismo, mas sim uma prática polimórfica que utiliza um método polimórfico de
# dentro de nossa biblioteca, o qual pode ser chamado independentemente de sua estrutura.

class Numero:

    def __init__(self, valor:int|float=0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self):
        return f'Tenho o valor {self.valor} dentro do Número.'


class Texto:

    def __init__(self, txt:str=''):
        self.texto = txt

    def dobrar(self):
        self.texto = self.texto + ' ' + self.texto

    def __str__(self):
            return f'Tenho o texto "{self.texto}" dentro do Texto.'
    


class Lista:

    def __init__(self, lst:list=[]):
        self.valores = lst

    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self):
            return f'Tenho os itens {self.valores} dentro da Lista.'
    


class Papel:

    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
            return f'O papel está {'novo' if not self.dobrado else 'dobrado'}.'
    


class Casa:

    def __init__(self):
        pass

    def __str__(self):
            return f'Quem casa quer casa.'


# DUCK TYPING

def tente_dobrar(objeto):
     try:
          objeto.dobrar()
     except:
          print(f'Não foi possível dobrar o objeto {objeto.__class__.__name__}.')
    
