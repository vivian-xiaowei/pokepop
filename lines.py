from spiral import *
from balls import *

# map 1
road1 = draw.line(window, (0, 0, 0), (100, 100), (900, 100), 1)  # top horizontal
road2 = draw.line(window, (0, 0, 0), (100, 300), (900, 300), 1)  # middle horizontal
road5 = draw.line(window, (0, 0, 0), (100, 600), (900, 600), 1)  # bottom horizontal
road3 = draw.line(window, (0, 0, 0), (900, 100), (900, 300), 1)  # higher vertical
road4 = draw.line(window, (0, 0, 0), (100, 300), (100, 600), 1)  # lower vertical
horizRoads1 = [road1, road2, road5]
vertRoads1 = [road3, road4]

# map 2: horizontal lines top to bottom
road1 = pygame.draw.line(window, (0, 0, 0), (50, 100), (930, 100), 1)
road2 = pygame.draw.line(window, (0, 0, 0), (50, 220), (930, 220), 1)
road3 = pygame.draw.line(window, (0, 0, 0), (50, 340), (930, 340), 1)
road4 = pygame.draw.line(window, (0, 0, 0), (50, 460), (930, 460), 1)
horizRoads2 = [road1, road2, road3, road4]

# map 3
road1 = pygame.draw.line(window, (0, 0, 0), (100, 100), (800, 100), 1)
road2 = pygame.draw.line(window, (0, 0, 0), (800, 100), (800, 200), 1)
road3 = pygame.draw.line(window, (0, 0, 0), (100, 200), (800, 200), 1)
teleport1 = pygame.draw.line(window, (0, 0, 0), (101, 199), (101, 201), 1)

road4 = pygame.draw.line(window, (0, 0, 0), (1000 - 100, 100 + 450), (1000 - 801, 100 + 450), 1)
road5 = pygame.draw.line(window, (0, 0, 0), (1000 - 800, 99 + 450), (1000 - 800, 201 + 450), 1)
road6 = pygame.draw.line(window, (0, 0, 0), (1000 - 100, 199 + 450), (1000 - 801, 199 + 450), 1)

horizRoads3 = [road1, road3, road4, road6]
vertRoads3 = [road2, road5]


def map1(ball):
    horizRoads = horizRoads1
    vertRoads = vertRoads1

    if ball.rect.colliderect(horizRoads[ball.road_h]):
        ball.move(0, ball.x_move)

    if ball.rect.colliderect(vertRoads[ball.road_v]) or (
            ball.road_v >= 1 and ball.rect.colliderect(vertRoads[ball.road_v - 1])):
        ball.move(1, ball.y_move)

    if ball.rect.colliderect(horizRoads[ball.road_h]) and ball.rect.colliderect(vertRoads[ball.road_v]):
        if ball.road_v + 1 < len(vertRoads):
            ball.road_v += 1
        if ball.road_h + 1 < len(horizRoads):
            ball.road_h += 1
            ball.x_move *= -1


def map2(ball):
    horizRoads = horizRoads2

    if ball.rect.colliderect(horizRoads[ball.road_h]):
        ball.move(0, ball.x_move)

    if ball.pos[0] >= 910 and ball.road_h < 3:
        yCoordinate = ball.positionY()
        ball.changePos(55, yCoordinate + 120)
        ball.road_h += 1


def map3(ball):
    added = True
    horizRoads = horizRoads3
    vertRoads = vertRoads3
    horizRoadsMove = [1, -1, -1, 1]

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

    elif ball.rect.colliderect(teleport1):
        ball.changePos(1000 - 100, 100 + 450)
        ball.road_v = 1
        ball.road_h = 2
