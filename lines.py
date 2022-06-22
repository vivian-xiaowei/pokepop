from setup import *
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
ending1 = pygame.draw.line(window, (0, 0, 0), (885, 600), (885, 615), 1)
horizRoads1 = [road1, road2, road5]
vertRoads1 = [road3, road4]
hmove = [1, 0, -1, 0, 1]
vmove = [0, 1, 0, 1, 0]

# map 2: horizontal lines top to bottom
road1 = pygame.draw.line(window, (0, 0, 0), (50, 100), (930, 100), 1)
road2 = pygame.draw.line(window, (0, 0, 0), (50, 220), (930, 220), 1)
road3 = pygame.draw.line(window, (0, 0, 0), (50, 340), (930, 340), 1)
road4 = pygame.draw.line(window, (0, 0, 0), (50, 460), (930, 460), 1)
ending2 = pygame.draw.line(window, (0, 0, 0), (877, 465), (877, 475), 1)
horizRoads2 = [road1, road2, road3, road4]

# map 3
road1 = pygame.draw.line(window, (0, 0, 0), (100, 110), (920, 110), 1)
road2 = pygame.draw.line(window, (0, 0, 0), (910, 665), (90, 665), 1)
road3 = pygame.draw.line(window, (0, 0, 0), (90, 265), (700, 265), 1)

road4 = pygame.draw.line(window, (0, 0, 0), (920, 110), (920, 650), 1)
road5 = pygame.draw.line(window, (0, 0, 0), (75, 650), (75, 275), 1)
road6 = pygame.draw.line(window, (0, 0, 0), (700, 275), (700, 400), 1)
ending3 = pygame.draw.line(window, (0, 0, 0), (685, 430), (695, 430), 1)
horizRoads3 = [road1, road2, road3]
vertRoads3 = [road4, road5, road6]
horizRoadsMove = [1, 0, -1, 0, 1, 0]
vertRoadsMove = [0, 1, 0, -1, 0, 1]
horizontals = [horizRoads1, horizRoads2, horizRoads3]
verticles = [vertRoads1, None, vertRoads3]



def map1(ball, speeding=True):
    horizRoads = horizRoads1
    vertRoads = vertRoads1
    rect = ball.rect
    speed_collide = speeding and ((ball.y_move == ball.speed and ball.pos[1] + 30 >= bottom) or (ball.x_move == -1 * ball.speed and ball.pos[0] <= left))

    if ball.road_h < 3 and ball.road_v < 2 and rect.colliderect(horizRoads[ball.road_h]) and rect.colliderect(vertRoads[int(ball.road_v)]) or speed_collide:
        if (ball.road_h == 1 and ball.pos[0] >= 888) or (ball.road_h == 2 and ball.pos[0] <= 111):
            ball.road_v += 1
        if ball.road_h + 1 < len(horizRoads) and ball.y_move == 0:
            ball.road_h += 1
        ball.y_move = ball.speed * vmove[ball.road_h + ball.road_v]
        ball.x_move = ball.speed * hmove[ball.road_h + ball.road_v]
    elif ending1.colliderect(ball):
        return True
    elif ball.pos[0] >= 990:
        ball.x_move = 0
        ball.y_move = 0
    return speeding


def map2(ball, speeding=True):
    if ball.pos[0] >= 910 and ball.road_h < 3:
        ball.pos = [55, ball.pos[1] + 120]
        ball.road_h += 1
    if ball.pos[0] > 1000:
        ball.x_move = 0
        ball.y_move = 0
    if ending2.colliderect(ball):
        return True
    return speeding


def map3(ball, speeding=True):
    horizRoads = horizRoads3
    vertRoads = vertRoads3

    speed_collide = speeding and ((int(ball.pos[1]) == 263 and ball.pos[0] == 672) or (int(ball.pos[1]) == 263 and ball.pos[0] == 75) or (int(ball.pos[1]) == 638 and ball.pos[0] == 75))

    if ball.road_h < 3 and ball.road_v < 3 and ball.rect.colliderect(horizRoads[ball.road_h]) and ball.rect.colliderect(
            vertRoads[ball.road_v]) or speed_collide:
        if WIN_Y / WIN_X + 1 >= (WIN_Y - ball.pos[1]) / ball.pos[0] >= WIN_Y / WIN_X - 0.1:
            # if ball.road_h + 1 < len(horizRoads):
            ball.road_h += 1
            # else:
            #     ball.road_h = 0
        else:
            # if ball.road_v + 1 < len(vertRoads):
            ball.road_v += 1
        ball.x_move = ball.speed * horizRoadsMove[ball.road_h + ball.road_v]  # * horizRoadsMove[int(ball.road_h)]
        ball.y_move = ball.speed * vertRoadsMove[ball.road_h + ball.road_v]  # * vertRoadsMove[int(ball.road_v)]
    elif ending3.colliderect(ball):
        ball.x_move = 0
        ball.y_move = 0
        return True
    return speeding
