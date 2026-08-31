# Monitoramento de erros através da biblioteca rich_

import rich
from rich.traceback import install      # >>> Importação do módulo específico

install()                               # >>> Gatilho do monitoramento

def divisao(x, y):
    return x / y

# Ao dividir 50 por 0 temos um erro, que sem o 'install' é apresentado de forma bagunçada
# Com o 'install', ele aponta a função que contém o erro, e dá um nome a ele de maneira
# muito mais organizada, facilitando o endereçamento da correção.
print(divisao(50, 0))