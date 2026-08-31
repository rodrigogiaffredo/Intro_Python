# ABSTRAÇÃO

# Abstração também é um dos pilares da POO. Sua definição clássica é 'a prática de ignorar
# o irrelevante e manter o foco estritamente no essencial.'

# Exemplo de aula: pensando num controle remoto, para utilizar bem precisamos conhecer só
# a interface (botões de volume, canal, menu, liga/desliga, etc.), sendo desnecessário para
# o seu bom uso conhecer o que está por trás da interface (placas e circuitos).

# O princípio base da ABSTRAÇÃO é que ela elimina a necessidade de se conhecer detalhes
# da implementação, liberando foco exclusivo para a interface pública que está disponível.

# Principais vantagens da ABSTRAÇÃO:

# - facilita a legibilidade (trabalhar com módulos por exemplo, deixa o código limpo)
# - padroniza (a relação superclasse / subclasse padroniza as operações do programa)
# - simplifica o código do programa principal
# - aumenta a segurança do código (por não expor os detalhes internos de funcionamento)

# Abstração de DADOS: acontece quando ignoramos informações desnecessárias para o escopo
# do projeto.

# Abstração de PROCESSOS: acontece quando não precisamos saber como um métodos faz seu
# trabalho, apenas saber que ele existe através da interface pública.



# CLASSE ABSTRATA

# É a superclasse que contém todos os métodos genéricos que afetarão as subclasses a ela
# associadas. No exemplo do controle remoto:

#                           CONTROLE GENÉRICO       (CLASSE ABSTRATA)
#                               ligar()
#                               desligar()
#                               aumentarvolume()    (MÉTODOS ABSTRATOS)
#                               diminuirvolume()
#                               avancarcanal()
#                               retrocedercanal()
#                                   ^
#                                  / \
#                                   |
#                                   |
# ---------------------------------------------------------------------------
#     |                 |               |               |               |
# CONTROLE 1        CONTROLE 2      CONTROLE 3      CONTROLE 4      CONTROLE5

# A classe ABSTRATA não tem objetos diretamente relacionados a ela. Seu papel é servir
# de base para subclasses, as quais essas sim terão objetos associados a elas.

# Os métodos abstratos da classe abstrata CONTROLE GENÉRICO obrigam todas as subclasses
# ligadas a ela a tê-los também.

# Na aula anterior sobre o pilar herança, o métodos associado à superclasse 'Pessoa'
# é o métodos abstrato ('fazer_aniversario()'), e ele obrigava todas as subclasses
# associadas ('Aluno', 'Professor', 'Funcionario') a herdá-lo. Portanto, a classe
# 'Pessoa' é uma classe ABSTRATA.

# Uma classe abstrata NUNCA SERÁ INSTANCIADA, pois será usada apenas como base para
# as subclasses.



# MÉTODOS CONCRETO E ABSTRATO

# As classes que efetivamente vão virar objetos são as subclasses (os diferentes controles,
# ou aluno/professor/funcionario), por isso elas são chamadas de classes especializadas.

# Todos os métodos definidos na classe ABSTRATA que são exatamente iguais em todas as
# classes especializadas vinculadas a ela são chamados de MÉTODOS CONCRETOS.

# Fazer aniversário no exemplo da aula anterior: é somar 1 à idade atual, não importando
# se a 'Pessoa' é 'Aluno', 'Professor' ou 'Funcionario'. O métodos funciona exatamente da
# mesma forma, portanto fazer_aniversario() é um MÉTODOS CONCRETO.

# No métodos CONCRETO, o código do métodos está DEFINIDO na classe ABSTRATA.

# Agora se criarmos um métodos estudar() na classe abstrata, ele pode variar dependendo
# de qual subclasse estiver olhando. Alunos estudam diferente de funcionários, professores
# também, enfim.

# Nesse caso, apesar de o métodos ser da classe mãe, o código não pode ser definido ali pois
# há diferenças importantes nas subclasses. É o mesmo que o controle remoto que tem botão
# liga/desliga porém cada controle liga um aparelho específico. A classe abstrata
# 'Controle Generico' obriga a existência do botão liga/desliga, mas não padroniza o
# código do métodos. Portanto, liga/desliga nesse caso é um métodos ABSTRATO.

# Sintaxe do métodos abstrato: estudar() {abstract}

# As classes abstratas poderão ter métodos abstratos obrigatórios para as subclasses, mas
# não é uma regra, e sim uma possibilidade.

# Classes abstratas podem também ter métodos concretos caso eles funcionem exatamente da
# mesma maneira para todas as subclasses (exemplo do 'fazer_aniversario()'), e aqui entra
# o famoso DRY ('Don't Repeat Yourself').


# INTERFACE PÚBLICA

# É o conjunto de MÉTODOS ABSTRATOS da classe.

# É justamente a parte do objeto com a qual interagimos, no exemplo do controle remoto é
# a parte dos botões. No computador as interfaces públicas são o teclado e a tela. No
# carro são o painel e os pedais.


# ABC E DRY

# ABC: é o módulo Abstract Base Classes, o qual fornece as funcionalidades
# necessárias à criação de classes abstratas no Python.

# DRY: Don't Repeat Yourself. Tudo que pode ser definido numa classe abstrata, deve ser
# definido nela. Isso reduz o risco de erros por digitação repetida massiva, mantém o
# código limpo, e facilita sua manutenção. Classes ABSTRATAS são ótimas candidatas à
# modularização.
