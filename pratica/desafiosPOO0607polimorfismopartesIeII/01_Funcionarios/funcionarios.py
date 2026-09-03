

# Criar a seguinte estrutura de classes para calular bônus salarial, aplicando 10% para 
# desenvolvedor, 15% para gerente, e 8% para designer:


# SUPERCLASSE
# --------------------
# Funcionário (abrstract)
# --------------------
# + nome
# - salario
# --------------------
# + calcular_bonus()
# --------------------

# SUBCLASSES
# --------------------      ------------------------        -----------------------
# Gerente                   Designer                        Desenvolvedor
# --------------------      ------------------------        -----------------------
# --------------------      ------------------------        -----------------------
#                                                           
# --------------------      ------------------------        -----------------------

from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome:str = None, salario:float = 1_621):
        self.nome = nome
        self.__salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor:float = None):
        if valor is None:
            raise ValueError("É mandatório informar um valor positivo.")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("Redução de salário não autorizada no sistema.")


    def __str__(self):
        return f'{self.nome} é {self.__class__.__name__}, ganha R$ {self.salario:,.2f} e seu bônus será de R$ {self.calcular_bonus():,.2f}.'


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10


class Designer(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.08


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15


