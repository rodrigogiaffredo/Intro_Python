# Dentro do pacote 'utilidadescev' tem um módulo chamado 'dado'. Criar uma função chamada
# leiadinheiro() que funcione como uma função input() mas com uma validação de dados para
# aceitar apenas valores que sejam monetários.

from utilidadescev import dado
from utilidadescev import moeda

preco = dado.leiadinheiro('Digite o preço: R$ ')
moeda.resumo(preco, 34, 61)

