#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#para salários superiores a R$1250,00 calcule um aumento de 10%
#para salários inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o seu salário? '))
if salario <=1250:
    print(f'o novo salário será R${salario + salario * 15/100:.2f}')
else:
    print(f'o novo salário será R${salario + salario * 10 /100:.2f}')

