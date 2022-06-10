from pygame.image import load
from lines import *
from shooter import *
from balls import *


def find_length(ball_list, count, push):
    start, end = count, count
    while start > 0 and ball_list[start].type == ball_list[start - 1].type:
        start -= 1
    while end < len(ball_list) - 2 and ball_list[end].type == ball_list[end + 1].type:
        end += 1
    if end <= len(ball_list) - 2 and ball_list[end + 1].type == ball_list[count].type and end + 2 == len(ball_list):
        end += 2
    if count == len(ball_list) - 1 and ball_list[count].type == push:
        end += 1
    return start, end


def game(map, level):
    ball_list = generate_ball(level, map) # randomly generate a list of balls
    front = pokeballs(pick_ball(), -30, -30, 0, 0, 0)
    back = pokeballs(pick_ball(), -30, -30, 0, 0, 0)
    shooter_pos = [[500, 450], [500, 640], [320, 460]]
    fly = []
    ingame = True

    while ingame:
        push = -1
        clock.tick(60)
        start, end = 0, 0
        # the bottom background
        window.blit(load("backgrounds/" + str(map) + "a.png"), (0, 0))
        # move the balls along the path, detect collision
        for count in range(len(ball_list)):
            ball = ball_list[count]
            ball.rect.topleft = ball.pos
            # balls off the path at the start
            if ball.pos[0] < 100 and ball.pos[1] <= 200:
                ball.shooter_move(True)
                ball.rotate = ball_list[0].rotate
            else:
                balls_exist.add(ball.type)
                for fly_count in range(len(fly)):
                    flying = fly[fly_count]
                    if dist(ball.pos, flying.pos) <= 30:
                        print(count, len(ball_list))
                        push = ball_list[len(ball_list) - 1].type
                        for i in range(len(ball_list)-1, count, -1):
                            ball_list[i].type = ball_list[i-1].type
                        ball_list[count].type = flying.type
                        fly.remove(flying)

                        start, end = find_length(ball_list, count, push)
                        print("starting", start)
                        print("ending  ", end)
                        print(len(ball_list))
                        break
                if ball.move2:
                    if map == 0:
                        ingame = map1(ball)
                    elif map == 1:
                        ingame = map2(ball)
                    else:
                        ingame = map3(ball)
                    ball.shooter_move(True)
                elif count + 1 == len(ball_list) or (ball_list[count + 1].move2 and dist(ball_list[count + 1].pos, ball.pos) <= 30):# abs(ball_list[count + 1].pos[0] - ball.pos[0]) <= 30 or abs(ball_list[count + 1].pos[1] - ball.pos[1]) <= 30):
                    for i in range(0, count + 1):
                        ball_list[i].move2 = True
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
            new_ball.road_h, new_ball.road_v = last.road_h, last.road_v
            new_ball.speed = abs(new_ball.x_move) + abs(new_ball.y_move)
            new_ball.move = last.move2
            ball_list.append(new_ball)

        if end - start + 1 >= 3:
            deleted = ball_list[start].type
            balls_exist.remove(ball_list[start].type)
            if end != len(ball_list) - 1:
                for i in range(0, start):
                    ball_list[i].move2 = False
            for i in range(start, end + 1):
                ball_list.remove(ball_list[start])
            if front.type == deleted:
                front.type = pick_ball(front.type)
            if back.type == deleted:
                back.type = pick_ball(back.type)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system
            if event.type == pygame.MOUSEBUTTONUP:
                run, rise = (front.pos[0] + 14 - shooter_pos[map][0], front.pos[1] + 15 - shooter_pos[map][1])
                diff = sqrt(pow(run, 2) + pow(rise, 2))
                fly.append(front)
                if map == 0:
                    fly[len(fly) - 1].x_move = run / diff * 20
                    fly[len(fly) - 1].y_move = rise / diff * 20
                elif map == 1:
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
        draw_shooter(map, window, front, back, shooter_pos[map])

        pygame.display.update()
