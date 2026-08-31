
# Sobrecarga de OPERADOR: manipulação do funcionamento de operadores de acordo com a necessidade do
#                         programador.


class Carteira:

    def __init__(self, valor:int|float = 0):
        self.__saldo = valor


    def __str__(self):
        return f'Saldo atual na carteira: R$ {self.saldo:,.2f}'


    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('Não é possível alterar o saldo manualmente.')


    # Criação do dunder method de sobrecarga de operador para comparar valores entre carteiras
    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

    # Criação do dunder method de sobrecarga de operador para adicionar valores à carteira
    def __iadd__(self, valor:int|float):
        self.__saldo = self.__saldo + valor
        return self


    # Criação do dunder method de sobrecarga de operador para retirar valores da carteira
    def __isub__(self, valor:int|float):
        self.__saldo = self.__saldo - valor
        return self

    # Criação do dunder method de sobrecarga de operador para verificação de menor ou igual
    def __le__(self, outro):
        if self.__saldo <= outro.__saldo:
            return True
        else:
            return False
        
