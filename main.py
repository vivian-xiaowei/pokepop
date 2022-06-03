import pygame.display
from pygame.image import load
from pygame.time import wait

from lines import *
from shooter import *


def game(map, level):
    global screen
    # randomly generate a list of balls
    ball_list = generate_ball(level)
    # randomly generate the two balls on the shooter and make sure the ball exist in the main list
    front = pokeballs(pick_ball(), 0, 0, 0, 0, 0)
    back = pokeballs(pick_ball(), 0, 0, 0, 0, 0)
    fly = []

    while True:
        push = -1
        clock.tick(60)

        # the bottom background
        window.blit(load("backgrounds/" + str(map) + "a.png"), (0, 0))
        # move the balls in the list base on the collision with lines
        for count in range(len(ball_list)):
            ball = ball_list[count]
            print(ball.pos)
            ball.rect.center = ball.pos
            # balls off the path at the start
            if ball.pos[0] < 100 and ball.pos[1] <= 100:
                ball.move(0, ball.x_move)
            else:
                balls_exist.add(ball.type)
                for fly_count in range(len(fly)):
                    flying = fly[fly_count]
                    # d = cos(flying.angle * 180 / pi + pi/2) * 15
                    # print(flying.angle * pi / 180 + pi/2, d)
                    # distance = dist((ball.pos[0] + 15, ball.pos[1] + 15), (flying.pos[0] + 15 - d, flying.pos[1] + 15 - d))
                    # pygame.draw.circle(window, (0, 0, 0), (ball.pos[0] + 15, ball.pos[1] + 15), 5)
                    # pygame.draw.circle(window, (0, 0, 0), (flying.pos[0] + 15 - d, flying.pos[1] + 15 - d), 5)
                    distance = dist(ball.pos, flying.pos)
                    if distance <= 30:
                        for i in range(len(ball_list)-1, count, -1):
                            ball_list[i].type = ball_list[i-1].type
                        ball_list[count].type = flying.type
                        push = ball_list[len(ball_list) - 1].type
                        fly.remove(flying)
                        break
                if map == 0:
                    map1(ball)
                elif map == 1:
                    map2(ball)
                else:
                    map3(ball)
                ball.draw(window)
        window.blit(load("backgrounds/" + str(map) + "b.png"), (0, 0))

        if push > -1:
            last = ball_list[len(ball_list)-1]
            x, y = last.pos
            if y == 100 or y == 592:
                x -= 30
            elif y == 292:
                x += 30
            else:
                y -= 30
            new_ball = pokeballs(push, x, y, last.rotate, last.x_move, last.y_move)
            new_ball.road_h = last.road_h
            new_ball.road_v = last.road_v
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
    window.blit(load("3.png"), (0, 0))
    window.blit(load("2.png"), (0, 0))
    window.blit(load("1.png"), (0, 0))
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

