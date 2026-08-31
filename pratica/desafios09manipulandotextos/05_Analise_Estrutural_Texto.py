# Criar um programa que leia uma frase digitada e mostre quantas vezes aparece a
# letra "A", em que posição ela aparece pela primeira vez, e em que posição ela
# aparece pela última vez.

# Aprendi nas aulas anteriores, e já meti um strip e um lower logo na variável porque
# fica a prova de erro de digitação do usuário e minha busca é por 'a' minúsculo.

frase = str(input('Digite uma frase: ')).strip().lower()

# Aqui eu achei que precisaria usar .lfind para a primeira aparição, mas no caso é só .find
# porque a procura começa sempre da esquerda para a direita. Outro detalhe é que coloquei um
# + 1 para que a coisa da posição zero não afete a contagem visual, senão dá a impressão para
# quem lê que a contagem está errada. Já no caso da última, aí sim uso o .rfind.

print(f'Aparições da letra * A * :\n>>> Quantas vezes aparece: {frase.count('a')}\n>>> Primeira vez: posição {(frase.find('a')+1)}\n>>> Última vez: posição {(frase.rfind('a')+1)}')

# Comentário: desse jeito, se eu escrevo a palavra 'não', o programa não conta esse 'a' por
# causa do til. Daí temos que incluir o módulo unicodedata no programa (segundo o NoteBookLM)
# mas é avançado e o professor ainda não chegou aqui.