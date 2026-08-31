# Usando painéis via rich_

import rich
from rich import print
from rich.panel import Panel        # Importando a CLASSE 'Panel' do módulo 'panel'

# Um OBJETO chamado 'caixa' criado na CLASSE 'Panel'
print()
caixa = Panel('[yellow]Criando um painel de exemplo[/]', title = 'Interessante',
              style = 'blue', width = 50)
print(caixa)
