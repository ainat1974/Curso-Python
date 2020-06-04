# Faça um programa que leia a largura e alatura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrado.

b = float(input('Largura da parede em metros:'))
h = float(input('Altura da parede em metros: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(b, h, b*h))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format((b*h)/2))
