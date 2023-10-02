# Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = str(input('Digite seu nome completo: '))
print(f'seu nome tem silva? {"silva" in nome.lower()}')
