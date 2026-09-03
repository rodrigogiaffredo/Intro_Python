

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


from funcionarios import *

def main():

    # Polimorfismo: mudo os cargos (Gerente, Designer, Programador) e o sistema já calcula os 
    # bônus nos percentuais diferentes.
    f = Gerente('Pedro', 8_000)
    print(f)

    # Tento reduzir salário, e o sistema retorna o tratamento de erro definido no arquivo 
    # 'funcionarios.py' via Encapsulamento.
    try:
        f.salario = 2_000
    except Exception as e:
        print(f'ERRO: {e}')


    # É possível também criar uma lista polimórfica de funcionários, e percorrer cada um dos 
    # objetos internos com o uso do 'for'.
    funcionarios = [Desenvolvedor('Pedro', 18_000), 
                    Designer('José', 25_000), 
                    Gerente('Mariana', 45_000)]

    for f in funcionarios:
        print(f)



if __name__ == '__main__':
    main()
