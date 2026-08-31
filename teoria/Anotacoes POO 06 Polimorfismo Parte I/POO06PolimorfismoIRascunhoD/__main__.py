# Polimorfismo de INCLUSÃO usando família como exemplo

# Mãe e filhos (um menino e uma menina)


from familia import *


def main():
    p1= Mae('Jaciara')
    p2 = Filho('Matheus')
    p3 = Filha('Monica')

    # A SUPERCLASSE define métodos para fazer pudim e fritar coxinha
    p1.fazer_pudim()
    p1.fritar_coxinha()

    p2.fazer_pudim()
    # Override: a SUBCLASSE 'Filho' tem seu próprio método para fritar coxinha; o resto ela herda da
    # SUPERCLASSE.
    p2.fritar_coxinha()

    # Override: a SUBCLASSE 'Filha' tem seu próprio método para fazer pudim; o resto ela herda da 
    # SUPERCLASSE.
    p3.fazer_pudim()
    p3.fritar_coxinha()



if __name__ == '__main__':
    main()

