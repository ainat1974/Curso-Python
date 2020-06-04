# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual o salário do Funcionário? R$ '))
aum = sal + (sal * 15 / 100)
print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber {:.2f} de salário.'.format(sal, aum))