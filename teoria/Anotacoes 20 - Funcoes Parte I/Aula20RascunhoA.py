# Funções (ou rotinas) são trechos de código que podem ser executados em momentos diferentes
# seja com parâmetros simples, seja com parâmetros múltiplos.

# Coisas que se repetem constantemente são resolvidas com funções. Ao longo do curso usei
# muitas funções nativas do Python, tais como print(), len(), input(), int(), float().

# Porém nem sempre as funções pré-definidas são suficientes para o que precisamos fazer, por
# isso é possível criar nossas próprias funções. Um exemplo simples, constantemente eu digito
# no mesmo programa print('-' * 35) para criar linhas separadoras, ou print() para pular linhas
# diversas vezes. Esses são fortes candidatos a virarem rotinas, ou funções.

# O comando 'def' declara funções no Python.

# Exemplo de uso potencial:

# print('------------------------------------------')
# print('       SISTEMA DE ALUNOS                  ')
# print('------------------------------------------')
# print('------------------------------------------')
# print('       CADASTRO DE FUNCIONÁRIOS           ')
# print('------------------------------------------')
# print('------------------------------------------')
# print('       ERRO DO SISTEMA                    ')
# print('------------------------------------------')

# Os cabeçalhos sempre têm uma linha antes, outra depois do texto. Ao invés de digitá-los
# todas as vezes, posso definir uma função 'mostralinha' através de um def:

# def mostralinha():
#   print('------------------------------------------')

# O que tornaria possível o código abaixo:

# mostralinha()
# print('       SISTEMA DE ALUNOS                  ')
# mostralinha()
# mostralinha()
# print('       CADASTRO DE FUNCIONÁRIOS           ')
# mostralinha()
# mostralinha()
# print('       ERRO DO SISTEMA                    ')
# mostralinha()

# Quando a função é chamada, o programa procura no código onde estão os detalhes da função,
# vai até lá, executa de acordo, e em seguida volta para o ponto do código imediatamente
# posterior à chamada da função.

# Questão funcional: entre o 'def' e o programa principal, é necessário ter duas linhas
# vazias.

# 'Def' cria comandos personalizados, mas além disso é possível trabalhar com parâmetros, o
# que o torna muito mais poderoso.

# No exemplo dos cabeçalhos, podemos perceber que a única diferença entre eles é o texto
# que fica entre linhas. Ao usar 'def' com parâmetros variáveis (no caso 'msg'), podemos
# criar o seguinte:

# def mensagem(msg):
#   print('-' * 30)
#   print(msg)
#   print('-' * 30)

# E para criar por exemplo um cabeçalho com a mensagem 'SISTEMA DE ALUNOS', bastaria chamar
# a função da seguinte forma:

# mensagem('SISTEMA DE ALUNOS')

# O que resultaria em:

#   ------------------------------------------
#         SISTEMA DE ALUNOS
#   ------------------------------------------

# O parâmetro (msg) poderia ser qualquer outra coisa, por exemplo, (txt), (frase), enfim, o
# que eu quiser usar.

