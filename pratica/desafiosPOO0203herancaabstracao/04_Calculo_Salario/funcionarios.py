# Criar uma estrutura capaz de calcular salários de funcionários diferentes. SUPERCLASSE
# Funcionário {abstract} com atributos nome, sal_bruto, salario, sal_min=1612, inss=7.5 e
# MÉTODOS calc_sal() {abstract} e analisar sal(). SUBCLASSES Horista atributos valor_hora
# e horas_trab e MÉTODOS calc_sal() e Mensalista MÉTODOS calc_sal().

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):

    salario_minimo = 1612
    desconto_inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        base = self.salario / Funcionario.salario_minimo

        # Mostrando também o nome da classe para informar o tipo de funcionário
        mensagem = (f'O salário de {self.nome} ({self.__class__.__name__}) é de '
                    f'R$ {self.salario:,.2f} correspondentes a {base:.1f} salários mínimos.')
        painel = Panel(mensagem, title='Análise de Salário', width=50)
        print(painel)


class FuncionarioHorista(Funcionario):

    # R$ 7.37 é o valor hora pago referente a um salário mínimo mensal
    def __init__(self, nome, valor_hora = 7.37, qtd_horas = 220):
        # Recebe o 'nome' da SUPERCLASSE
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_horas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas

    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.desconto_inss / 100)



class FuncionarioMensalista(Funcionario):

    # Se não atribuir salário, vale o salário mínimo
    def __init__(self, nome, salario_bruto = Funcionario.salario_minimo):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.desconto_inss / 100)
