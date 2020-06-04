# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere o valor do dolar = US$ 1,00 = R$ 3,27

real = float(input('Informe quanto de dinheiro você tem na carteira? R$  '))
print('Com R$ {:.2f} reais é possível comprar US$ {:.2f} dolares. '.format(real, real/5.86))
print('Com R$ {:.2f} reais é possível comprar EUR {:.2f} euros. '.format(real, real/6.34))
