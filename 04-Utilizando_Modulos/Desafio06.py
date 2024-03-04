# Faça um programa em Python que abara e reproduza o áudio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()