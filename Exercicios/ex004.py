#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

a= input('Digite algo: ')
print('o tipo primitivo é', type(a))
print('só tem espaços?', a.isspace())
print('é um número?', a.isnumeric())
print('é alfabetico?', a.isalpha())
print('é alfanumérico?', a.isalnum())
print('está em maiúsculas?', a.isupper())
print('está em minúscula?', a.islower())
print('está capitalizado?', a.istitle())

