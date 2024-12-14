'''21 - Faça um programa em Python que abra e reproduza um arquivo MP3. '''
import pygame
pygame.init()
pygame.mixer.music.load('arquivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()