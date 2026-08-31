# Adaptar o código do exercício criando uma função adicional chamada moeda() que
# consiga mostrar os valores como um valor monetário formatado. Vamos manter o arquivo
# anterior e criar um novo, com a atualização.

import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A medade de {moeda.moeda(preco)} é igual a {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é igual a {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando {moeda.moeda(preco)} em 15% temos {moeda.moeda(moeda.aumentar(preco, 15))}')
print(f'Reduzindo {moeda.moeda(preco)} em 27% temos {moeda.moeda(moeda.diminuir(preco, 27))}')
