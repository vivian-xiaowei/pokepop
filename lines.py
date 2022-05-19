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


def follow_lines(ball_pos, ball_rect, horizRoad, vertRoad, xmove):
    global added
    added=True
    pygame.draw.line(window, (0, 0, 0), (100, 100), (900, 100), 1)
    pygame.draw.line(window, (0, 0, 0), (101, 300), (901, 300), 1)
    pygame.draw.line(window, (0, 0, 0), (900, 99), (900, 301), 1)
    pygame.draw.line(window, (0, 0, 0), (100, 299), (100, 501), 1)
    pygame.draw.line(window, (0, 0, 0), (100, 500), (900, 500), 1)

    # rolling = pygame.transform.rotate(ball_images[colour][pos], 90)
    # window.blit(rolling, (int(coordinates[0]), int(coordinates[1])))
    # circle = rolling.get_rect()
    # circle.center = coordinates
    #print(vertRoad)

    if ball_rect.colliderect(horizRoads[horizRoad]) :
        ball_pos[0] += xmove

    if ball_rect.colliderect(vertRoads[vertRoad]) or (vertRoad>=1 and ball_rect.colliderect(vertRoads[vertRoad-1])):
        ball_pos[1] += 0.8


    if ball_rect.colliderect(horizRoads[horizRoad]) and ball_rect.colliderect(vertRoads[vertRoad]):
        added = False
        if vertRoad + 1 < len(vertRoads):
            vertRoad += 1
        if horizRoad + 1 < len(horizRoads):
            horizRoad += 1
            xmove *= -1

    return ball_pos, horizRoad, vertRoad, xmove

