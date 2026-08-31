# Criando tabelas com rich_

import rich
from rich import print
from rich.table import Table    # Lembrando que CLASSES começam com maiúsculas

tabela = Table(title = 'Tabela de Preços')
tabela.add_column('Produto', justify = 'right')
tabela.add_column('Preço', justify = 'center', style = 'blue')
tabela.add_row('Lápis', 'R$ 1,50')
tabela.add_row('Borracha', 'R$ 0,50')

print(tabela)

