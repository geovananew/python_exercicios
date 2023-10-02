#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
m= (nota1 + nota2) /2
print(f'Suas notas são {nota1} e {nota2} e a média delas é {m:.1f}')