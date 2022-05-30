import pygame
from pygame.image import load

from lines import *
from shooter import *


def ingame(map, level):
    # randomly generate a list of balls
    ball_list = generate_ball(level)
    # randomly generate the two balls on the shooter and make sure the ball exist in the main list
    front = pokeballs(pick_ball(), 0, 0, 0, 0, 0)
    back = pokeballs(pick_ball(), 0, 0, 0, 0, 0)
    fly = pokeballs(0, -100, -100, 0, 0, 0)

    while True:  # main game loop
        clock.tick(60)

        back.shooter_move()
        # the bottom background
        window.blit(load("backgrounds/" + str(map) + "a.png"), (0, 0))

        # move the balls in the list base on the collision with lines
        for count in range(len(ball_list)):
            ball = ball_list[count]
            ball.rect.center = ball.pos
            # balls off the path at the start
            if ball.pos[0] < 100 and ball.pos[1] <= 100:
                ball.move(0, ball.x_move)
            # for the balls to follow map
            else:
                balls_exist.add(ball.type)
                if map == 0:
                    map1(ball)
                elif map == 1:
                    map2(ball)
                else:
                    map3(ball)
                ball.draw(window)
        window.blit(load("backgrounds/" + str(map) + "b.png"), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system
            if event.type == pygame.MOUSEBUTTONUP:
                run, rise = (front.pos[0] + 14 - 500, front.pos[1] + 15 - 450)
                diff = sqrt(pow(run, 2) + pow(rise, 2))
                front.x_move = run / diff * 20
                front.y_move = rise / diff * 20
                fly = front
                front = back
                back = pokeballs(pick_ball(), 0, 0, 0, 0, 0)

        fly.shooter_move()
        fly.draw(window)

        draw_shooter(map, window, front, back)

        pygame.display.update()


if __name__ == "__main__":
    ingame(0, 0)
