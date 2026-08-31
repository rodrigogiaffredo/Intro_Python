# Estruturas condicionais que aparecem dentro de outras estruturas condicionais, são
# chamadas de condições aninhadas.

# Sintaxe genérica: if..: elif..: else..:

nome = str(input('Digite o seu nome: '))
if nome == 'Rodrigo':                                       # CONDICIONAL SIMPLES
    print('Nome lindo hein, parabéns!')
elif nome == 'Neide' or nome == 'Judite':                   # CONDICIONAL ANINHADA
    print('Nome de véia! Brinks...')
elif nome in 'Creitin Marquin Junin Sergin':                # CONDICIONAL ANINHADA
    print('Nome feio da muléstxa! Brinks...')
else:                                                       # CONDICIONAL COMPOSTA
    print('O nome é comum, mas o dia não precisa ser!')     # O else.: é sempre opcional
print(f'Tenha um bom dia, {nome}!')
