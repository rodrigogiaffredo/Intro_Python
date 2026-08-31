# Adicionar ao módulo moeda.py uma função chamada resumo() que mostra na tela algumas
# informações geradas pelas outras funções criadas nos exercícios anteriores, em formato
# tabela com cabeçalho centralizado, margens superior e inferior, contendo Preco analisado,
# Dobro do preco, Metade do preco, 80% de aumento, 35% de redução, e todos os valores
# formatados.

import moeda

preco = float(input('Digite o preço: R$ '))
moeda.resumo(preco, 48, 17)


