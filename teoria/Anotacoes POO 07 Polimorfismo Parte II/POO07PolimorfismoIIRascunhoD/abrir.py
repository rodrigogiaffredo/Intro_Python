
# DUCK TYPING

# Não é um tipo de polimorfismo, mas sim uma prática polimórfica que utiliza um método polimórfico de
# dentro de nossa biblioteca, o qual pode ser chamado independentemente de sua estrutura.

class Porta:
    def abrir(self):
        print('Girar a maçaneta e puxar ou empurrar a porta.')


class Empresa:
    def abrir(self):
        print('Apresentar a documentação necessária para a criação do CNPJ.')

class Ovo:
    def abrir(self):
        print('Quebre a casca e separe as partes.')

class Pedra:
    pass


# Método polimórfico DUCK TYPING exclusivo do Python, com o uso do 'try' para tratamento adequado das
# exceções em que o método, por exigência do código, não funcionar.
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f'Não é possível abrir um objeto tipo {objeto.__class__.__name__}.')



