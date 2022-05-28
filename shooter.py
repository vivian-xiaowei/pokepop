import math
from math import *

import pygame.transform

from balls import *


def rotate_shooter(window, x, y, mouse_pos, image):
    run, rise = (mouse_pos[0]-x, mouse_pos[1]-y)
    angle = math.degrees(math.atan2(rise, run))

    rotimage = pygame.transform.rotate(image, -angle - 90)
    rect = rotimage.get_rect(center=(x, y))
    window.blit(rotimage, rect)


def follow_shooter(window, ball, center, distance, pos):
    run, rise = (pos[0] - center[0], center[1] - pos[1])
    diff = sqrt(pow(run, 2) + pow(rise, 2))
    x = center[0] + run / diff * distance - ball.rect.width/2
    y = center[1] - rise / diff * distance - ball.rect.height/2
    ball.pos = x, y
    ball.rect.center = ball.pos
    if rise > 0:
        ball.angle = -atan((pygame.mouse.get_pos()[0] - 500)/(450 - pygame.mouse.get_pos()[1])) * 180 / math.pi
    elif rise < 0:
        ball.angle = -atan((pygame.mouse.get_pos()[0] - 500) / (450 - pygame.mouse.get_pos()[1])) * 180 / math.pi + 180
    elif run < 0:
        ball.angle = 90
    else:
        ball.angle = 270


def draw_shooter(map, window, front, back):
    if map == 0:
        center = [500, 450]
        shooter = pygame.image.load("shooter 1.png")
        shooter = pygame.transform.scale(shooter, (112, 190))
        follow_shooter(window, front, center, 85, pygame.mouse.get_pos())
        front.draw(window)
        follow_shooter(window, back, center, -35, pygame.mouse.get_pos())
        back.angle += 180
        back.draw(window)
        rotate_shooter(window, center[0], center[1], pygame.mouse.get_pos(), shooter)
