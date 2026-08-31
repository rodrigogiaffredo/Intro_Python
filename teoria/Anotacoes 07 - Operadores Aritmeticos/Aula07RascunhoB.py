n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
# Dica: quando criar variáveis e quando não criar? Variáveis são úteis
# quando precisamos acessar o resultado diversas vezes ao longo do
# programa. Quando não, o cálculo direto na string já resolve.
# print(f'A soma vale {n1+n2}')
# Como estamos aprendendo operadores aritméticos, vamos de variáveis:
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {s}')
print(f'A multiplicação vale {m}')
print(f'A divisão vale {d}')
print(f'A divisão inteira vale {di}')
print(f'A exponenciação vale {e}')
# Podemos mostrar vários resultados num print
print(f'A soma é {s}, a multiplicação é {m} e a divisão é {d:}.')
print(f'Já a divisão inteira é {di} e a exponenciação é {e}.')
# É possível limitar o número de casas decimais de um número real, no
# exemplo abaixo deixei 2 casas após a vírgula.
print(f'A divisão dá {d:.2f}.')
# Se eu quero manter 2 prints distintos numa mesma linha, posso usar
# o comando end igual a espaço no final da primeira linha. Se quiser
# marcar a transição com algum símbolo, basta colocá-lo dentro das aspas.
print(f'A soma dos valores deu {s}.', end=' ')
print(f'Já a multiplicação deu {m}.')
print(f'A soma dos valores deu {s} ',end='>>> ')
print(f'Já a multiplicação deu {m}.')
# É possível também fazer quebra de linha no meio do print usando
# a instrução barra invertida 'n' (\n)
print(f'A soma dos valores deu {s};\nA divisão deu {d:.2f}.')
