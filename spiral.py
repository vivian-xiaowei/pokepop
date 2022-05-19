import sys
import pygame
from pygame import *
import math
from math import *
# from lines import *

pygame.init()
clock = time.Clock()

# setting up window size
WIN_X = int(1000)

# how tall the screen is going to be
WIN_Y = int(750)

# set the screen
window = pygame.display.set_mode((WIN_X, WIN_Y))


def spiral():
    spiral_x = [WIN_X / 2]
    spiral_y = [WIN_Y / 2]
    distance = 1
    for angle in range(600):
        x_pos = WIN_X / 2 + math.cos(angle * math.pi / 100) * distance
        y_pos = WIN_Y / 2 + math.sin(angle * math.pi / 100) * distance

        point_distance = sqrt(pow(spiral_x[len(spiral_x)-1] - x_pos, 2) + pow(spiral_y[len(spiral_x)-1] - y_pos, 2))
        if point_distance >= 20:
            spiral_x.append(x_pos)
            spiral_y.append(y_pos)
        distance += 0.6
    return spiral_x, spiral_y


def draw_spiral(spiral_x, spiral_y):
    # spiral_x, spiral_y = spiral()
    # print(spiral_x)
    # print(spiral_y)

    for i in range(len(spiral_x)):
        pygame.draw.circle(window, (0, 0, 0), (spiral_x[i], spiral_y[i]), 1, 1)