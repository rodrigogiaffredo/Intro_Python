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

from credencial import *

def main():
    c = Credencial()
    # Criação da senha
    c.senha = 'DmK!@'
    # Após a criação da senha, tudo que se refere a ela é apresentado em formato hash
    print(c.senha)
    # Tentando validar uma senha incorreta via comparação entre as hashs, configurada no
    # métodos 'validar' do arquivo credencial.py
    c.validar('Teste123')
    # Tentando validar a senha correta via comparação entre as hashs, configurada no
    # métodos 'validar' do arquivo credencial.py
    c.validar('DmK!@')
    # Entrada de senha por input com posterior validação
    c.senha = str(input('Digite a senha: '))
    print(c.senha)
    c.validar('DmK!@')


if __name__ == '__main__':
    main()
