#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com um pausa de 1 segundo entre eles

from time import sleep
import emoji
print('A queima de artifícios vai começar!!')
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.2)
print(emoji.emojize("Bum:fireworks:"))
fogos = emoji.emojize(' :fireworks:')
print(fogos*5)
