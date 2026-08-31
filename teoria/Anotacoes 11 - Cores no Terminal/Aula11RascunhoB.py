# 0: none, ou sem estilo nenhum
# 1: bold, ou negrito
# 4: underline, ou sublinhado
# 7: negative, ou inversão (o que está configurado para letra vai para fundo, e vice-versa)

# 30: preto
# 31: vermelho
# 32: verde
# 33: amarelo
# 34: azul
# 35: magenta (lilás)
# 36: ciano (verde água)
# 37: cinza
# 97: super branco

print('Hello world!')
# em vermelho
print('\033[0;31mHello world!')
# negrito, letra vermelha, fundo amarelo (como não fechei a configuração de cima, a letra
# continua vermelha, não preciso citar novamente).
print('\033[1;43mHello world!')
# Dica: quanto fechamos a configuração no final da frase (\033[m), limitamos o efeito de
# fundo ao tamanho do texto somente (evitando aquela faixa infinita), e voltamos a cor do
# texto à original do terminal.
print('\033[1;43mHello world!\033[m')
# sublinhado, letra branca, fundo magenta
print('\033[4;97;45mHello world!\033[m')
# letra branca, fundo preto (só deixar fundo sem nada que já pega a cor do terminal).
print('\033[0;97mHello world!\033[m')
# letra preta, fundo super branco (é só usar o 7 no estilo, que é o negativo, ou inversão).
print('\033[7;97mHello world!\033[m')
# letra amarela, fundo azul
print('\033[0;33;44mHello world!\033[m')
# agora invertendo o anterior, basta colocar 7 no estilo
print('\033[7;33;44mHello world!\033[m')
