# Encapsulamento é um dos pilares da POO, o qual visa manter a integridade do sistema,
# protegendo o estado interno do objeto contra inteferência externa não regulamentada.

# Voltando ao exemplo da conta bancária criado no RascunhoD na aula 06 (módulo rich).

from RascunhoB import *


def main():
    c1 = Contabancaria(111, 'Maria Mamamolto', 5000)
    c1.depositar(500)
    c1.sacar(100)
    # Pelo fato de o código ainda não estar encapsulado, posso cometer absurdos como por
    # exemplo depositar um valor negativo (o que teria o efeito de um saque)...
    # *** Atualização: incluímos a transformação em valor absoluto na função
    c1.depositar(-500)
    # ... ou sacar um valor negativo (o que teria o efeito de um depósito)...
    # *** Atualização: incluímos a transformação em valor absoluto na função
    c1.sacar(-300)
    # ... ou interagir diretamente com o saldo, sem passar por transações quaisquer.
    c1.saldo = 0

    # Interessante notar que após tranformar o atributo 'saldo' em privado ('__'), a
    # linha de comando 'c1.saldo = 0' não surtiu efeito em '_ContaBancaria__saldo' no
    # dicionário impresso, o qual passou a ter '__' associado a ele. Ao invés disso, ele
    # incluiu um item no dicionário chamado ''saldo': 0' sem o '__').
    # O mesmo acontece se eu tentar alterar o titular da conta através do programa
    # principal: não será possível pois se trata de um atributo com visibilidade protegida.
    c1.titular = 'Jão'
    # Ele cria um item no final do dicionário sem o '_' de protegido, e sem mudar o item
    # original do começo (esse sim com o '_' de protegido).
    print(c1)

    # MAS ATENÇÃO! Se no programa principal eu tivesse usado
    # c1.Contabancaria__saldo = 0 e c1.__titular = Jão, ele
    # teria aceito já que no Python a proibição segue uma convenção,
    # não há barreira hard nenhuma na estrutura da sintaxe.

    # Ou seja, como um programador 'adulto consentido', eu não
    # devo mexer diretamente em atributos com '_' ou '__', mesmo
    # que isso seja tecnicamente possível.

if __name__ == '__main__':
    main()
