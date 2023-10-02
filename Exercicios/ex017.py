#faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa
import math

oposto = float(input('Informe o comprimento: '))
adjacente = float(input('Cateto adjacente'))
hipotenusa = math.hypot(oposto, adjacente)
print(f'a jipotenusa vai medir {hipotenusa:.2f}')