
# Sobrecarga de MÉTODO: o mesmo nome de método, mas com parâmetros diferentes os quais fazem com que as
#                       tarefas executadas sejam diferentes. As assinaturas diferentes distinguem o 
#                       resultado da execução do método. No Python isso não é nativo, mas existe uma
#                       biblioteca chamada 'functools' a qual, quando importada, permite o overload
#                       de método.
#                       
#                       Exemplo:
#                       ----------------------
#                       SUPERCLASSE Analisador
#                       ----------------------
#                       ----------------------
#                       MÉTODOS
#                       analisar(int)
#                       analisar(float)
#                       analisar(str)
#                       analisar(bool)
#                       analisar(list)
#                       analisar(dict)
#                       ----------------------


from analisador import *

def main():
    x = Analisador()
    x.analisar([3, 5, 7])
    x.analisar('Python')
    x.analisar(9)
    x.analisar(299.6)
    x.analisar(None)
    x.analisar(max(23, 355.1, 14))
    x.analisar(len({'nome':'Creitin', 'idade':24}))

if __name__ == '__main__':
    main()

