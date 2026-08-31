# Simular um diário secreto orientado a objetos. O diagrama da SUPERCLASSE Diario é:
# SUPERCLASSE
# Diario
# ATRIBUTOS
# # - __segredos[]
# # - __ senha
# MÉTODOS
# # + escrever(msg)
# # + ler(msg)

class Diario:
    def __init__(self, senhamestra = 'BdZ!@'):
        # Lista pois exige dinamismo
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError('Sem senha, sem acesso.')
        else:
            print('Diário liberado, agora é por sua conta e risco:')
            for segredo in self.__segredos:
                print(f'- {segredo}')

    @property
    def senha(self):
        raise PermissionError(f'Visualização de senha não autorizada')
