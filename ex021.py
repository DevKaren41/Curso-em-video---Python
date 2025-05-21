import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
pygame.event.wait()
input('Qual é a musica?')