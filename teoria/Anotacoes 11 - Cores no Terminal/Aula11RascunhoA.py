# Baseado no padrão ANSI escape sequence, não vamos de módulo colorize, é o básico.
# A forma escolhida no curso é a da sintaxe \033[ codigo da cor m (contra-barra, zero trinta e três,
# abre colchetes, o código de estilo, cor do texto e cor de fundo, todos separados por ponto
# e vírgula, e a letra 'm' minúsculo no final.

# Sintaxe genérica: \033[ style;text;back m

# No exemplo \033[0;33;44m o estilo da fonte é 0, a cor do texto é 33 e a cor do fundo é 44

# Todos os valores numéricos são opcionais, e a ordem não importa pois o identificador do
# tipo está na dezena, e não na posição ocupada (dezena 3 é sempre cor do texto, dezena 4
# é sempre cor de fundo, dezena nula é sempre estilo de texto).

# Os códigos para estilo da fonte que funcionam melhor no terminal para Python são:

# 0: none, ou sem estilo nenhum
# 1: bold, ou negrito
# 4: underline, ou sublinhado
# 7: negative, ou inversão (o que está configurado para letra vai para fundo, e vice-versa)

# Já os de cores de texto são:

# 30: preto
# 31: vermelho
# 32: verde
# 33: amarelo
# 34: azul
# 35: magenta (lilás)
# 36: ciano (verde água)
# 37: cinza
# 97: super branco

# As cores de fundo seguem a mesma lógica das de texto, mas com dezena 4 (40, 41, 42, etc.)

#Exemplos

# \033[0;37;41m é sem estilo, texto super branco, fundo vermelho
# \033[4;33;44m é sublinhado, texto amarelo e fundo azul
# \033[1;35;43m é negrito, texto magenta e fundo amarelo
# \033[37;42m é sem estilo (pode omitir ao invés de colocar 0), texto super branco e fundo verde
# \033[m é sem estilo, texto cinza e fundo preto, que é o padrão do terminal
# \033[7;97m é estilo negativo, e como 97 é super branco o texto fica preto (que é a cor do fundo)
# e o fundo fica preto (que é a cor do texto).









