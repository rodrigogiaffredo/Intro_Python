# P A C O T E S

# Quando os módulos se tornam tão robustos que sua gestão também começa a ficar inviável,
# passamos a utilizar os chamados PACOTES (equivalentes ao conceito de biblioteca em outras
# linguagens de programação).

# Na modularização, o objetivo é diminuir o código principal, e guardar o restante necessário
# dentro de um módulo (basicamente um arquivo.py que será importado no programa principal).

# E quando os módulos também ficam grandes demais, e começam a misturar assuntos por exmeplo,
# ou começam a demonstrar todas as desvantagens que os códigos principais demonstravam quando
# surgiu a necessidade de criação de módulos (dificuldade de ler e manter o código, etc.)
# quebramos o módulo em vários arquivos e agrupamos em pastas por assuntos, e isso é o que
# chamamos de PACOTES em Python.

# Longa-história-curta: PACOTE é um tipo de pasta que contém módulos.

# Vamos imaginar que ao invés de somente o arquivo chamado uteis22.py que criei para a
# aprendizagem de módulos, agora eu criasse o pacote 'muitouteis22' contendo vários outros
# arquivos, como por exemplo numbers.py, strings.py, dates.py, colors.py os quais
# são nada mais do que os recortes que já haviam num arquivo que se tornou tão imenso,
# que precisou virar um diretório de arquivos menores - ou um PACOTE com módulos.

# Para IMPORTAR o conteúdo de um pacote, basta  usar import - aqui no meu exemplo, se eu
# fizer import muitouteis22 agora, ao invés de apenas um módulo, será importado um pacote
# inteiro, que no caso contém 4 módulos (numbers22, strings22, dates22, colors22).

# Posso também importar somente certos módulos de dentro dos pacotes, usando o já
# conhecido from muitouteis22 import strings22, ou from uteis22 import colors22

# Portanto, posso ter pacotes dentro de pacotes. Caso por exemplo o arquivo colors22.py se
# tornasse tão imenso que precisasse virar um pacote, eu poderia ter a pasta
# colors22 dentro de muitouteis22, e dentro da pasta os módulos foreground22.py
# e background22.py por exemplo.

# Aliás, uma boa prática recomendada em Python é - mesmo que tenhamos apenas 1 arquivo
# num determinado subpacote - que criemos uma pasta específica para ele.

# Mas atenção: pacotes são úteis quando os projetos são realmente imensos. Normalmente é
# possível resolver questões cotidianas apenas com diferentes módulos.

# Existe uma sintaxe específica para nomes de arquivos dentro de PACOTES:

# Inclusive um arquivo em especial estará em cada uma das pastas contidas nos pacotes:
# __init__.py (no Pycharm esse arquivo é criado automaticamente, mas em outras IDEs é
# possível que tenha que criar manualmente).

# Na hora de exercitar a parte prática da aula, criei por exemplo um pacote chamado
# 'muitouteis22' para não ter que apagar o arquivo (módulo) uteis22.py que criei para
# o estudo de módulos.

# CRIANDO PACOTES NO PYCHARM: botão direito / new / Python Package

# Automaticamente vemos o pacote criado no diretório, bem como o arquivo __init__.py

# Todas as funções de um determinado subpacote devem estar escritas em seu respectivo
# arquivo __init__.py, por isso é uma boa prática que cada módulo dentro de um pacote tenha
# seu diretório específico.








