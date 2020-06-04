# Escreva um programa que leia um valor em metros e o exiba convertido em kilômetro, Hectômetro, Decâmetro,
#  Decímetro, Centímetro e Milímetro.

v = float(input('Digite um valor em metros: '))
print('O valor {} em metros. Corresponde a: '.format(v))
print('Kilômetro = {} Km'.format(v/1000))
print('Hectômetro = {} Hm'.format(v/100))
print('Decâmetro = {} Dac'.format(v/10))
print('Decímetro = {} dm'.format(v*10))
print('Centimetro = {} cm'.format(v*100))
print('Milímetro = {} mm'.format(v*1000))
