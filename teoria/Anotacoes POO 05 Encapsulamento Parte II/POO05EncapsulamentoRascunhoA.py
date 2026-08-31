# Encapsulamento é um dos pilares da POO, o qual visa manter a integridade do sistema,
# protegendo o estado interno do objeto contra inteferência externa não regulamentada.


# ACESSO A DADOS ENCAPSULADOS

# Existem duas formas de acessar dados encapsulados:

# - Através dos métodos acessores (getters & setters)
# - Através do uso do decorador @property




# MÉTODOS ACESSORES (GETTERS & SETTERS) - mais tradicional

# Métodos ACESSORES são aqueles que acessam os dados de maneira segura para evitar
# quebras, presentes em POO de qualquer linguagem.

# Setter: espécie de validador do dado passado ao atributo.
# Getter: retorna o valor validado do atributo.

# Exemplo: na SUPERCLASSE Avaliacao, temos os atributos públicos 'nome' e 'disciplina',
# e o atributo protegido '_nota'. Notas seguem critérios (não podem ser negativas, não
# podem ser maiores que a pontuação máxima, não podem ser negativas, etc.), então podemos
# ter o métodos público setter 'set_nota(valor)' e o métodos público getter 'get_nota()'.

# SUPERCLASSE
# Avaliacao

# ATRIBUTOS
# + nome
# + disciplina
# _nota

# MÉTODOS
# + set_nota(valor)
# + get_nota()

# Programa principal:

# main
# a = Avaliacao()
# a.nome = 'Creitin'
# a.disciplina = 'Ciências Sociais'
# a.set_nota(2.4)



# DECORADOR @PROPERTY - mais moderno

# O decorador @property cria atributos que são passíveis de validação no Python. Mais
# elegante pois permite mexer diretamente no atributo, sem a necessidade de utilizar
# métodos (getters ou setters).

# No exemplo da SUPERCLASSE Avaliacao, temos os atributos públicos 'nome' e 'disciplina'
# e o atributo protegido '_nota' seguido de dois outros atributos públicos decorados,
# '@nota.getter' e '@nota.setter'.

# SUPERCLASSE
# Avaliacao

# ATRIBUTOS
# + nome
# + disciplina
# # _nota
# + @nota.getter
# + @nota.setter

# Programa Principal

# a = Avaliacao()
# a.nome = 'Creitin'
# a.disciplina = 'Sociologia'
# a.nota = 3.2
