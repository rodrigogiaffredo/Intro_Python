# PILARES DA POO

# - Encapsulamento: proteção de partes importantes do código
# - Herança: trata da hierarquia dos dados
# - Polimorfismo: variedade de formas de execução de atividades
# - Abstração: capacidade de simplificação e descarte de redundâncias

# HERANÇA

# Herança é um relacionamento entre itens gerais (ancestrais) e tipos mais específicos
# (descendentes) desses itens, que herdam ATRIBUTOS e MÉTODOS dos níveis superiores. É
# como herdar características e comportamentos dos pais. Assim como não há necessidade
# dos herdeiros serem exclusivamente cópias parciais dos pais, os itens descendentes
# podem ter seus próprios métodos e atributos, ideia que será aprofundada quando falarmos
# em especialização.

# Outros nomes do mecanismo de herança: GENERALIZAÇÃO, RELAÇÃO TIPO 'É UM'

# Vantagens: reutilização de código, organização hierárquica, facilidade na
# manutenção, extensibilidade (mexeu no nível mais alto, os níveis mais baixos são
# automaticamente beneficiados), suporte a polimorfismo.


# SUPERCLASSE & SUBCLASSE

# A representação gráfica de uma herança no diagrama de classes é uma seta vazada
# apontando para cima, que vai do descendente para o ancestral.

# Num diagrama de classes, a classe que está acima (na ponta da seta vazada) é chamada de
# SUPERCLASSE (ancestral). A de baixo, SUBCLASSE (descendente). É correto portanto dizer
# que a subclasse herda da superclasse. Outros nomes utilizados para a superclasse são
# classe base, ancestral, classe mãe. Outros nomes utilizados para a subclasse são classe
# derivada, descendente, classe filha.

# Exemplo:

# Num sistema com 3 objetos conforme abaixo

# ALUNO                     # PROFESSOR                     # FUNCIONARIO
# nome                      # nome                          # nome
# idade                     # idade                         # idade
# curso                     # especialidade                 # cargo
# turma                     # nível                         # setor
# fazer_aniversario()       # fazer_aniversario()           # fazer_aniversario()
# fazer_matricula()         # dar_aula()                    # bater_ponto()

# Percebo que os atributos nome e idade, e o métodos fazer_aniversario() são comuns
# aos 3 objetos. Ao invés de declará-los para cada objeto, poderia estabelecer uma
# relação de herança criando uma superclasse 'Pessoa', e a partir daí aluno, professor e
# funcionário herdarão de pessoa esses atributos e métodos, materializando a relação
# 'é um': aluno é um pessoa; professor é um pessoa; funcionário é um pessoa.

                            # PESSOA
                            # nome
                            # idade
                            # fazer_aniversario()

#                               ^
#                              / \
#                               |
# -----------------------------------------------------------------------
#   |                           |                               |
# ALUNO                     # PROFESSOR                     # FUNCIONARIO
# curso                     # especialidade                 # cargo
# turma                     # nível                         # setor
# fazer_matricula()         # dar_aula()                    # bater_ponto()



# GENERALIZAÇÃO & ESPECIALIZAÇÃO

# O exemplo anterior ilustra bem os conceitos de generalização e especialização, e facilita
# sua compreensão: os atributos e métodos da SUPERCLASSE 'Pessoa' representam a GENERALIZAÇÃO
# pois impactam os herdeiros em geral. Já os atributos e métodos das SUBCLASSES 'Aluno,
# Professor e Funcionario' representam a ESPECIALIZAÇÃO, pois são exclusivas a cada uma delas.
