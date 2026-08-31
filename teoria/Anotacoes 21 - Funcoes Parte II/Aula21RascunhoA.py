# Interactive Help, docstrings para documentação de funções, argumentos opcionais, escopo
# de variáveis, e retorno de resultados.

# INTERACTIVE HELP

# É o aparato de ajuda que a linguagem oferece, e no Python esse aparato
# é chamado através da função interna 'help()', no PYTHON CONSOLE.

# Lá, quando digito help(), ele já muda o prompt para help, e a partir daí basta digitar
# qualquer comando, função, métodointerno, etc. e consigo acessar um manual completo sobre
# aquele determinado tópico. Por exemplo, se digito 'print', ele explica o que há para se
# saber sobre ele.

# Fora isso, aqui mesmo no interpreter dá para acessar o interactive help também, sem ter
# que ir para o console. Basta digitar help('string') por exemplo, e executar o "programa"
# para ter acesso à ajuda completa sobre 'string' no caso.

# DOCSTRINGS

# Docstring é uma string de documentação. Toda funcionalidade interna do Python tem sua
# docstring, e as funções que nós criamos também podem ter suas docstrings.

# Para isso basta abrir aspas duplas 3 vezes logo após a linha 'def' da função criada, e
# digitar informações que ajudem o usuário a entender o que sua função faz. A partir daí,
# ela também será acessível através do 'help('suafuncao')'.


# Exemplo:

# def contador(i, f, p)
#   """
#   --> Faz uma contagem e mostra na tela.
#   ; param i: início da contagem
#   ; param f: fim da contagem
#   ; param p: passo da contagem
#   ; return: sem retorno
#   ; Função criada por Fulano de Tal em data tal
#   """
#   c = i
#   while c <= f
#       print(f'(c)', end = '..')
#       c += p
#   print('-- fim --')

# Ou seja, a partir de agora, se eu digitar help('contador'), terei acesso ao help da função
# que acabei de criar.


# PARÂMETROS OPCIONAIS

# Imaginando a função abaixo:
# def somar(a, b, c):
#   s = a + b + c
#   print(f'A soma vale {s}')

# Caso passemos os valores somar(3, 2, 5), a função seria executada normalmente já que
# ela exige 3 parâmetros, e passamos os 3. Porém se eu passasse os valores somar(8, 4)
# haveria o retorno de um erro, pois a função exige 3 parâmetros, e passei apenas 2.

# Para isso existe a possibilidade de definirmos PARÂMETROS OPCIONAIS, e no caso da minha
# recém-criada função 'somar', basta fazer com que 'c' receba 0 caso o parâmetro não seja
# passado no programa principal.

# Ficaria assim: def somar(a, b, c=0)

# Portanto, o 'c' passou a ser nosso parâmetro opcional. Aliás, se necessário poderia colocar
# todos os parâmetros como opcionais:

# def somar(a=0, b=0, c=0) --> útil por exemplo para os casos somar()

# No entanto, se eu informar 4 ou mais valores, aí sim a função dará erro pois eu a defini
# com 3 parâmetros (ainda que opcionais). Justamente aqui entra a funcionalidade de
# encapsulamento e desencapsulamento, vista na aula anterior.


# ESCOPO DE VARIÁVEIS

# É o local onde a variável vai existir, e deixar de existir, ao longo do programa.

# Variáveis com escopo GLOBAL: funcionam tanto no programa principal, quanto na definição
# da função. Essas variáveis devem ser declaradas no corpo do programa principal, pois
# quando declaradas dentro da função, passam a ser variáveis de escopo local.
# No exemplo abaixo, a variável 'n' se aplica tanto ao programa principal, quanto
# à função teste(), pois foi declarada no corpo do programa principal.

# def teste():
#   print(f'No escopo da função, n vale {n}.')

# Programa principal
# n = 2
# print(f'No programa principal, n vale {n}.')

# Ambas as frases serão impressas com 'n' valendo 2.

# Já neste outro exemplo, a variável 'x' tem escopo LOCAL pois foi declarada no corpo da
# função teste(), ficando portanto restrita a ela. Se chamarmos a variável 'x' diretamente
# (sem passar pela função) no programa principal, ocorrerá um erro.

# def teste()
#   x = 3
#   print(f'No escopo local, x vale {x}.')

# Programa principal
# print(f'No programa principal, x vale {x}.') - RETORNARÁ UM ERRO

# teste() - FUNCIONARÁ NORMALMENTE

# IMPORTANTE: É POSSÍVEL INFORMAR NA FUNÇÃO QUE NÃO QUEREMOS A SUBSTIUÇÃO DE UMA VARIÁVEL
# GLOBAL POR OUTRA LOCAL.

# No cenário abaixo:

# def teste(b):
#   a = 8
#   b += 4
#   c = 2
#   print(f'a dentro vale {a}.')
#   print(f'b dentro vale {b}.')
#   princ(f'c dentro vale {c}.')

# Programa principal
# a = 5
# print(f'a fora vale {a}.')

# A impressão do programa principal resultaria em a = 5 pois a variável global prevalece.
# Porém, ao executar a função 'teste()', seria impresso a = 8.

# A não ser que incluíssemos um aviso para o Python no escopo da função, comunicando que
# ele não deve criar uma nova variável LOCAL 'a', mas sim substituir o valor da variável
# GLOBAL 'a' por aquilo que a função determinar.

# Ou seja:

# def teste(b):
#   global a     --> O AVISO
#   a = 8
#   b += 4
#   c = 2
#   print(f'a dentro vale {a}.')
#   print(f'b dentro vale {b}.')
#   princ(f'c dentro vale {c}.')

# Programa principal
# a = 5
# teste(a)
# print(f'a fora vale {a}.')

# Imprimirá 'a' = 8 mesmo que nós tenhamos dito no começo do programa que a = 5, pois
# demos uma autorização para a função através de 'global a' para substituir o conteúdo
# da variável global 'a' pelo que a função determinar.

# E ao imprimirmos a função no corpo do programa principal, teríamos as seguintes respostas:

# 'a' dentro vale 8. (substituindo o 5 mencionado na variável global, pois autorizamos)
# 'b' dentro vale 9. (5 + 4, ou seja, preservou o primeiro 5 da variável global)
# 'c' dentro vale 2. (porque não associamos a variável local 'c' à variável global 'a')

# A mesma ideia de aplica a IMPORTAÇÃO DE BIBLIOTECAS. Podemos importar bibliotecas e
# mantê-las com escopo global (caso importemos no corpo do programa principal), ou com
# escopo local, caso as importemos no corpo da função.


# RETORNO DE VALORES

# Muito úteis quando precisamos PERSONALIZAR a apresentação dos resultados no programa
# principal.
# As funções em Python podem ou não retornar valores dentro delas. Caso eu queira retornar
# um valor DENTRO de uma função, devo usar a palavra reservada 'return'.

# def somar(a=0, b=0, c=0)   --> Variáveis opcionais
#   s = a + b + c
#   return s

# r1 = somar(3, 2, 5)
# r2 = somar(1, 7)
# r3 = (4)
# print(somar(7, 11, 3))


# IMPORTANTE: return não serve apenas para números. Podemos retornar valores lógicos (True
# or False), listas, dicionários, tuplas...

# Isso faz com que o resultado da soma, calculado na função (e não no corpo do programa
# principal), preencha variáveis (no exemplo as variáveis r1, r2 e r3 respectivamente)
# ou mostrar diretamente o resultado da soma num print caso eu opte por essa ação - abrindo
# a possibilidade de formatar, agrupar resultados em linha, etc.
