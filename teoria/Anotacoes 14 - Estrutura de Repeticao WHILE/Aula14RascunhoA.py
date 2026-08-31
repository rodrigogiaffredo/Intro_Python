# Enquanto a estrutura de repetição FOR trabalha com um limite conhecido e pré-definido, a
# estrutura de repetição WHILE é ideal para situações em que uma ação deva ocorrer até que
# uma determinada condição seja atendida, sendo que não sabemos exatamente quando isso vai
# ocorrer. É o que chamamos de estrutura de repetição com teste lógico.

# A escolha entre usar FOR e WHILE é do programador, mas na aula vamos exercitar WHILE apenas.

# Sintaxe genérica: enquanto [condição] faça

# Sintaxe Python: while [condição] faça

# A grande beleza da estrutura de repetição com teste lógico é o aninhamento de condições.
# Por exemplo, um personagem segue por um caminho cheio de buracos e moedas, e deve chegar
# até uma maçã. O ciclo será repetido tantas vezes quantas necessárias até chegar na maçã.

# while not maçã: (não sei quantos passos são, mas sei meu objetivo)
#   if chão:
#       ande
#   if buraco:
#       pule
#   if moeda:
#       pegue (dentro do if, é a moeda)
# pegue (fora do if, é a maçã lá do while)
# fim

