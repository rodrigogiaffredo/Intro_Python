# Dentro do pacote utilidadescev tem um módulo chamado 'dado'. Criar uma função chamada
# leiadinheiro() que funcione como uma função input() mas com uma validação de dados para
# aceitar apenas valores que sejam monetários. Daí o programa principal vai ser minúsculo
# também, com a primeira linha preco = dado.leiadinheiro("Digite o preço em R$: ') e na
# linha de baixo moeda.resumo(preco, 35, 22). Daí qualquer coisa diferente de números que
# for digitada pelo usuário, aparece em texto vermelho 'ERRO! 'tal coisa que você digitou'
# é um preço inválido.' E já aparece na linha de baixo o 'Digite o preço em R$: '.
# Até que o usuário entre com um valor numérico e a tabelinha é gerada. Mas tem um pulo do
# gato: no input do valor com centavos vai aceitar tanto ponto quanto virgula, ao invés de
# so ponto como é padrão do Python.

def leiadinheiro(numero):
    # Elimino quaisquer espaços da string
    dinheiro = str(input(numero)).strip()
    # O usuário pode até digitar vírgula, que eu substituo por ponto e continuo validando
    if ',' in dinheiro:
        dinheiro = dinheiro.replace(',', '.')
    # Substituo ponto por nada para validar se a string que sobra é apenas numérica
    ajustado = dinheiro.replace('.','')
    while True:
        # Se o que sobra na string não for apenas número, retorno o erro até corrigir
        if ajustado.isnumeric() == False:
            dinheiro = str(input('\033[31mERRO! Digite um preço válido: \033[m')).strip()
            # Depois da nova entrada, faço as substituições e exclusões novamente
            if ',' in dinheiro:
                dinheiro = dinheiro.replace(',', '.')
            ajustado = dinheiro.replace('.', '')
        # Se estiver tudo certo com a entrada, encerro o loop
        else:
            break
    # Mostro a string 'dinheiro' convertida para float agora que garanti que é numérica
    return float(dinheiro)


# SOLUÇÃO DO PROFESSOR (mais simples aparentemente, gostei do raciocínio)

# def leiadinheiro(msg):
#   valido == False
#   while not valido:
#       entrada = str(input(msg)).replace(',', '.').strip()
#       if entrada.isalpha() or entrada == '': --> Verificando se é alfanumérica
#                                                  ou vazia
#           print(f'\033[31mERRO: \"{entrada}"\ é um preço inválido\033[m')
#       else:
#           valido == True
#           return float(entrada)