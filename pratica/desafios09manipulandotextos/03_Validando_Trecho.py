# Criar um programa que leia o nome de uma cidade e diga se ela começa ou não
# com a palavra "Santo".

cidade = str(input('Digite o nome da cidade: ')).strip()
# Peguei no ar com o professor explicando, porque caso o usuário digite tudo maiúsculo ou
# tudo minúsculo ou tudo zoado, quando eu coloco em formato título, minha checagem pela
# palavra Santo (só o S maiúsculo e o resto minúsculo) não fica comprometida.
ajustado = cidade.title()
lista = ajustado.split()

print(f'O nome da cidade começa com Santo?: {'Santo' in lista[0]}')
