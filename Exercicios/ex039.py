#faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#se ele ainda vai se alistar ao serviço militar; se é a hora de se alistar; se já passou do tempo de alistamento
#também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'quem nasceu em {nasc} tem {idade} anos em {atual}')
if  idade == 18:
    print('é hora de se alistar!')
elif idade <18:
    print(f'faltam {18 - idade} anos para se alistar')
elif idade >18:
    print(f'você já deveria ter se alistado há {idade - 18} ano(s)')