# Criar uma classe que gerencie a hash SHA256 de uma senha. O diagrama da SUPERCLASSE Credencial é:
# SUPERCLASSE
# Credencial
# ATRIBUTOS
# # - __hash_senha
# MÉTODOS
# # + validar(senha)

# Hash = bagunça (nome usado para criptografia)
# SHA = Secure Hash Algorithm (a versão 256 é a mais segura atualmente)
# NSA = National Security Agency (criadora do SHA)

from hashlib import sha256

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        # Verificando se o campo não está vazio
        if len(chave) > 0:
            # Vide arquivo explicando_hash para mais detalhes
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Senha inválida')

    def validar(self, chave):
        # Para validar, tenho que converter o que o usuário digitou para SHA256 etc. e fazer
        # a comparação do resultado com o que está gravado no banco de dados, já que o banco não
        # grava a senha, mas sim a hash da senha.
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print('Senha correta')
            return True
        else:
            print('Senha incorreta')
            return False
