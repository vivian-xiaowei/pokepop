from spiral import *
from balls import *

# map 1
left = 112
right = 916
top = 100
middle = 321
bottom = 620
road1 = draw.line(window, (0, 0, 0), (0, top), (right, top), 1)  # top horizontal
road2 = draw.line(window, (0, 0, 0), (left, middle), (right, middle), 1)  # middle horizontal
road5 = draw.line(window, (0, 0, 0), (left, bottom), (right, bottom), 1)  # bottom horizontal
road3 = draw.line(window, (0, 0, 0), (right, top), (right, middle), 1)  # higher vertical
road4 = draw.line(window, (0, 0, 0), (left, middle), (left, bottom), 1)  # lower vertical
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

multiplier = 1


def map1(ball):
    global multiplier
    horizRoads = horizRoads1
    vertRoads = vertRoads1

    if ball.x_move != 0:
        speed = abs(ball.x_move) * multiplier
    else:
        speed = abs(ball.y_move) * multiplier

    if int(ball.road_v) < 2 and ball.rect.colliderect(horizRoads[ball.road_h]) and ball.rect.colliderect(
            vertRoads[int(ball.road_v)]):
        ball.y_move = speed - ball.y_move
        if ball.pos[0] > WIN_X / 2:
            ball.x_move -= speed
        else:
            ball.x_move += speed
        if ball.road_v == 1.5:
            ball.road_v = 0
        else:
            ball.road_v += 0.5

        if ball.road_h + 1 < len(horizRoads) and ball.y_move == 3:
            ball.road_h += 1
    elif ball.rect.colliderect(horizRoads[ball.road_h]):
        if ball.road_h == 0 or ball.road_h == 2:
            ball.x_move = speed
        else:
            ball.x_move = -1 * speed
        ball.y_move = 0
    else:
        ball.y_move = speed
        ball.x_move = 0

    ending = pygame.draw.line(window, (0, 0, 0), (882, 600), (882, 615), 1)
    if ending.colliderect(ball):
        multiplier = 1.25
    if ball.pos[0] >= 990:
        ball.x_move = 0
        ball.y_move = 0


def map2(ball):
    global multiplier

    if ball.pos[0] >= 910 and ball.road_h < 3:
        yCoordinate = ball.positionY()
        ball.changePos(55, yCoordinate + 120)
        ball.road_h += 1
    ending = pygame.draw.line(window, (0, 0, 0), (877, 465), (877, 475), 1)
    if ending.colliderect(ball):
        multiplier = 5
    if ball.speed == ball.x_move:
        ball.x_move *= multiplier


def map3(ball):
    global multiplier
    road1 = pygame.draw.line(window, (0, 0, 0), (100, 110), (920, 110), 1)
    road2 = pygame.draw.line(window, (0, 0, 0), (910, 665), (90, 665), 1)
    road3 = pygame.draw.line(window, (0, 0, 0), (90, 265), (700, 265), 1)

    road4 = pygame.draw.line(window, (0, 0, 0), (920, 110), (920, 650), 1)
    road5 = pygame.draw.line(window, (0, 0, 0), (75, 650), (75, 275), 1)
    road6 = pygame.draw.line(window, (0, 0, 0), (700, 275), (700, 400), 1)
    horizRoads = [road1, road2, road3]
    vertRoads = [road4, road5, road6]
    horizRoadsMove = [1, -1, 1]
    vertRoadsMove = [1, -1, 1]

    if ball.rect.colliderect(horizRoads[ball.road_h]):
        ball.x_move = ball.speed * horizRoadsMove[ball.road_h] * multiplier
        ball.y_move = 0

    elif ball.rect.colliderect(vertRoads[ball.road_v]):
        ball.y_move = ball.speed * vertRoadsMove[ball.road_v] * multiplier
        ball.x_move = 0

    if ball.rect.colliderect(horizRoads[2]) and ball.rect.colliderect(vertRoads[2]):
        ball.road_v = 2
        ball.road_h = 2
        ball.y_move = ball.speed * vertRoadsMove[ball.road_v] * multiplier
        ball.x_move = 0
    elif ball.rect.colliderect(horizRoads[ball.road_h]) and ball.rect.colliderect(vertRoads[ball.road_v]):
        if ball.pos[0] > WIN_X / 2:
            ball.road_h += 1
        if ball.pos[1] > WIN_Y / 2:
            ball.road_v += 1
    if ball.road_v == 2 and ball.road_h == 2 and not ball.rect.colliderect(vertRoads[2]):
        ball.x_move = 0
        ball.y_move = 0
        print(ball.pos)
    # if ball.road_v == 2 and ball.road_h == 2 and ball.pos[0]

    ending = pygame.draw.line(window, (0, 0, 0), (685, 400), (695, 400), 1)

    if ending.colliderect(ball):
        multiplier = 3
