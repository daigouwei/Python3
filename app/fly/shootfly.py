#!/usr/bin/env
#-*- coding:utf-8 -*-

import pygame
from sys import exit
# from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((480, 800))
pygame.display.set_caption('SHOOT FLY')
# background = pygame.image.load('PythonShootGame/resources/image/background.png').convert()
background = pygame.image.load('PythonShootGame/resources/image/background.png')
game_over_img = pygame.image.load('PythonShootGame/resources/image/gameover.png')
plane_image = pygame.image.load('PythonShootGame/resources/image/shoot.png')
player_plane_image = plane_image.subsurface(pygame.Rect(0, 99, 102, 126))

while True:
    screen.fill(0)
    screen.blit(background, (0, 0))
    screen.blit(player_plane_image, (200, 600))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
