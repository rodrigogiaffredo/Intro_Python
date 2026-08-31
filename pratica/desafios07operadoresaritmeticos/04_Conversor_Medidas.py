# Um programa que converte metros em centímetros e milímetros

import hmac
from encodings.cp862 import decoding_map

m = float(input('Quantos metros vamos converter?: '))
km = (m/1000)
hm = (m/100)
dcam = (m/10)
dcm = (m*10)
cm = (m*100)
mm = (m*1000)
print(f'Para sua informação, {m:.2f} metros equivalem a:\n>>> {cm:.2f} cm\n>>> {mm:.2f} mm')
print(f'Além disso:\n>>> Em km: {km}\n>>> Em hm: {hm}\n>>> Em dcam: {dcam}\n>>> Em dcm: {dcm}.')
