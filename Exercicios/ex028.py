#escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
computador = randint(0,5) #Faz o computador escolher
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
if jogador == computador:
    print('PARABÉNS, VOCÊ ACERTOU!')
else:
    print(f'você errou, o número era {computador}')