# Encapsulamento é um dos pilares da POO, o qual visa manter a integridade do sistema,
# protegendo o estado interno do objeto contra inteferência externa não regulamentada.


from RascunhoB import *
from rich import print, inspect


def main():
    av1 = Avaliacao('Creitin', 'Punhetologia', 9.75)
    # Ao tentar mudar para 11, o sistema retornará 'Nota Inválida' e manterá 9.75
    av1.set_nota(11)
    # Nesse exemplo, 'nome' e 'disciplina' são atributos públicos (sem o '_') e o
    # atributo '_nota' é protegido (com o '_').
    print(f'Nota atual de {av1.nome} em {av1.disciplina}: {av1.get_nota()}')
    # 'private=True' mostra os dados privados na inspeção
    inspect(av1, private=True)


if __name__ == '__main__':
    main()
