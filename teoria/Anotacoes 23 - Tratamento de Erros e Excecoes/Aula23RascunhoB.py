# O Python permite tratar erros e criar respostas para exceções, através da estrutura
# 'try: except: else:'.

# try:
#   operação --> aquilo que pode eventualmente dar um problema
# except:
#   falha --> o que acontece caso a operação proposta em 'try' falhe
# else:
#   execução --> o que acontece caso a falha não ocorra (OPCIONAL)
# finally:
#   continuidade --> o que acontece independente de ter ocorrido a falha o não (OPCIONAL)


print()
print('Tratando exceção com mensagens personalizadas')
# Executar dividindo por zero, ou escrevendo os números por extenso
try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b
except:
    print('Houve um problema com o cálculo.')
else:
    print(f'O resultado da divisão é {r}')
finally:
    print('-- Fim do Programa --')


print()
print('Tratando exceção mencionando conteúdo formal do Python sobre a exceção')
try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b
# Acessando o tipo 'Exception' e armazenando seu resultado na variável 'erro'
except Exception as erro:
    # Ao digitar 'erro.' aparece uma lista de possibilidades, o professor começou
    # a demonstração usando '__class__' que traz por exemplo 'ZeroDivisionError'
    print(f'Houve um problema com o cálculo: {erro.__class__}')
else:
    print(f'O resultado da divisão é {r}')
finally:
    print('-- Fim do Programa --')


print()
print('Tratando várias exceções com sequência de except')
# Executar dividindo por zero, escrevendo os números por extenso, e interrompendo a
# execução do programa no teclado.
try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Houve um problema com o cálculo, relacionado ao tipo de dado digitado.')
except ZeroDivisionError:
    print(f'Não é possível dividir {a} por zero.')
except KeyboardInterrupt:
    print('O usuário optou por não informar os dados.')
except Exception as erro:  # Erro genérico, sempre bom durante a fase de programação
    print(f'Ocorreu um erro relacionado a {erro.__class__}')
else:
    print(f'O resultado da divisão é {r}')
finally:
    print('-- Fim do Programa --')

