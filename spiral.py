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
    distance = 0
    slope = []
    for i in range(400):
        sub = distance / 3
        x_pos = WIN_X / 2 + math.cos(distance / 3) * distance * 7 # i * math.pi / 300) * distance * 1.4
        y_pos = WIN_Y / 2 + math.sin(distance / 3) * distance * 5 # i * math.pi / 300) * distance + 30
        point_distance = sqrt(pow(spiral_x[len(spiral_x) - 1] - x_pos, 2) + pow(spiral_y[len(spiral_x) - 1] - y_pos, 2))
        if point_distance >= 30:
            spiral_x.append(x_pos)
            spiral_y.append(y_pos)
            slope.append((sin(sub) + sub * cos(sub)) / cos(sub) - sub * sin(sub))
        distance += 0.18

    return spiral_x, spiral_y, slope


def map2(spiral_x, spiral_y):
    start = 0
    lines = [pygame.draw.line(window, (0, 0, 0), (spiral_x[start], spiral_y[start]), (spiral_x[start+1], spiral_y[start+1]), 1)]
    for i in range(start+2, len(spiral_x)):
        lines.append(
            pygame.draw.line(window, (0, 0, 0), (spiral_x[i - 1], spiral_y[i - 1]), (spiral_x[i], spiral_y[i]), 1))
        if i >= 1402:
            lines.append(
                pygame.draw.line(window, (0, 0, 255), (spiral_x[i - 1], spiral_y[i - 1]), (spiral_x[i], spiral_y[i]), 1))

    return lines


def follow_spiral(ball, slopes, s_x, s_y):
    ball.x, ball.y = ball.pos
    for i in range(len(slopes)):
        if ball.collide(window, s_x[i-1], s_y[i-1], s_x[i], s_y[i]):
            if slopes[i] >= 0:
                ball.x += 1 / sqrt(slopes[i] * slopes[i] + 1)
                ball.y += slopes[i] / sqrt(slopes[i] * slopes[i] + 1)
            else:
                ball.x += 1 / sqrt(slopes[i] * slopes[i] + 1)
                ball.y -= slopes[i] / sqrt(slopes[i] * slopes[i] + 1)
    ball.pos = ball.x, ball.y
