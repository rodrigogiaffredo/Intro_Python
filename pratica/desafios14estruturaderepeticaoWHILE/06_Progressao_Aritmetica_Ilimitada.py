# Melhorar o desafio anterior (aula 14 desafio 05, o da PA), perguntando ao usuário se ele
# quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0
# (zero) termos.

print()
print('-' * 43)
print('-- CALCULANDO A PROGRESSÃO ARITMÉTICA (PA) --')
print('-' * 43)

# an = a1 + (n - 1) * r

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termos = int(input('Quantos termos quer ver?: '))
termosamais = ()
n = 1

while n <= termos:
    print(f'{a1}', end = '')
    # Aí o lance de limpar a última flechinha de novo.
    print(' -> ' if n < termos else '', end = '')
    a1 += r
    n += 1
    if n > termos:
        print()
        termosamais = int(input('Quer ver mais termos? Digite quantos (ou digite 0 para encerrar): '))
        if termosamais != 0:
            termos += termosamais
            print(f'{a1}', end = ' -> ')
            # Aí o lance de limpar a última flechinha de novo.
            print(' -> ' if n < termosamais else '', end = '')
            a1 += r
            n += 1
        else:
            print()
            # Vi que o professor incluiu essa visualização na demo, corri e fiz também.
            print(f'Você visualisou {termos + termosamais} termos da PA.')
print('-- Fim --')
print()




