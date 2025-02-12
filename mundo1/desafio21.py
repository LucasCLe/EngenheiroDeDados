'''
    Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.

'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/lucas/Estudos/python/EngenheiroDeDados/mundo1/desafio021.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()