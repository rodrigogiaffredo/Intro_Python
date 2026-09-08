
# Criar um simulador que gerencie pagamentos de diferentes tipos, conforme o diagrama de classes
# abaixo:

# SUPERCLASSE

# Pagamento (abstract)
# --------------------
# # valor
# @fvalor
# --------------------
# pagar()

# SUBCLASSES

# Boleto
# --------------------
# --------------------

# CartaoCredito
# --------------------
# --------------------

# Pix
# --------------------
# --------------------


from pagamentos import *


def main():

    p1 = Pix()
    p1.valor = 2_838_523.85
    # Chamando o método 'fvalor' para validar se a formatação do valor funcionou
    print(p1.fvalor)

    # Chamando o método de pagamento, mas como está com 'return' na classe 'Pagamentos' a confirmação
    # do pagamento só será retornada quando usarmos o método 'finalizar_compra' abaixo, devido ao
    # polimorfismo
    p2 = Boleto()
    p2.pagar(2_800)
    

    # Chamando o método polimórfico direto, para não precisar criar objeto
    finalizar_compra(CartaoCredito(), 29_844_777.62)
    finalizar_compra(Boleto(), 2800)
    finalizar_compra(Pix(), 0.01)





if __name__ == "__main__":
    main()
