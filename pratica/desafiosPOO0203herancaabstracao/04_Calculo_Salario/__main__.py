# Criar uma estrutura capaz de calcular salários de funcionários diferentes. SUPERCLASSE
# Funcionário {abstract} com atributos nome, sal_bruto, salario, sal_min=1612, inss=7.5 e
# MÉTODOS calc_sal() {abstract} e analisar sal(). SUBCLASSES Horista atributos valor_hora
# e horas_trab e MÉTODOS calc_sal() e Mensalista MÉTODOS calc_sal().

from funcionarios import *
from rich import inspect

def main():

    f1 = FuncionarioHorista('Paulo', 45, 211)
    f1.calcular_salario()
    f1.analisar_salario()
    # inspect(f1)


    f2 = FuncionarioMensalista('Amanda', 9500)
    f2.calcular_salario()
    f2.analisar_salario()


if __name__ == '__main__':
    main()
