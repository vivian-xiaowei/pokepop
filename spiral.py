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
    distance = 120
    slope = []
    for i in range(1450):
        x_pos = WIN_X / 2 + math.cos(i * math.pi / 300) * distance * 1.4
        y_pos = WIN_Y / 2 - math.sin(i * math.pi / 300) * distance + 30
        point_distance = sqrt(pow(spiral_x[len(spiral_x) - 1] - x_pos, 2) + pow(spiral_y[len(spiral_x) - 1] - y_pos, 2))
        if i > 1400 and point_distance >= 30:
            print(i)
            print(sqrt(pow(spiral_x[len(spiral_x) - 1] - 500, 2) + pow(spiral_y[len(spiral_x) - 1] - 375, 2)))
            print((y_pos - spiral_y[len(spiral_x) - 1]) / (x_pos - spiral_x[len(spiral_x) - 1]))
            print(atan((y_pos - spiral_y[len(spiral_x) - 1]) / (x_pos - spiral_x[len(spiral_x) - 1])))
        if point_distance >= 30:
            spiral_x.append(x_pos)
            spiral_y.append(y_pos)
        distance += 0.18

    return spiral_x, spiral_y, slope


def draw_spiral(spiral_x, spiral_y):
    start = 0
    lines = [pygame.draw.line(window, (0, 0, 0), (spiral_x[start], spiral_y[start]), (spiral_x[start+1], spiral_y[start+1]), 1)]
    slope = [[] in range(2)]
    for i in range(start+2, len(spiral_x)):
        lines.append(
            pygame.draw.line(window, (0, 0, 0), (spiral_x[i - 1], spiral_y[i - 1]), (spiral_x[i], spiral_y[i]), 1))
        if i >= 1402:
            lines.append(
                pygame.draw.line(window, (0, 0, 255), (spiral_x[i - 1], spiral_y[i - 1]), (spiral_x[i], spiral_y[i]), 1))

        slope.append([(spiral_x[i - 1] - spiral_x[i]) / 30, (spiral_y[i - 1] - spiral_y[i]) / 30])
    return lines, slope


def follow_spiral(ball, slopes):
    ball.x, ball.y = ball.pos
    distance = sqrt(pow(ball.x - WIN_X / 2, 2) + pow(ball.y - WIN_Y / 2, 2))
    ball.x = WIN_X / 2 + ball.distance * math.cos(ball.circle_angle)
    ball.y = WIN_Y / 2 + ball.distance * math.sin(ball.circle_angle)

    ball.pos = ball.x, ball.y
