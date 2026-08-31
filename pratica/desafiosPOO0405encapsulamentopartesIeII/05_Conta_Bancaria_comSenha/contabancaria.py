# Aprimorar o exercício da ContaBancaria aplicando conceitos de encapsulamento. O diagrama da
# SUPERCLASSE ContaBancaria é:
# SUPERCLASSE
# ContaBancaria
# ATRIBUTOS
# # # _id
# # # _titular
# # - __saldo
# # - __hash
# # + @nome
# MÉTODOS
# # + validar senha(chave)
# # + pede senha()
# # + sacar(valor, chave)
# # + depositar(valor)

from hashlib import sha256


class Contabancaria:
    """
    A classe 'Contabancaria' cria uma conta bancária, permitindo saques e depósitos.
    """

    def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:str = None):
        # Atributos de instância
        # Botão direito sobre 'id', rename / current file para inserir o '_' em todas
        # as ocorrências de uma vez só
        self._id = id # protegido (#)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado ('-')
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print()
        print(f'Conta {id} criada com sucesso. Saldo atual: US$ {self.__saldo:,.2f}')

    def pede_senha(self) -> str:
        # Criação de senha com 6 ou mais dígitos

        # Usando a biblioteca 'pwinput' para dar o efeito asterisco na digitação da senha
        # 'pwinput' = password input
        # Importando no escopo local propositalmente

        from pwinput import pwinput

        while True:
            senha = str(pwinput('Senha: ')).strip()
            if len(senha) >= 6:
                break

        return senha


    def validar_senha(self, chave:str):
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        return (f'Saldo atual da conta {self._id} em nome de {self._titular}: '
                f'US$ {self.__saldo:,.2f}')
        #return f'Estado atual da conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)  # Para garantir que não haja depósito negativo.
        self.__saldo += valor
        print(f'Depósito de US$ {valor:,.2f} realizado com sucesso na conta {self._id}')

    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)  # Para garantir que não haja saque negativo.

        # Aumentando a segurança do saque, agora pedindo senha
        if chave is None:
            chave = self.pede_senha()

        # O saque somente será aceito se a senha for validada
        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'Saque de US$ {valor:,.2f} NÃO AUTORIZADO (__saldo insuficiente):'
                      f' Conta {self._id} >> __saldo atual US$ {self.__saldo:,.2f}')
            else:
                self.__saldo -= valor
                print(f'Saque de US$ {valor:,.2f} autorizado na conta {self._id}')
        else:
            print(f'Senha incorreta. Saque não efetuado.')


    # Alterando o nome do titular com camada de validação
    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome:str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            # Exigindo tamanho mínimo no campo 'novonome'
            if len(novonome) >= 5:
                self._titular = novonome
        else:
            print('Senha incorreta. Alteração de nome não efetuada.')
