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

horizRoad = 0
vertRoad = 0

road = road1

xmove = 0.8


def follow_lines(colour, pos, ball_pos, ball_rect):
    global added, horizRoad, xmove, vertRoad
    pygame.draw.line(window, (0, 0, 0), (100, 100), (900, 100), 1)
    pygame.draw.line(window, (0, 0, 0), (101, 300), (901, 300), 1)
    pygame.draw.line(window, (0, 0, 0), (900, 99), (900, 301), 1)
    pygame.draw.line(window, (0, 0, 0), (100, 299), (100, 501), 1)
    pygame.draw.line(window, (0, 0, 0), (100, 500), (900, 500), 1)

    # rolling = pygame.transform.rotate(ball_images[colour][pos], 90)
    # window.blit(rolling, (int(coordinates[0]), int(coordinates[1])))
    # circle = rolling.get_rect()
    # circle.center = coordinates
    print(ball_rect.colliderect(horizRoads[horizRoad]))
    if ball_rect.colliderect(horizRoads[horizRoad]):
        ball_pos[0] += xmove
    else:
        if horizRoad + 1 < len(horizRoads) and added == False:
            horizRoad += 1
            xmove *= -1
            added = True
    if ball_rect.colliderect(vertRoads[vertRoad]):
        ball_pos[1] += 1
    else:
        if vertRoad + 1 < len(vertRoads) and added == False:
            vertRoad += 1
            added = True

    if ball_rect.colliderect(horizRoads[horizRoad]) and ball_rect.colliderect(vertRoads[vertRoad]):
        added = False

    return ball_pos
