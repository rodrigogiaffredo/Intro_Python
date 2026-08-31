# O Python permite tratar erros e criar respostas para exceções, através da estrutura
# 'try: except: else: finally:'.

# Em linhas gerais, os erros na programação podem ser SINTÁTICOS (relacionados à sintaxe do
# código) ou SEMÂNTICOS (relacionados à estrutura e à lógica do programa).

# Exemplo de erro sintático: primt(x) com 'm' no lugar de 'n'

# Exemplo de erro semântico: print(x) sem a definição prévia da variável 'x'

# IMPORTANTE:erros semânticos não são chamados normalmente de erros,
# mas sim de EXCEÇÕES ('Exception').

# No exemplo print(x) sem a prévia definição de 'x', é disparada uma EXCEÇÃO chamada
# 'NameError'.

# Outro exemplo: n = int(input('Digite um número: ')), se digitarmos um número o programa
# roda, mas se escrevermos o número por extenso ('oito' ao invés de 8), ocorrerá uma
# exceção chamada 'ValueError' (defini 'n' como int, e digitei uma str).

# Outro exemplo: a = int(input('Numerador: ')) b = int(input('Denominador: ')) r = a / b
# print(f'O resultado é {r}').

# Além da exceção de valor ('ValueError'), é possível também que ocorra alguma
# exceção diretamente relacionada ao cálculo, por exemplo, se disser que b = 0 ocorrerá
# a exceção 'ZeroDivisionError'.

# Outro exemplo: r = 2 / '2' (no Python, um int dividido por uma str gera uma exceção
# chamada 'TypeError').

# Outro exemplo: lst = [3, 6, 4] print(lst[3]) esperando que o número '4' seja impresso,
# porém as contagens começam em 0, e não em 1, portanto essa lista não possui a posição
# [3] e o comando resultará na exceção 'IndexError'.

# Se fosse o mesmo caso porém com um dicionário, a exceção seria um 'KeyError'.

# Outro exemplo, tentar importar um módulo que não existe resulta na exceção
# 'ModuleNotFoundError'.

# Para lidar com exceções em Python usamos a estrutura 'try: except: else: finally: '

# try:
#    operação --> aquilo que pode eventualmente dar um problema
# except:
#    falha --> o que acontece caso a operação proposta em 'try' falhe
# else:
#    execução --> o que acontece caso a falha não ocorra (OPCIONAL)
# finally:
#    continuidade --> o que acontece independente de ter ocorrido a falha o não (OPCIONAL)

# Bastante útil em momento de desenvolvimento do programa, pois por exemplo classes de
# erro não são o tipo de coisa que temos que mostrar para usuários do sistema, mas são
# muito úteis para o desenvolvedor enquanto ele cria os programas.

# É possível ter tantos 'except' quanto necessários, a depender da quantidade de cenários
# que o desenvolvedor precise testar para garantir a qualidade do programa.

# try:
#    operação
# except TypeError:
#    falha
# except ValueError:
#    falha
# except OSError:
#    falha
# else:
#    execução
# finally:
#    continuidade



