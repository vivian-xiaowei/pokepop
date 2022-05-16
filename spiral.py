import pygame
from pygame import *
import math

width = 1000
height = 750
window = pygame.display.set_mode((1000, 750))


def spiral():
    spiral_x = []
    spiral_y = []
    distance = 1
    for angle in range(96):
        x_pos = width / 2 + math.cos(angle * math.pi / 16) * distance
        y_pos = height / 2 + math.sin(angle * math.pi / 16) * distance
        spiral_x.append(x_pos)
        spiral_y.append(y_pos)
        distance += 4
    return spiral_x, spiral_y


def draw_spiral(spiral_x, spiral_y):
    for i in range(len(spiral_x)):
        pygame.draw.circle(window, (0, 0, 0), (spiral_x[i], spiral_y[i]), 1, 1)