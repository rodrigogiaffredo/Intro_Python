
# Criar um simulador que gerencie pagamentos de diferentes tipos, conforme o diagrama de classes
# abaixo:

# SUPERCLASSE

# Pagamento (abstract)
# --------------------
# # valor
# @fvalor
# --------------------
# pagar()

# SUBCLASSES

# Boleto
# --------------------
# --------------------

# CartaoCredito
# --------------------
# --------------------

# Pix
# --------------------
# --------------------

from abc import ABC, abstractmethod
# Biblioteca 'locale' para localização de valores (nesse caso monetários, mas tem outros)
import locale


class Pagamentos(ABC):

    def __init__(self):
        self._valor = None


    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor:float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("Digite um valor positivo.")

    @property
    def fvalor(self):
        # Jeito simples de formatar o número
        # return f'R$ {self._valor:,.2f}'
        # Formatando o número com 'locale'
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._valor, grouping=True)

    @abstractmethod
    def pagar(self, valor:float):
        pass


class Boleto(Pagamentos):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            # Código para pagamento se fosse vida real mesmo
            return f'Pagamento CONFIRMADO de {self.fvalor} via Boleto.'
        except Exception as e:
            return f'Falha no pagamento de {self.fvalor} via Boleto.'



class Pix(Pagamentos):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            # Código para pagamento se fosse vida real mesmo
            return f'Pagamento CONFIRMADO de {self.fvalor} via Pix.'
        except Exception as e:
            return f'Falha no pagamento de {self.fvalor} via Pix.'



class CartaoCredito(Pagamentos):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            # Código para pagamento se fosse vida real mesmo
            return f'Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito.'
        except Exception as e:
            return f'Falha no pagamento de {self.fvalor} via Cartão de Crédito.'


# Aplicando DUCKTYPING para pagar via método polimórfico

def finalizar_compra(tipo_pag: Pagamentos, valor:float):
    print(tipo_pag.pagar(valor))


















