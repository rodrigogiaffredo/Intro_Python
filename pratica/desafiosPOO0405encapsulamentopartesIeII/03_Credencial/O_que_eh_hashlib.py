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

# Usando texto acentuado para percebeu o efeito b-string
texto = 'Especulação'
# Criando a 'b-string' (codificação em formato binário) do texto no padrão utf-8
# Necessário para criação de hash, já que o padrão não aceita acentuação
cod = texto.encode('utf-8')
print(cod)
# Criptografando no modelo SHA256 (evitar SH1 e MD5, já foram decifrado)
# Preparando para impressão em formato hexadecimal via '.hexdigest()'
hash = sha256(cod).hexdigest()
print(hash)


# Em cadastros que exijam nome e senha, os servidores sérios nunca armazenam senhas. Armazenam
# as hashs de similaridades das senhas, ou seja, ainda que a criptografia seja decifrada, não
# será possível chegar à senha.

# Servidores menos bem elaborados ainda utilizam SHA1 ou MD5 os quais já foram decifrados,
# tornando a criptografia das senhas fáceis de decifrar.

# Portanto, sempre que tiver que armazenar senha, escolher o modelo mais moderno e seguro possível
# entre os disponíveis para criptografia, e armazenar somente a hash, nunca a senha.

# Quando o usuário digitar a senha, o sistema deve testar se a hash daquilo que o usuário digitou
# bate com a hash daquilo que está cadastrado no banco de dados.

# Se eventualmente o banco de dados vazar, não há problema pois as senhas foram criadas usando
# modelos fortes de criptografia, e o que vai ser publicado são hashs, não senhas.



