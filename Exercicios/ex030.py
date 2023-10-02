#crie um programa que leia um número interio qualquer e mostre na tela se ele é PAR ou ÍMPAR

n = int(input('Digite um número: '))
resultado = n % 2
if resultado == 0:
    print(f'o número {n} é par')
else:
    print(f'o número {n} é ímpar')