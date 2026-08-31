# Definição de classe
class Contabancaria:
    """
    A classe 'Contabancaria' cria uma conta bancária, permitindo saques e depósitos.
    """
    # Métodos CONSTRUTOR
    def __init__(self, id, titular, saldo = 0):
        # Atributos de instância
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print()
        print(f'Conta {id} criada com sucesso. Saldo atual: US$ {self.saldo:,.2f}')

    # Métodos de instância
    def __str__(self):
        return f'Saldo atual da conta {self.id}: US$ {self.saldo:,.2f}'

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de US$ {valor:,.2f} realizado com sucesso na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque de US$ {valor:,.2f} NÃO AUTORIZADO (saldo insuficiente):'
                  f' Conta {self.id} >> US$ {self.saldo:,.2f}')
        else:
            self.saldo -= valor
            print(f'Saque de US$ {valor:,.2f} autorizado na conta {self.id}')



# Definição de objeto
conta1 = Contabancaria(512, 'Rodrigo', 2000000)
print(conta1.__doc__)
print()
conta1.sacar(50_000)
conta1.depositar(150_000)
conta1.sacar(3_500_000)
print(conta1)
