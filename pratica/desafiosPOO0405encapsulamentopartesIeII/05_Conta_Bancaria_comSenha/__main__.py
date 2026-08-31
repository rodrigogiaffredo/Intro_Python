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

from contabancaria import *

def main():

    # Se a senha ('chave') não for definida na tupla, ele vai pedir para criar uma por causa do
    # métodos 'pede_senha' criado no arquivo contabancaria.py.
    cc = Contabancaria(111, 'Marquin', 1_000_000)

    # Se a senha ('chave') for definida na tupla, ele não vai pedir para criar uma.
    cc = Contabancaria(110, 'Julieta', 2_000_000, 'senhanova')

    # E se imprimirmos os dados da conta, a senha não vai aparecer, mas sim o hash por causa
    # da proteção que criamos no arquivo 'contabancaria.py'
    print(cc)

    cc = Contabancaria(999, 'Creitin', 1000)
    print()
    print('Tentativa de saque')
    # Ao tentarmos sacar, se errarmos a senha, o programa encerra sem concluir a operação.
    cc.sacar(500)
    print()
    print('Tentativa de mudança de nome')
    # Mudança de nome protegida com senha
    cc.nome = 'Maricledson'
    print(cc)


if __name__ == '__main__':
    main()
