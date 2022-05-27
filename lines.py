import pygame

from spiral import *
from balls import *

# top horizontal
road1 = draw.line(window, (0, 0, 0), (100, 100), (900, 100), 1)
# middle horizontal
road2 = draw.line(window, (0, 0, 0), (100, 300), (900, 300), 1)
# bottom horizontal
road5 = draw.line(window, (0, 0, 0), (100, 600), (900, 600), 1)
# higher vertical
road3 = draw.line(window, (0, 0, 0), (900, 100), (900, 300), 1)
# lower vertical
road4 = draw.line(window, (0, 0, 0), (100, 300), (100, 600), 1)

horizRoads = [road1, road2, road5]
vertRoads = [road3, road4]


def map1(ball):
    draw.line(window, (0, 0, 0), (100, 100), (900, 100), 1)
    draw.line(window, (0, 0, 0), (100, 300), (900, 300), 1)
    draw.line(window, (0, 0, 0), (100, 600), (900, 600), 1)
    draw.line(window, (0, 0, 0), (900, 100), (900, 300), 1)
    draw.line(window, (0, 0, 0), (100, 300), (100, 600), 1)

    if ball.rect.colliderect(horizRoads[ball.road_h]):
        ball.move(0, ball.x_move)

    if ball.rect.colliderect(vertRoads[ball.road_v]) or (ball.road_v >= 1 and ball.rect.colliderect(vertRoads[ball.road_v - 1])):
        ball.move(1, ball.y_move)

    if ball.rect.colliderect(horizRoads[ball.road_h]) and ball.rect.colliderect(vertRoads[ball.road_v]):
        if ball.road_v + 1 < len(vertRoads):
            ball.road_v += 1
        if ball.road_h + 1 < len(horizRoads):
            ball.road_h += 1
            ball.x_move *= -1

def map2(ball):

    roadVert = pygame.draw.line(window, (255, 255, 255), (900, 100), (900, 500), 1)

    road1=pygame.draw.line(window, (0, 0, 0), (100, 100), (900, 100), 1)

    road2=pygame.draw.line(window, (0, 0, 0), (100, 220), (900, 220), 1)

    road3=pygame.draw.line(window, (0, 0, 0), (100, 340), (900, 340), 1)

    road4 = pygame.draw.line(window, (0, 0, 0), (100, 460), (900, 460), 1)

    horizRoads=[road1, road2, road3, road4]

    if ball.rect.colliderect(horizRoads[ball.road_h]):
        ball.move(0, ball.x_move)

    if ball.pos[0] >= 900 and ball.road_h < 3:
        yCoordinate = ball.positionY()
        ball.changePos(100, yCoordinate + 120)
        ball.road_h += 1

def map3(ball):
    added = True
    road1=pygame.draw.line(window, (0, 0, 0), (100, 100), (800, 100), 1)
    road2=pygame.draw.line(window, (0, 0, 0), (800, 100), (800, 200), 1)
    road3=pygame.draw.line(window, (0, 0, 0), (100, 200), (800, 200), 1)
    teleport1=pygame.draw.line(window, (0,0,0), (101,199), (101,201),1)

    road4 = pygame.draw.line(window, (0, 0, 0), (1000-100, 100+450), (1000-801, 100+450), 1)
    road5 = pygame.draw.line(window, (0, 0, 0), (1000-800, 99+450), (1000-800, 201+450), 1)
    road6 = pygame.draw.line(window, (0, 0, 0), (1000-100, 199+450), (1000-801, 199+450), 1)

    horizRoads=[road1, road3, road4, road6]
    vertRoads=[road2, road5]
    horizRoadsMove=[1,-1,-1,1]

    if ball.rect.colliderect(horizRoads[ball.road_h]):
        ball.x_move = abs(ball.x_move) * horizRoadsMove[ball.road_h]
        ball.move(0, ball.x_move)

    if ball.road_v < 2 and ball.rect.colliderect(vertRoads[ball.road_v]):
        ball.move(1, ball.y_move)

        added = False

    if ball.rect.colliderect(horizRoads[3]) and ball.rect.colliderect(vertRoads[1]) and not added:
        ball.road_v = 0
        # ball.road_h = math.ceil(ball.road_h/2)
    elif ball.rect.colliderect(horizRoads[0]) and ball.rect.colliderect(vertRoads[0]) and not added:
        ball.road_h = 1
    elif ball.rect.colliderect(horizRoads[2]) and ball.rect.colliderect(vertRoads[1]) and not added:
        ball.road_v = 1
        ball.road_h = 3

    # if ball.rect.colliderect(horizRoads[3]) and ball.rect.colliderect(vertRoads[1]) and not added:
    #     ball.road_h = 3
    elif ball.rect.colliderect(teleport1):
        ball.changePos(1000-100, 100+450)
        ball.road_v = 1
        ball.road_h = 2
