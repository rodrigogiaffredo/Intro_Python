# Encapsulamento é um dos pilares da POO, o qual visa manter a integridade do sistema,
# protegendo o estado interno do objeto contra inteferência externa não regulamentada.

# Voltando ao exemplo da conta bancária criado no RascunhoD na aula 06 (módulo rich).

class Contabancaria:
    """
    A classe 'Contabancaria' cria uma conta bancária, permitindo saques e depósitos.
    """

    def __init__(self, id, nome, saldo = 0):
        # Atributos de instância
        self.id = id # público (+)
        # Botão direito sobre '_titular', rename / current file para inserir o '_' em todas
        # as ocorrências de uma vez só
        self._titular = nome # protegido (#)
        # Idem para __saldo, porém inserindo '__'
        self.__saldo = saldo # privado ('-')
        print()
        print(f'Conta {id} criada com sucesso. Saldo atual: US$ {self.__saldo:,.2f}')

    def __str__(self):
        #return (f'Saldo atual da conta {self.id} em nome de {self._titular}: '
                #f'US$ {self.__saldo:,.2f}')
        return f'Estado atual da conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)  # Para garantir que não haja depósito negativo.
        self.__saldo += valor
        print(f'Depósito de US$ {valor:,.2f} realizado com sucesso na conta {self.id}')

    def sacar(self, valor):
        valor = abs(valor)  # Para garantir que não haja saque negativo.
        if valor > self.__saldo:
            print(f'Saque de US$ {valor:,.2f} NÃO AUTORIZADO (__saldo insuficiente):'
                  f' Conta {self.id} >> __saldo atual US$ {self.__saldo:,.2f}')
        else:
            self.__saldo -= valor
            print(f'Saque de US$ {valor:,.2f} autorizado na conta {self.id}')
