# Crie um programa que leia um número Real qualquer pelo tecldo e mostre na tela a sua porção inteira.

import math # desta forma importa todas as funcionalidades da bliblioteca math
valor = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(valor, math.trunc(valor)))