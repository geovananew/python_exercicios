#escreva um programa para aprovar o empréstimo bancário de uma casa.
#o programa vai perguntar o valor da casa, o salário e em quantos anos ele vai pagar
#calcule o valor da prestação mensal,sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor = float (input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos= float(input('Em quantos anos vai pagar? '))
prestacao = valor/ (anos*12)
minimo = salario * 30/100
print(f'a prestação mensal será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')