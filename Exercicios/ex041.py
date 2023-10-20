#a confederação nacional de natação precisa de um programa que
# leia o ano de nascimento de um atleta  e mostre sua categoria, de acordo com a idade:
# até 9 anos: mirim;
# até 14 anos: infantil;
# até 19 anos: junior;
# até 25 anos: sênior;
# acima:master

from datetime import date
nasc = int(input('Informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'você tem {idade} ano(s)')
if idade <=9:
    print('a categoria da sua idade é mirim')
elif idade <=14:
    print('a categoria da sua idade é infantil')
elif idade <=19:
    print('a categoria da sua idade é junior')
elif idade <=25:
    print('a categoria da sua idade é senior')
else:
    print('a categoria da sua idade é master')