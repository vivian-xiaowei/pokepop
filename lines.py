import pygame

from main import *


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

xmove = 1


def follow_lines():
    global added, horizRoad, xmove, vertRoad
    road1 = draw.line(window, (0, 0, 0), (100, 100), (900, 100), 1)

    road2 = pygame.draw.line(window, (0, 0, 0), (101, 300), (901, 300), 1)

    road3 = pygame.draw.line(window, (0, 0, 0), (900, 99), (900, 301), 1)

    road4 = pygame.draw.line(window, (0, 0, 0), (100, 299), (100, 501), 1)

    road5 = pygame.draw.line(window, (0, 0, 0), (100, 500), (900, 500), 1)

    ball = pygame.image.load("1.png")
    window.blit(ball, coordinates)
    circle = ball.get_rect()
    circle.center = coordinates
    # pygame.draw.circle(window, (0, 0, 0), coordinates, 5)

    if circle.colliderect(horizRoads[horizRoad]):
        coordinates[0] += xmove
    else:
        if horizRoad + 1 < len(horizRoads) and added == False:
            horizRoad += 1
            xmove *= -1
            added = True
    if circle.colliderect(vertRoads[vertRoad]) == True:
        coordinates[1] += 1
    else:
        if vertRoad + 1 < len(vertRoads) and added == False:
            vertRoad += 1
            added = True

    if circle.colliderect(horizRoads[horizRoad]) == True and circle.colliderect(vertRoads[vertRoad]) == True:
        added = False