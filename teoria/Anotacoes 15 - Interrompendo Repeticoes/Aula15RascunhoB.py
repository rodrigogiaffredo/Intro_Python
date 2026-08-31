# Repetições WHILE (com teste lógico no início) podem ser interrompidas. Essa interrupção
# desvia o programa para o lado de fora do laço de repetição, eliminando inclusive a
# necessidade do teste lógico no início do programa.

# Uma estrutura de repetição comum, para servir de parâmetro de comparação.
cont = 1
while cont <= 10:
    print(cont, ' ', end = '')
    cont += 1
print('-- Fim --')
print()


# Substituindo o teste lógico pelo booleano True, o programa roda infinitamente.
#cont = 1
#while True:
#    print(cont, ' ', end = '')
#    cont += 1
#print('-- Fim --')

# While True executa o programa infinitamente, e o comando que faz com que esse loop infinito
# seja encerrado é o comando break.

# Usando como exemplo a missão de montar um programa que seja interrompido ao atingir a flag
# 999, enquanto soma todos os números digitados mas não soma a própria flag, poderíamos usar
# o break da seguinte forma:

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break # O break antes da atualização da soma exclui o flag do resultado dela.
    s += n
print(f'A soma dos números digitados é {s}.')
