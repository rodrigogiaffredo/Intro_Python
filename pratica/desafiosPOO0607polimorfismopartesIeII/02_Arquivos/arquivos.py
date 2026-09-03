



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

from abc import ABC, abstractmethod


class Arquivo(ABC):
    def __init__(self, nome:str, ext:str, tam:int = 0):
        self.nome = nome
        # O atributo 'extensao' é protegido
        self._extensao = None
        self.tamanho = tam
        self.extensao = ext


    @abstractmethod
    def abrir(self):
        pass

    # Property e setter do atributo protegido 'extensao'
    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf', 'doc', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError('Arquivo em formato não suportado.')


    @property
    def nome_completo(self):
        return f'"{self.nome}.{self.extensao}" ({self.tamanho / 1_000_000}MB)'



class PDF(Arquivo):
    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'pdf', tam)

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} no Adobe Acrobat Reader.')


class DOC(Arquivo):
    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'docx', tam)

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} no Microsoft Word.')



# Posso também usar o ducktyping para chamar o método 'abrir()'
def abrir_arquivo(arquivo):
    arquivo.abrir()








