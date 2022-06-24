# https://stackoverflow.com/questions/70419688/find-size-of-rotated-rectangle-that-covers-orginal-rectangle

import pygame.draw
import balls
from main import try_exit
from main import aftergame
from main import choose_level
from main import choose_map
from lines import *
from shooter import *
from balls import *


def find_length(ball_list, count, push, toadd):
    start, end = count, count
    while start > 0 and ball_list[start].type == ball_list[start - 1].type and (ball_list[start].move ==
            ball_list[start - 1].move or dist(ball_list[start].pos, ball_list[start - 1].pos) <= 30):
        start -= 1
    while end < len(ball_list) - 2 and ball_list[end].type == ball_list[end + 1].type and (ball_list[end].move ==
            ball_list[end + 1].move or dist(ball_list[end].pos, ball_list[end + 1].pos) <= 30):
        end += 1
    if end == toadd - 1 and ball_list[toadd].type == ball_list[count].type:
        end += 1
    if end == toadd and push == ball_list[start].type:
        end += 1
    if end < len(ball_list) and not ball_list[end].move and ball_list[end + 1].move and dist(ball_list[end].pos, ball_list[end + 1].pos) <= 60:
        end += 1
    return start, end


def find_stopped(ball_list, start, back=True):
    if back:
        while start + 1 < len(ball_list) and not ball_list[start + 1].move and dist(ball_list[start].pos, ball_list[start + 1].pos) <= 30:
            start += 1
    else:
        while start - 1 >= 0 and dist(ball_list[start].pos, ball_list[start - 1].pos) <= 30:
            start -= 1
    return start


def add_correction(ball, last, rh, rv, xm, ym):
    x, y = ball.pos
    rect = pygame.Rect(x, y, 30, 30)
    ball.rect.topleft = ball.pos
    last.rect.topleft = last.pos
    if ball.road_h < len(rh) and ball.road_v < len(rv) and not rh[int(ball.road_h)].colliderect(rect) and not rv[int(ball.road_v)].colliderect(rect) \
            and not (ball.pos[0] < 100 and ball.pos[1] <= 200) and not (rh[ball.road_h - 1].colliderect(rect) or rv[ball.road_v - 1].colliderect(rect)):
        if rh[int(last.road_h)].colliderect(last.rect):
            x = abs(last.pos[0])
            y = last.pos[1] + 30
            ball.rect.topleft = [x, y]
            ball.road_v -= 1
            ball.x_move = 0
            ball.y_move = ball.speed * ym[ball.road_h + int(ball.road_v)]
            if not rv[int(ball.road_v)].colliderect(ball.rect):
                y = last.pos[1] - 30
        else:
            x = last.pos[0] - 30
            y = abs(last.pos[1])
            ball.rect.topleft = [x, y]
            ball.road_h -= 1
            ball.y_move = 0
            ball.x_move = ball.speed * xm[ball.road_h + int(ball.road_v)]
            if not rh[int(ball.road_h)].colliderect(ball.rect):
                x = last.pos[0] + 30
    return [x, y]


def map2_correction(ball_list, count):
    diff = 88 - ball_list[count].pos[0]
    for i in range(find_stopped(ball_list, count, False), count + 1):
        ball = ball_list[i]
        ball.pos[0] += diff
        print(ball.pos)


def pause():
    window.blit(load("backgrounds/" + str(map) + "c.png"), (0, 0))
    grey = pygame.Surface((WIN_X, WIN_Y))
    grey.set_alpha(100)
    grey.fill((0, 0, 0))
    window.blit(grey, (0, 0))
    # window.fill(())
    pygame.mixer.music.load("music/Map" + str(map + 1) + " Level Select Music.mp3")
    mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)
    draw.rect(window, (97, 56, 29), (250, 170, 500, 400), 0, 15, 15, 15, 15)
    draw.rect(window, (207, 159, 111), (270, 190, 460, 360), 0, 15, 15, 15, 15)
    window.blit(load("pause/Level.png"), (400, 240))
    window.blit(load("pause/" + str(level + 1) + ".png"), (550, 240))
    button_number = [0, 1, 4]
    buttons = []
    for i in range(3):
        buttons.append(window.blit(load_button[button_number[i]], (460 + (len(buttons) - 1) * 130, 380)))
    pygame.display.update()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            try_exit(event)
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(mouse):
                    return False, "map"
                elif buttons[1].collidepoint(mouse):
                    return False, "level"
                elif buttons[2].collidepoint(mouse):
                    pygame.mixer.music.load("music/Map" + str(map + 1) + " Level " + str(level + 1) + " Music.mp3")
                    mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    return True, None


def game(map, level):
    ball_list = generate_ball(level, map)  # randomly generate a list of balls
    front = pokeballs(pick_ball(), -30, -30, 0, 0, 0)  # front ball on shooter
    back = pokeballs(pick_ball(), -30, -30, 0, 0, 0)  # second shooter ball
    shooter_pos = [[500, 450], [500, 640], [280, 460]]  # the center for shooters on different maps
    fly = []  # to store balls shot out
    speedup = False  # if the ball touches the end and speed up to leave
    speed = 6  # the number of times moving the ball at the start
    add_index = 0   # the position to add the ball
    ingame = True  # quit the loop if the game is finish
    win = False
    next = None
    # refer to the moving function for the map
    if map == 0:
        change_move = map1
    elif map == 1:
        change_move = map2
    else:
        change_move = map3
    pygame.mixer.music.load("music/Map" + str(map + 1) + " Level " + str(level + 1) + " Music.mp3")
    mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)
    print(level)
    # while the game is not over or there are ball flying, blit game screen
    while ingame or len(fly) != 0:
        clock.tick(30)
        if len(ball_list) == 0:  # player wins
            ingame = False
            win = True
        elif ball_list[len(ball_list) - 1].x_move + ball_list[len(ball_list) - 1].y_move == 0:  # player loses
            ingame = False

        push = -1  # the ball type to add at the end of the list
        start, end = 0, 0  # to store starting and ending positions of the same colour
        window.blit(load("backgrounds/" + str(map) + "a.png"), (0, 0))  # the bottom background
        # shift balls to show up faster on screen if there is no more balls
        if len(ball_list) != 0 and ball_list[0].pos[0] < 90 and ball_list[0].pos[1] <= 200:
            diff = 90 - ball_list[0].pos[0]
            for ball in ball_list:
                ball.pos[0] += diff
        # move the balls along the path, detect collision with flying balls
        for count in range(len(ball_list)):
            ball = ball_list[count]
            length = len(ball_list)
            ball.rect.topleft = ball.pos
            if ball.pos[0] < 100 and ball.pos[1] <= 200:  # balls off the path at the start
                for _ in range(int(speed)):
                    ball.shooter_move(True)
                ball.rotate = ball_list[count - 1].rotate
            else:                                         # the balls showing on the screen
                balls.balls_exist.add(ball.type)
                center = ball.pos[0] + 15, ball.pos[1] + 15  # center of the ball
                for flying in fly:
                    angle = flying.angle
                    half = 15 * (abs(cos(angle)) + abs(sin(angle)))
                    center_f = (flying.pos[0] + half, flying.pos[1] + half)  # center of the angled ball (reference)
                    if dist(center, center_f) <= 30:  # distance less than the ball diameter
                        pop = pygame.mixer.Sound("music/pop.mp3")
                        pop.play()
                        notmove = find_stopped(ball_list, count)
                        if ball.move or dist(ball_list[notmove].pos, ball_list[notmove + 1].pos) <= 60:
                            add_index = length - 1
                        else:
                            add_index = notmove
                        push = ball_list[add_index].type
                        for i in range(add_index, count, -1):
                            ball_list[i].type = ball_list[i - 1].type
                        ball_list[count].type = flying.type
                        fly.remove(flying)
                        start, end = find_length(ball_list, count, push, add_index)
                        break
                if ball.move:
                    for _ in range(int(speed)):
                        speedup = change_move(ball, speedup)
                        ball.shooter_move(True)
                elif count + 1 == length or (
                        ball_list[count + 1].move and dist(ball_list[count + 1].pos, ball.pos) <= 30):
                    for j in range(count, -1, -1):
                        if j + 1 == length or dist(ball_list[j].pos, ball_list[j + 1].pos) <= 30:
                            ball_list[j].move = True
                        else:
                            break
                if map == 1 and not ball.move and ball.pos[0] < 85:
                    map2_correction(ball_list, count)
                ball.draw(window)

        if speedup:
            speed += 0.2
        elif int(speed) > 1 and not speedup:
            speed -= 0.1

        if push > -1:
            last = ball_list[add_index]
            x, y = last.pos
            x -= 30 * last.x_move / last.speed
            y -= 30 * last.y_move / last.speed
            new_ball = pokeballs(push, x, y, last.rotate, last.x_move, last.y_move)
            new_ball.road_h, new_ball.road_v = last.road_h, last.road_v
            new_ball.speed, new_ball.move, new_ball.angle = last.speed, last.move, last.angle
            ball_list.insert(add_index + 1, new_ball)
            ball = ball_list[add_index + 1]
            last = ball_list[add_index]
            if map == 0:
                ball.pos = add_correction(ball, last, horizRoads1, vertRoads1, hmove, vmove)
            elif map == 2:
                ball.pos = add_correction(ball, last, horizRoads3, vertRoads3, horizRoadsMove, vertRoadsMove)
            if not (ball.pos[0] < 100 and ball.pos[1] <= 200):
                ball.draw(window)
        window.blit(load("backgrounds/" + str(map) + "b.png"), (0, 0))
        if end - start + 1 >= 3:
            if end != len(ball_list) - 1:
                for i in range(0, start):
                    ball_list[i].move = False
            for i in range(start, end + 1):
                ball_list.remove(ball_list[start])

        pause_button = window.blit(load_button[5], (900, 20))
        for event in pygame.event.get():
            try_exit(event)
            if event.type == pygame.MOUSEBUTTONUP and pause_button.collidepoint(mouse.get_pos()):
                ingame, next = pause()
            elif event.type == pygame.MOUSEBUTTONUP and int(speed) == 1:
                run, rise = (front.pos[0] + 14 - shooter_pos[map][0], front.pos[1] + 15 - shooter_pos[map][1])
                diff = sqrt(pow(run, 2) + pow(rise, 2))
                fly.append(front)
                fly[len(fly) - 1].x_move = run / diff * 20
                fly[len(fly) - 1].y_move = rise / diff * 20
                front = back
                back = pokeballs(pick_ball(-1), 0, 0, 0, 0, 0)

        if not fly == []:
            out = 0
            for ball in fly:
                if not (0 - 30 < ball.pos[0] < WIN_X and -30 < ball.pos[1] < WIN_Y):
                    out = ball
                ball.shooter_move()
                ball.draw(window)
            if out != 0:
                fly.remove(out)
        window.blit(load("backgrounds/" + str(map) + "c.png"), (0, 0))
        front.type = pick_ball(front.type)
        back.type = pick_ball(back.type)
        draw_shooter(map, window, front, back, shooter_pos[map], speed)
        balls.balls_exist.clear()
        pygame.display.update()
    pygame.mixer.music.stop()
    if next == "map":
        choose_map()
    elif next == "level":
        choose_level()
    else:
        aftergame(win, level)
