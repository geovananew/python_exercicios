#crie um programa que faça o computador jogar jokenpô com você

from random import randint
from time import sleep
itens = ('Pedra' , 'Papel', 'Tesoura')
computador = randint(0,2)
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador ==1 or jogador ==2 or jogador ==3:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
print('__' * 12)
print(f'Computador jogou {itens[computador]}')
if jogador ==1 or jogador ==2 or jogador ==3:
    print(f'Jogador jogou {itens[jogador]}')
else:
  print('OPÇÃO INVÁLIDA')
print('__' * 12)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA!')