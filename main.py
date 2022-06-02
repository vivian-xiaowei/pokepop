from pygame.image import load

from lines import *
from shooter import *


def game(map, level):
    # randomly generate a list of balls
    ball_list = generate_ball(level)
    # randomly generate the two balls on the shooter and make sure the ball exist in the main list
    front = pokeballs(pick_ball(), 0, 0, 0, 0, 0)
    back = pokeballs(pick_ball(), 0, 0, 0, 0, 0)
    fly = []

    while True:
        push = -1
        clock.tick(30)

        # the bottom background
        window.blit(load("backgrounds/" + str(map) + "a.png"), (0, 0))
        # move the balls in the list base on the collision with lines
        for count in range(len(ball_list)):
            ball = ball_list[count]
            ball.rect.center = ball.pos
            # balls off the path at the start
            if ball.pos[0] < 100 and ball.pos[1] <= 100:
                ball.move(0, ball.x_move)
            else:
                balls_exist.add(ball.type)
                for fly_count in range(len(fly)):
                    flying = fly[fly_count]
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
                print(count, ball.pos)
        # window.blit(load("backgrounds/" + str(map) + "b.png"), (0, 0))

        if push > -1:
            x, y = ball_list[len(ball_list)-1].pos
            x -= 30
            new_ball = pokeballs(push, x, y)
            new_ball.rotate = ball_list[0].rotate
            ball_list.append(new_ball)
            if x > 100:
                ball_list[len(ball_list)-1].draw(window)

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


if __name__ == "__main__":
    game(0, 0)
