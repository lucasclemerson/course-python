import pygame
pygame.init()
pygame.mixer.music.load('exercicios/musica.mp3')
pygame.mixer.music.play()
pygame.event.wait(timeout=0)