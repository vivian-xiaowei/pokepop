import pygame

from spiral import *
from balls import *

coordinates = [100, 100]

road1 = draw.line(window, (0, 0, 0), (100, 100), (900, 100), 1)

road2 = draw.line(window, (0, 0, 0), (100, 300), (900, 300), 1)

road3 = draw.line(window, (0, 0, 0), (900, 100), (900, 300), 1)

road4 = draw.line(window, (0, 0, 0), (100, 300), (100, 500), 1)

road5 = draw.line(window, (0, 0, 0), (100, 500), (900, 500), 1)

horizRoads = [road1, road2, road5]
vertRoads = [road3, road4]

added = True

road = road1


def follow_lines(ball):
    global added
    added = True
    pygame.draw.line(window, (0, 0, 0), (100, 100), (900, 100), 1)
    pygame.draw.line(window, (0, 0, 0), (101, 300), (901, 300), 1)
    pygame.draw.line(window, (0, 0, 0), (900, 99), (900, 301), 1)
    pygame.draw.line(window, (0, 0, 0), (100, 299), (100, 501), 1)
    pygame.draw.line(window, (0, 0, 0), (100, 500), (900, 500), 1)

    if ball.rect.colliderect(horizRoads[ball.road_h]):
        ball.move(0, ball.x_move)

    if ball.rect.colliderect(vertRoads[ball.road_v]) or (ball.road_v >= 1 and ball.rect.colliderect(vertRoads[ball.road_v - 1])):
        ball.move(1, ball.y_move)

    if ball.rect.colliderect(horizRoads[ball.road_h]) and ball.rect.colliderect(vertRoads[ball.road_v]):
        added = False
        if ball.road_v + 1 < len(vertRoads):
            ball.road_v += 1
        if ball.road_h + 1 < len(horizRoads):
            ball.road_h += 1
            ball.x_move *= -1
