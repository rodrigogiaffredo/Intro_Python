# Encapsulamento é um dos pilares da POO, o qual visa manter a integridade do sistema,
# protegendo o estado interno do objeto contra inteferência externa não regulamentada.


from RascunhoC import *
from rich import print, inspect


def main():
    av1 = Avaliacao('Creitin', 'Punhetologia')
    # Atualizando direto o atributo getter passível de validação 'nota' (sem parênteses
    # e sem '_' pois não se trata de um métodos e sim de um atributo).
    # Portanto, quando válida, a nota será alterada na variável protegida, passando de
    # 0 (padrão na def do arquivo RascunhoC) para 7.8 no caso desse exemplo.
    av1.nota = 7.8
    print()
    print(f'Nota atual de {av1.nome} em {av1.disciplina}: {av1.nota}')
    print()
    # No inspect, vemos o atributo 'nota' dando acesso ao atributo protegido '_nota'.
    inspect(av1, private=True)


if __name__ == '__main__':
    main()
