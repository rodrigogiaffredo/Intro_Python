# Fazer um programa que tenha uma função chamada escreva() que receba um texto qualquer
# como parâmetro e mostre uma mensagem com tamanho adaptável. Exemplo: escreva('Olá, Mundo!')
# saída ~~~~~~~~~~~
# 		Olá, Mundo!
# 		~~~~~~~~~~~
# O truque é que as linhas de cima e de baixo vão sempre acompanhar o tamanho do texto, sem
# sobrar nem faltar. As 3 frases a gente já digita no programa principal, não tem entrada de
# usuário.

def escreva(texto):
    # Tive que criar a variável 'tamanho' para poder somar 4 e deixar 2 sobrando de cada lado
    tamanho = len(texto) + 4
    print('~' * tamanho)
    # Chave dentro de chave foi sugestão do autocomplete do PyCharm, eu não sabia essa
    # O professor meteu a gambiarra de dar 2 espaços antes da palavra 'texto' abaixo kkkkk
    print(f'{texto:^{tamanho}}')
    print('~' * tamanho)

escreva('Brasil ganhou de virada do Japão!')
print()
escreva('Palmeiras!')
print()
escreva('Hello World!')
