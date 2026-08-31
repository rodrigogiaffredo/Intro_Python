

# DECLARAÇÃO DE CLASSE (o molde)

class Pessoa:      # Por convenção, a primeira letra do nome da classe é maiúscula

    # métodos CONSTRUTOR
    def __init__(self):
        # atributos de INSTÂNCIA
        self.nome = ''   # >> Todos os atributos de instância começam com self.
        self.idade = 0   # >> Na execução do programa, 'self' é substituído pelos NOMES
        self.sexo = ''   # >> dos objetos que criarmos para essa classe (no meu exemplo,
                         # >> os nomes são 'p1' e 'p2' (ver abaixo).

    # métodos de INSTÂNCIA
    def aniversario(self):
        # No dia do aniversário, a idade aumenta em 1
        self.idade += 1
    def mensagem(self):
        # Uma mensagem qualquer, no caso a descrição da pessoa
        return f'Saiba que {self.nome} tem {self.idade} anos de idade.'


# DECLARAÇÃO DE OBJETOS

# Criando um OBJETO chamado 'p1' da CLASSE 'Pessoa'

p1 = Pessoa()         # Os parênteses () são a chamada ao métodos CONSTRUTOR
print(p1.mensagem())  # Nesse momento o atributo nome está em branco, e o atributo
                      # idade está 0

# Adicionando dados aos atributos de p1

p1.nome = 'Rodrigo'
p1.idade = 49
print(p1.mensagem()) # Aqui o atributo nome aparece como 'Rodrigo', e o atributo idade
                     # aparece como 49. Ou seja, o OBJETO 'p1' da CLASSE 'Pessoa' tem
                     # o ATRIBUTO 'nome' igual a Rodrigo, e o ATRIBUTO 'idade' igual a 49.

# DICA: SEM PARÊNTESES NO FINAL, ATRIBUTO; COM PARÊNTESES NO FINAL, MÉTODOS

# O MÉTODOS aniversário foi executado, portanto a idade aumentou em 1

p1.aniversario()
print(p1.mensagem())

# Criando outro objeto ('p2') e aplicando o métodos aniversário a ele também

p2 = Pessoa()
p2.nome = 'Bianca'
p2.idade = 48
print(p2.mensagem())
p2.aniversario()
print(p2.mensagem())

# O recurso self. do métodos CONSTRUTOR é o que garante que o objeto certo (o que chamou
# o MÉTODOS DE INSTÂNCIA) seja atualizado toda vez que um métodos de instância for chamado.

# Em resumo, criei um molde (CLASSE) chamado 'Pessoa', e a partir dele consegui criar
# dois OBJETOS ('p1' e 'p2'), cada um deles com os ATRIBUTOS 'nome' e 'idade', e passíveis
# da aplicação dos MÉTODOS DE INSTÂNCIA 'aniversario' e 'mensagem'.

# A partir de agora, consigo criar quantos OBJETOS eu precisar, usando a mesma CLASSE.

# DICA: AS DECLARAÇÕES DE CLASSE NÃO PRECISAM FICAR NO MESMO ARQUIVO DAS DECLARAÇÕES DE
# OBJETO, PODEMOS USAR O CONCEITO DE MODULARIZAÇÃO PARA ORGANIZAR O CÓDIGO CONFORME OS
# PROGRAMAS FICAM MAIORES.
