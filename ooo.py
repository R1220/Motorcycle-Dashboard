import sys
import math
import os
import pygame
pygame.init()
size = width, height = 1024, 768
black = 0, 0, 0
speed = [2, 2]
screen = pygame.display.set_mode(size)
dash = pygame.image.load ("cap.jpg")
dashrect = dash.get_rect()
background = black
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    dashrect = dashrect.move(speed)

    if dashrect.left < 0 or dashrect.right > width:
        speed [0] = -speed[0]
    if dashrect.top < 0 or dashrect.bottom >height:
        speed[1] = -speed[1]
    screen.fill  (black)
    screen.blit(dash, dashrect)
    pygame.display.flip()

