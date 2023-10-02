#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3

import pygame
pygame.init()
pygame.mixer_music.load('nomearquivo.mp3')
pygame.mixer_music.play()

input()
pygame.event.wait()


#'outra alternativa'
#from playsound import playsound
#playsound('ex021.mp3')