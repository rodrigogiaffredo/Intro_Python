# Criar uma classe que represente um retângulo pelas suas medidas e área. O diagrama da
# SUPERCLASSE Retangulo é:
# SUPERCLASSE
# Retangulo
# ATRIBUTOS
# # # _base
# # # _altura
# # # _área
# # + @base
# # + @altura
# # + @medidas
# # + @area

class Retangulo:

    def __init__(self, base = 1, altura = 1):
        # Declaração dos ATRIBUTOS da instância
        self._base = None
        self._altura = None
        self._area = None
        # Atribuição dos valores passados por parâmetro, sabendo que base e altura são parâmetros
        # personalizáveis e validados (via getters e setters).
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError('Para a base é obrigatório digitar um número')
        if valor < 0:
            raise ValueError('Números negativos não são permitidos na definição da base')
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError('Digite apenas números positivos')
        if valor < 0:
            raise ValueError('Digite apenas números positivos')
        else:
            self._altura = valor

    @property
    def area(self):
        self._area = self.base * self.altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError('Erro: o sistema não permite definir a área manualmente')

    @property
    def medidas(self):
        return f'Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}'

    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError('Informar as medidas dentro dos parênteses')
        if len(valores) != 2:
            raise SyntaxError('Informar dois valores númericos')
        if isinstance(valores[0], float) or isinstance(valores[0], int):
            self.base = valores[0]
        else:
            raise TypeError('Informar valor numérico válido para a base')
        if isinstance(valores[1], float) or isinstance(valores[1], int):
            self.altura = valores[1]
        else:
            raise TypeError('Informar valor numérico válido para a altura')
