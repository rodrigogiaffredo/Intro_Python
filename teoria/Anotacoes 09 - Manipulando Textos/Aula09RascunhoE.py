# Exercitando durante a aula

# Dica muito boa: quando queremos imprimir um texto muito grande, ao invés de escrever
# infinitamente na horizontal, podemos fazer a quebra de texto como quisermos preservando
# os espaços entre palavras, daí no começo da string abrimos aspas 3 vezes, e no final fechamos
# também 3 vezes.

print("""Batatinha quando nasce esparrama pelo chão, a menina quando dorme põe a 
mão no coração, água mole em pedra dura tanto bate até que fura, pelo ronco pelo berro 
esse pulmão é de ferro.""")

frase = 'Curso Teórico e Prático Python'
outra = '   Estuda sem parar   '
lista = frase.split()


print(frase)
print(frase[3])
print(frase[4:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(outra.strip())
print('Curso' in frase)
print(frase.find('Teórico'))
print(frase.find('teórico'))
print(frase.lower().find('teórico'))
print(frase.split())
print(lista)
# Mostrando somente o primeiro elemento da lista (o elemento zero, não esquece)
print(lista[0])
# Mostrando no elemento "tal" da lista, o caractere da posição "tal" (Exemplo,
# a letra 4 da palavra 3, lembrando que a palavra curso é a zero, assim como a letra "P")
print(lista[3][4])

print(frase.replace('Python', 'Android'))

# A mudança acima ocorre apenas na instância print, a variável frase continua íntegra.
# Para mudar definitivamente o conteúdo de frase substituindo as palavras Python por
# Android, o caminho correto é:

frase = frase.replace('Python', 'Android')
print(frase)

# Transformando cada caractere da frase num elemento de lista
por_caractere = list(frase)
print(por_caractere)
print()

# Alinhamentos à esquerda, direita e centro (seguem a lógica de f-string)
print('Impressão com alinhamento')
print(f'{'Rodrigo':<20}', f'{'Rodrigo':>20}', f'{'Rodrigo':^20}')






