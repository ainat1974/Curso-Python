# Detalhando string
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ela

# Pode ser escrito assim                  ou                          Assim
n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))   #print('O tipo primitivo desse valor é ', (type(n))
print('Só tem espaços? {}'.format(n.isspace()))              #print('Só tem espaços?', n.isspace())
print('É um número? {}'.format(n.isnumeric()))               #print('É um número?', n.isnumeric())
print('É alfabetico? {}'.format(n.isalpha()))                #print('É alfabetico?', n.isalpha())
print('É alfanumérico? {}'.format(n.isalnum()))              #print('É alfanumérico?', n.isalnum())
print('Está em maiúsculas? {}'.format(n.isupper()))          #print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas? {}'.format(n.islower()))          #print('Está em minúsculas?', n.islower())
print('Está capitalizada? {}'.format(n.istitle()))           #print('Está capitalizada?', n.istitle())
