# Criar um programa que tenha uma tupla com várias palavras (não usar acentos). Mostrar,
# para cada palavra, quais são as suas vogais. Exemplo de output: "A palavra CANDLE tem
# as vogais a e ", "A palavra MAXIMA tem as vogais a i a", etc.

tupla = ('ticker', 'candle', 'abertura', 'maxima', 'minima', 'fechamento', 'volume')
print(tupla)

print('-' * 40)
c = 0
while c < len(tupla):
    # Apelei para o NotebookLM na parte de encontrar e imprimir as vogais, o resto eu fiz.
    # E realmente não chegaria a essa conclusão sozinho, mas faz todoh o sentido: criar uma
    # variável chamada vogal que receba os elementos (que nesse caso são palavras) da tupla
    # a cada rodada do while; Em seguida, criar um for aninhado com um if que percorra a
    # palavra e procure por 'aeiou'. Daí imprime as letras com espaço entre elas.
    # O professor fez do mesmo jeito, mas eu achei genial porque ao invés desse passo de
    # jogar tupla[c] para dentro de uma variável palavra, ele considerou o próprio c (que é
    # um elemento da tupla de palavras) como uma nova variável composta com várias letras
    # que as compõem. Ficou assim:
    # No lugar de 'palavra = tupla[c]' seguido de 'for vogal in palavra', ficou apenas:
    # 'for vogal in c':
    # e o teste lógico é exatamente o mesmo.
    palavra = tupla[c]
    print(f'A palavra {tupla[c].upper()} tem as vogais:  ', end = '')
    for vogal in palavra: # Vogal é apenas um contador, e palavra é o elemento [c] da tupla
        if vogal in 'AEIOUaeiou': # Agora, os elementos (contados pelo contador 'vogal')
                                  # são as letras da palavra.
            print(vogal, end = '  ')
    c += 1
    print()




# DESTACAR E CONTAR AS VOGAIS