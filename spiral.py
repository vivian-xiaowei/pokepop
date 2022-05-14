import pygame
from pygame import *
import math
pygame.init()
clock = pygame.time.Clock()

width = 1000
height = 750
window = pygame.display.set_mode((1000, 750))

spiral_x = []
spiral_y = []


def spiral():
    distance = 1
    for angle in range(100):
        x_pos = width / 2 + math.cos(angle * math.pi / 16) * distance
        y_pos = height / 2 + math.sin(angle * math.pi / 16) * distance
        spiral_x.append(x_pos)
        spiral_y.append(y_pos)
        distance += 4
    print(spiral_x)
    print(spiral_y)


window.fill((255, 255, 255))
pygame.display.update()

spiral()

while True:
    clock.tick(60)
    for i in range(len(spiral_x)):
        pygame.draw.circle(window, (0, 0, 0), (spiral_x[i], spiral_y[i]), 1, 1)

    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or key[K_ESCAPE]:
            quit()

    pygame.display.update()
