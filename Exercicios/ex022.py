#Crie um programa que leia o nome completo de uma pessoa e mostre:
# --> o nome com todas as letras maiúsculas
# --> o nome com todas minúsculas
# --> quantas letras ao todoo (sem considerar espaços)
# --> quantas letras tem o primeiro nome

nome= str(input('Digite seu nome completo: ')).strip() #strip elimina os espaços antes e depois
print(f'seu nome em maiúsculas é {nome.upper()}')
print(f'seu nome em minúsculas é {nome.lower()}')
letras = len(nome)-nome.count(' ')
print(f'seu nome tem ao todo {letras} letras')
primeiro = nome.find(' ')
print(f'seu primeiro nome tem {primeiro}')
