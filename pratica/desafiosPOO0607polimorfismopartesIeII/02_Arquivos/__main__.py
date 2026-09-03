



# Criar um simulador que gerencia a abertura de diferentes tipos de
# arquivos.

# SUPERCLASSE
# --------------------
# Arquivo (abrstract)
# --------------------
# + nome
# # _extensao
# + tamanho
# @nome_completo
# --------------------
# + abrir()
# --------------------

# SUBCLASSES
# --------------------      ------------------------
# PDF                       DOC                
# --------------------      ------------------------
# --------------------      ------------------------
#                                                           
# --------------------      ------------------------



from arquivos import *

def main():
    # Aplico polimorfismo selecionando entre arquivos PDF e DOC
    a1 = DOC('Teste', 1_200_000)
    a1.abrir()

    a2 = PDF('Toste', 2_100_000)
    a2.abrir()

    # Abrindo através da versão criada com ducktyping
    abrir_arquivo(a1)
    abrir_arquivo(a2)
    

if __name__ == '__main__':
    main()