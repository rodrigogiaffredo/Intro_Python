# Atividades práticas de aprendizagem
# Lembrando: igual em Python são dois sinais de igual (1 só é recebe).

# Estrutura condicional simples, sem o else.
# Alguns ifs não precisam de um else. Adicionalmente note que a parte identada só acontece
# se a condição for verdadeira, e tudo que está colado na margem acontece em qualquer caso.
# Importantíssimo identar:


#nome = str(input('Digite seu nome: '))
#if nome == 'Rodrigo':
#    print('Que nome lindo você tem!')
#print(f'Muito prazer em te conhecer, {nome}!')
#print('--FIM--')


# Usando a condicional composta (com else) e identação:

nome=str(input('Digite seu nome: '))
if nome == 'Rodrigo':
    print('Caraca mano, que nome lindo da porra!')
else:
    print('Nome comum, vida que segue.')
print(f'Brinks kkkkk muito prazer em te conhecer, {nome}!')
print('--PRÓXIMO--')


# Outro exemplo, o velho e bom cálculo das médias com feedback, usando a sintaxe completa
# e em seguida usando a sintaxe simplificada.

# Sintaxe condição completa

#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = (n1 + n2) / 2
#if m >= 6.0:
#    print(f'Média {m:.1f}? Aprovado porra, parabéns!')
#else:
#    print(f'Média {m:.1f}? Reprovado ahahahah prepara a lomba!')
#print('--FIM--')

# Sintaxe condição simplificada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) /2
print(f'Média {m:.1f}, vejamos o que isso significa:')
print('Passou de ano!' if m >= 6.0 else 'Reprovado, que pena...')
print('--FIM--')
