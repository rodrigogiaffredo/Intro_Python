# Implementar um termostato orientado a objetos. Mínimo de 16o.C, máximo de 30o.C, quando liga
# fica em 24o.C e quando gira a temperatura varia de 0.5 em 0.5o.C. O diagrama de classes da
# SUPERCLASSE Termostato é:

# SUPERCLASSE
# Termostato
# ATRIBUTOS
# # - __temperatura (privado)
# # + @temperatura (validável, limita mínima e máxima e só permite variações inteiras ou de 0.5 em 0.5)
# # + @ftemperatura (validável, retorna temperatura formatada em o.C)

class Termostato:
    def __init__(self):
        # Temperatura ao ligar 24
        self.__temperatura = 24

    @property
    # Getter temperatura sem formatação
    def temperatura(self):
        return self.__temperatura

    @property
    # Getter temperatura formatada
    def ftemperatura(self):
        return f'{self.__temperatura}{chr(176)}C'

    @temperatura.setter
    def temperatura(self,valor):
        # Alterações de temperatura autorizadas somente de 0.5 em 0.5
        if valor % 0.5 != 0:
            raise ValueError(f'Temperatura de {valor}{chr(176)}C é inválida.')
        # Temperatura mínima de 16
        if valor < 16:
            self.__temperatura = 16
        # Temperatura máxima de 30
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor
