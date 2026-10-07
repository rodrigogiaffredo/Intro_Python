
# Implementar a seguinte estrutura com agregação, incluindo sobrecarga do operador '+' para 
# adicionar produtos ao carrinho de compras.

# ------------
# Carrinho
# ------------
# + produtos[0..n]      //agregação
# + @total
# ------------
# ------------
#     /\
#     \/
#     |
#     |
# ------------
# Produto
# ------------
# + nome 
# + preco
# ------------
# ------------


from carrinho import *


def main():
    
    p1 = Produto('Notebook', 8_500)
    p2 = Produto('Mouse', 250)
    p3 = Produto('Fone de Ouvido', 450.35)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1
    c1 = c1 + p2
    c1 = c1 + p3
    print(c1)


    c2 = c2 + p2
    print(c2)

    c2 = c2 + c1
    print(c2)


if __name__ == '__main__':
    main()

