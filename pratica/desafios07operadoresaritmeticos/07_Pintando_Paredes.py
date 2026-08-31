# Um programa que indica a área a ser pintada com base na
# largura e na altura informadas, e calcula quantos litros
# de tinta serão necessários (cada litro pinta 2m2)

l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))
area = l * a
print(f'Sua parede mede {l:.1f} m por {a:.1f} m e portanto a área a ser pintada é de {area:.2f} m2.\nPor isso, você precisará de', end = (' '))
print(f'{(area / 2):.2f} litro(s) de tinta para pintá-la, pois um litro de tinta pinta 2 m2 de parede.')