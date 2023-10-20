#refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#equilátero: todos os lados iguais; isósceles: dois lados iguais; escaleno: todos os lados diferentes

r1 = float(input('primeira reta: '))
r2= float(input('segunda reta: '))
r3= float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+ r2:
    print('os segmentos PODEM FORMAR um triângulo')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('os segmentos NÃO PODEM FORMAR um triângulo')