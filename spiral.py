import sys
import pygame
from pygame import *
import math
from math import *
from balls import *

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
    for i in range(2000):
        x_pos = WIN_X / 2 + math.cos(i * math.pi / 300) * distance * 1.4
        y_pos = WIN_Y / 2 - math.sin(i * math.pi / 300) * distance + 30
        point_distance = sqrt(pow(spiral_x[len(spiral_x) - 1] - x_pos, 2) + pow(spiral_y[len(spiral_x) - 1] - y_pos, 2))
        if point_distance >= 30:
            spiral_x.append(x_pos)
            spiral_y.append(y_pos)
        distance += 0.18

    return spiral_x, spiral_y


def draw_spiral(spiral_x, spiral_y):
    start = 0
    lines = [pygame.draw.line(window, (0, 0, 0), (spiral_x[start], spiral_y[start]), (spiral_x[start+1], spiral_y[start+1]), 1)]
    slope = [[] in range(2)]
    for i in range(start+2, len(spiral_x)):
        lines.append(
            pygame.draw.line(window, (0, 0, 0), (spiral_x[i - 1], spiral_y[i - 1]), (spiral_x[i], spiral_y[i]), 1))
        slope.append([(spiral_x[i-1]-spiral_x[i])/30, (spiral_y[i-1]-spiral_y[i])/30])
    return lines, slope


def follow_spiral(ball, lines, slopes):
    for count in range(len(lines)):
        if ball.rect.colliderect(lines[count]):
            print(slopes[i])
            ball.x_move = slopes[i][0]
            ball.y_move = slopes[i][1]
            ball.two_direction_move()
            break
