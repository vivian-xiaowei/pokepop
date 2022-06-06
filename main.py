import pygame.display
from pygame.image import load
from pygame.time import wait

from lines import *
from shooter import *


def game(map, level):
    global screen
    ball_list = generate_ball(level) # randomly generate a list of balls
    front = pokeballs(pick_ball(), -30, -30, 0, 0, 0)
    back = pokeballs(pick_ball(), -30, -30, 0, 0, 0)
    fly = []
    test = pokeballs(pick_ball(), 0, 0, 0, 0, 0)
    test.pos = 140, 515
    framerate = 60

    while True:
        push = -1
        clock.tick(framerate)

        # the bottom background
        window.blit(load("backgrounds/" + str(map) + "a.png"), (0, 0))
        # move the balls in the list base on the collision with lines
        for count in range(len(ball_list)):
            ball = ball_list[count]
            ball.rect.topleft = ball.pos
            # balls off the path at the start
            if ball.pos[0] < 100 and ball.pos[1] <= 100:
                ball.shooter_move(True)
                ball.rotate = ball_list[0].rotate
            else:
                balls_exist.add(ball.type)
                for fly_count in range(len(fly)):
                    flying = fly[fly_count]
                    if dist(ball.pos, flying.pos) <= 30:
                        for i in range(len(ball_list)-1, count, -1):
                            ball_list[i].type = ball_list[i-1].type
                        ball_list[count].type = flying.type
                        push = ball_list[len(ball_list) - 1].type
                        fly.remove(flying)

                        startingIndex, endingIndex = count, count
                        while startingIndex > 0:
                            if ball_list[startingIndex].type == ball_list[startingIndex - 1].type:
                                startingIndex -= 1
                            else:
                                break
                        while endingIndex < len(ball_list) - 2:
                            if ball_list[count].type == ball_list[endingIndex + 1].type:
                                endingIndex += 1
                            else:
                                break
                        if ball_list[endingIndex + 1].type == ball_list[count].type and endingIndex + 2 == len(ball_list):
                            endingIndex += 2
                        print("startingIndex", startingIndex)
                        print("endingIndex", endingIndex)
                        print(len(ball_list))
                        break
                if map == 0:
                    map1(ball)
                elif map == 1:
                    map2(ball)
                else:
                    map3(ball)
                ball.shooter_move(True)
                ball.draw(window)
        window.blit(load("backgrounds/" + str(map) + "b.png"), (0, 0))

        if push > -1:
            last = ball_list[len(ball_list)-1]
            x, y = last.pos
            X, Y = last.x_move, last.y_move
            if X != 0:
                x += 30 * X * -1 / abs(X)
            if Y != 0:
                y -= 30
            new_ball = pokeballs(push, x, y, last.rotate, last.x_move, last.y_move)
            new_ball.road_h, new_ball.road_v, new_ball.rect.topleft = last.road_h, last.road_v, new_ball.pos
            if not (new_ball.rect.colliderect(horizRoads1[new_ball.road_h]) or new_ball.rect.colliderect(vertRoads1[int(new_ball.road_v)])) and not new_ball.pos[0] < 10:
                if Y > 0:
                    if x > WIN_X/2:
                        x = last.pos[0] + (y - last.pos[1])
                        new_ball.road_v -= 0.5
                    else:
                        x = last.pos[0] - (y - last.pos[1])
                    y = last.pos[1]
                    new_ball.road_h -= 1
                else:
                    y = last.pos[1] - 30
                    x = last.pos[0]
                    new_ball.road_v -= 0.5
                    new_ball.y_move = abs(new_ball.x_move)
                    new_ball.x_move = 0
                new_ball.pos = [x, y]
            ball_list.append(new_ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system
            if event.type == pygame.MOUSEBUTTONUP:
                run, rise = (front.pos[0] + 14 - 500, front.pos[1] + 15 - 450)
                diff = sqrt(pow(run, 2) + pow(rise, 2))
                fly.append(front)
                fly[len(fly) - 1].x_move = run / diff * 20
                fly[len(fly) - 1].y_move = rise / diff * 20
                front = back
                back = pokeballs(pick_ball(), 0, 0, 0, 0, 0)

        if not fly == []:
            for count in range(len(fly)):
                ball = fly[count]
                if not(0 - 30 < ball.pos[0] < WIN_X and -30 < ball.pos[1] < WIN_Y):
                    fly.remove(ball)
                    break
                ball.shooter_move()
                ball.draw(window)
                ball.rect = ball.ball_image.get_rect()

        draw_shooter(map, window, front, back)

        pygame.display.update()


def choose_map():
    global screen
    for i in range(3, 0, -1):
        window.blit(load("choose maps/" + str(i) + ".png"), (0, 0))
    pygame.display.update()
    if pygame.mouse.get_pressed()[0]:
        screen = 2


def blackout():
    global screen
    window.fill((0, 0, 0))
    pygame.display.update()
    wait(1000)
    screen = 3


if __name__ == "__main__":
    screen = 1
    map = 0
    level = 0
    while True:
        clock.tick(60)
        if screen == 1:
            choose_map()
        if screen == 2:
            blackout()
        if screen == 3:
            game(map, level)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

