print(''' Um professor quer sortear um dos seus quatro alunos para
 apagar o guadro. Faça um programa que ajude ele, lendo o nome deles
  e escrevendo o nome do escolhido. \n''')

from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolha = choice(lista)
print('O aluno escolhido foi {}'.format(escolha))