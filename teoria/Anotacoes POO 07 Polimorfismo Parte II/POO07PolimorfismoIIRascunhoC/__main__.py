
# Sobrecarga de OPERADOR: manipulação do funcionamento de operadores de acordo com a necessidade do
#                         programador.


from carteira import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(100)

    # Por ter definido um dunder method de sobrecarga de operador, agora quando testo se são iguais
    # não se trata mais de comparar objetos, mas sim de realizar uma operação (no caso a verificação de
    # igualdade). Substituí a funcionalidade padrão de igualdade, por uma comparação de saldos.
    
    # Comparação antes de mexer na carteira:
    print(c1 == c2)

    # O mesmo para adição de valores na carteira
    c1 += 50

    # O mesmo para retirada de valores da carteira
    c2 -= 30

    # O mesmo para comparações que envolvam os operadores para as quais haja um dunder method de 
    # sobrecarga de operador definido:

    if (c1 == c2):
        print('Carteiras com valores iguais.')
    else:
        print('Carteiras com valores diferentes.')

    # O mesmo para comparações 'menor ou igual' (optei pela escrita simplificada do comando 'if')
    print('A segunda carteira tem mais dinheiro.') if c1 <= c2 else print('A primeira carteira tem ' \
    'mais dinheiro')

    print(c1)
    print(c2)

    

if __name__ == '__main__':
    main()