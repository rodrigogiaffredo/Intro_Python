
# Implemente um sistema de mensagens padronizadas usando orientação a objetos.

# SUPERCLASSE
# -----------
# Mensagem
# -----------
# # mensagem
# # tipo
# # icone
# -----------
# + mostrar()
# -----------

# SUBCLASSES

# ----------
# Erro
# ----------
# ----------

# ----------
# Aviso
# ----------
# ----------


from alertas import *


def main():

    # Jeito clássico de mostrar as mensagens 
    
    m1 = Mensagem('Olá Mundo')
    m1.mostrar()

    m2 = Alerta('Cuidado!')
    m2.mostrar()

    m3 = Erro('Falhou...')
    m3.mostrar()

    # Outro jeito de mostrar as mensagens

    Mensagem('Outro jeito').mostrar()
    Alerta('Escolhe!').mostrar()
    Erro('Oh noh...').mostrar()


if __name__ == '__main__':
    main()