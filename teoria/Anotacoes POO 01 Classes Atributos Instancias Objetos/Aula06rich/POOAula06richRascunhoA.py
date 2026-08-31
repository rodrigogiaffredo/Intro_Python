# Biblioteca rich_

# Para instalar: Python packages na barra lateral / digita rich na busca / install

# Em seguida, clica na flechina de 'Current File / Edit configurations'
# No canto inferior esquerdo, clica em 'Edit configuration templates'
# Seleciona 'Python' na lista, e clica em 'Modify options' no canto superior direito
# Marca a opção 'Emulate terminal in output console' / 'Apply' / 'Ok'

# Uma vez instalado, podemos chamar os módulos da biblioteca

# A partir de agora, é muito mais simples mexer com cores, estilos, emojis, tabelas

import rich
from rich import print

# Um exemplo interessante: após a importação da biblioteca rich_, é possível substituir
# o print que usei até aqui, pelo print do rich_. O comando funciona da mesma maneira,
# mas agrega novas funcionalidades.

# Imprimindo só a palavra 'World' em vermelho com um emoji do globo terrestre
print('Hello [red]World[/]! :earth_americas:')
# Imprimindo a palavra 'PALESTRA' em negrito verde com fundo branco e emoji coração
print('Vai [bold green on white]PALESTRA[/]! :raising_hands_medium-light_skin_tone:')
# Imprimindo joínha pra baixo e joínha pra cima
print(':-1:    :+1:')

# Para escolher emojis: abre o 'Terminal' na barra lateral esquerda, e digita:
# python -m rich.emoji
# Vai aparecer a lista completa dos nomes dos emojis; basta escrevê-los no código.
# IMPORTANTE: tem que importar a biblioteca rich_ inteira para o comando acima funcionar


