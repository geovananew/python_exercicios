#crie um programa que leia o ano de nascimento de sete pessoas
#no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas já são maiores

from datetime import date
atual = date.today ().year
maioridade = 0
menoridade = 0
for pess in range(1,8):
    nasc= int(input(f'Em que ano a {pess}ª nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        maioridade += 1
    else:
        menoridade +=1
print(f'Ao todo tivemos {maioridade} pessoas maiores de idade')
print(f'E também tivemos tivemos {menoridade} pessoas menores de idade')