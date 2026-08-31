# Reescrever a função 'leiaint' do exercício 04 de Modularização,  incluindo a
# possibilidade da digitação de # um tipo inválido. Criar também uma função leiafloat()
# com a mesma funcionalidade.


def leiaint(msg):
    try:
        while True:
            try:
                inteiro = int(input(msg))
            except (ValueError, TypeError):
                print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
                continue
            else:
                return inteiro
    except KeyboardInterrupt:
        print()
        print('\033[31mPrograma encerrado pelo usuário.\033[m')
        return 0
    else:
        return inteiro




def leiafloat(msg):
    try:
        while True:
            try:
                real = float(input(msg))
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número real válido.\033[m')
                continue
            else:
                break
    except KeyboardInterrupt:
        print()
        print('\033[31mPrograma encerrado pelo usuário.\033[m')
        return 0
    else:
        return real






# Programa principal
n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}.')
