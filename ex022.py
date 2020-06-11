print(""" # Crie um programa que leia o nome completo de uma pessoa e mostre: 
            > O nome com todas as letras maiúsculas 
            > O nome com todas as letras minusculas
            > Quantas letras ao todo (sem considerar os espaços)
            > Quantas letras tem o primeiro nome 
          """)
nome = str(input('Digite seu nome completo:')).strip() # strip() elimina os espaços antes e depois da string
print('Analisando seu nome...')
print('Seu nome em maiusculas é: {} '.format(nome.upper())) # coloca todos os caracteres da string em maiúscula
print('Seu nome em minúsculas é: {} '.format(nome.lower())) # coloca todos os caracteres da string em minúscula)
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # elimina os espaços dentro da string
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # nesta lógica ele encontra o primeiro espaço que está logo após o primeiro nome e como ele não considera o índice onde está o espaço da certo
separa = nome.split() # split() cria listas as strings entre os espaços
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))