# Criar um pacote chamado 'utilidadescev' que tenha dois módulos internos chamados moeda e
# dado. Transferir todas as funções utilizadas nos 4 desafios anteriores para o primeiro
# pacote e manter tudo funcionando no programa principal. O código a ser utilizado é
# exatamente o mesmo do último exercício, mas com o novo import.

from utilidadescev import moeda

preco = float(input('Digite o preço: R$ '))
moeda.resumo(preco, 25, 34)