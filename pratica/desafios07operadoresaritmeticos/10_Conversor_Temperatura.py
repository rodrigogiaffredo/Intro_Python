# Um programa que converte a temperatura de °C para °F

c = float(input('Qual a temperatura atual em °C (Celsius): '))
f = (c * 9 / 5) + 32
print(f'>>> Os {c:.1f}°C (Celsius) equivalem a {f:.1f}°F (Fahrenheit).')
