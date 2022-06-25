from setup import *
from balls import *

# map 1: position, the lines, end, lists of lines and separate vertical and horizontal speed
left, right = 112, 916
top, middle, bottom = 100, 321, 620
road1 = draw.line(window, (0, 0, 0), (0, top), (right, top), 1)  # top horiz
road2 = draw.line(window, (0, 0, 0), (left, middle), (right, middle), 1)  # middle horiz
road5 = draw.line(window, (0, 0, 0), (left, bottom), (right, bottom), 1)  # bottom horiz
road3 = draw.line(window, (0, 0, 0), (right, top), (right, middle), 1)  # higher vert
road4 = draw.line(window, (0, 0, 0), (left, middle), (left, bottom), 1)  # lower vert
ending1 = pygame.draw.line(window, (0, 0, 0), (885, 600), (885, 615), 1)
horizRoads1 = [road1, road2, road5]
vertRoads1 = [road3, road4]
hmove = [1, 0, -1, 0, 1]
vmove = [0, 1, 0, 1, 0]

# map 2: no need to use lines
ending2 = pygame.draw.line(window, (0, 0, 0), (877, 465), (877, 475), 1)

# map 3: the lines, end, lists of lines and separate vertical and horizontal speed
road1 = pygame.draw.line(window, (0, 0, 0), (100, 110), (920, 110), 1)  # top horiz
road2 = pygame.draw.line(window, (0, 0, 0), (910, 665), (90, 665), 1)  # bottom horiz
road3 = pygame.draw.line(window, (0, 0, 0), (90, 265), (700, 265), 1)  # middle horiz
road4 = pygame.draw.line(window, (0, 0, 0), (920, 110), (920, 650), 1)  # right vert
road5 = pygame.draw.line(window, (0, 0, 0), (75, 650), (75, 275), 1)  # left vert
road6 = pygame.draw.line(window, (0, 0, 0), (700, 275), (700, 400), 1)  # middle vert
ending3 = pygame.draw.line(window, (0, 0, 0), (685, 430), (695, 430), 1)
horizRoads3 = [road1, road2, road3]
vertRoads3 = [road4, road5, road6]
horizRoadsMove = [1, 0, -1, 0, 1, 0]
vertRoadsMove = [0, 1, 0, -1, 0, 1]


def map1(ball, speeding=True):
    horizRoads = horizRoads1
    vertRoads = vertRoads1
    rect = ball.rect
    # the correct collision when it's speeding
    speed_collide = speeding and ((ball.y_move == ball.speed and ball.pos[1] + 30 >= bottom) or (ball.x_move == -1 * ball.speed and ball.pos[0] <= left))
    # when the ball collide with both roads or speeding collision
    if ball.road_h < 3 and ball.road_v < 2 and rect.colliderect(horizRoads[ball.road_h]) and rect.colliderect(vertRoads[int(ball.road_v)]) or speed_collide:
        # increase vertical road when changing from vertical to horizontal movement
        if (ball.road_h == 1 and ball.pos[0] >= 888) or (ball.road_h == 2 and ball.pos[0] <= 111):
            ball.road_v += 1
        # increase horizontal road when not moving vertically
        if ball.road_h + 1 < len(horizRoads) and ball.y_move == 0:
            ball.road_h += 1
        # use the road number the ball is on to adjust the speed in different directions
        ball.y_move = ball.speed * vmove[ball.road_h + ball.road_v]
        ball.x_move = ball.speed * hmove[ball.road_h + ball.road_v]
    elif ending1.colliderect(ball):
        return True  # change speeding to true when ball collide with end
    elif ball.pos[0] >= 990:  # stop ball after passing the end
        ball.x_move = 0
        ball.y_move = 0
    return speeding  # don't change the speeding value


def map2(ball, speeding=True):
    # change to next line after passing a point on the right for the first 3 lines
    if ball.pos[0] >= 910 and ball.road_h < 3:
        ball.pos = [55, ball.pos[1] + 120]
        ball.road_h += 1
    # stop ball after passing the end
    if ball.pos[0] > 1000:
        ball.x_move = 0
        ball.y_move = 0
    if ending2.colliderect(ball):
        return True  # change speeding to true when ball collide with end
    return speeding


def map3(ball, speeding=True):
    # similar logic as the first map
    horizRoads = horizRoads3
    vertRoads = vertRoads3
    # the correct collision when speeding
    speed_collide = speeding and ((int(ball.pos[1]) == 263 and ball.pos[0] == 672) or (int(ball.pos[1]) == 263 and ball.pos[0] == 75) or (int(ball.pos[1]) == 638 and ball.pos[0] == 75))
    # ball collide with both roads or speeding collision
    if ball.road_h < 3 and ball.road_v < 3 and ball.rect.colliderect(horizRoads[ball.road_h]) and ball.rect.colliderect(
            vertRoads[ball.road_v]) or speed_collide:
        # increase horizontal road at the turning point near window diagonal, otherwise, increase vertical road
        if WIN_Y / WIN_X + 1 >= (WIN_Y - ball.pos[1]) / ball.pos[0] >= WIN_Y / WIN_X - 0.1:
            ball.road_h += 1
        else:
            ball.road_v += 1
        # use the road number the ball is on to adjust the speed in different directions
        ball.x_move = ball.speed * horizRoadsMove[ball.road_h + ball.road_v]
        ball.y_move = ball.speed * vertRoadsMove[ball.road_h + ball.road_v]
    # when collide with end, stop and change speeding to true
    elif ending3.colliderect(ball):
        ball.x_move = 0
        ball.y_move = 0
        return True
    return speeding  # don't change the speeding value
