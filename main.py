import pygame.sprite

from lines import *
from shooter import *


def main():
    map = 0
    ball_list = generate_ball(0)
    front = pokeballs(randint(0, 6), 0, 0)
    back = pokeballs(randint(0, 6), 0, 0)

    while True:  # main game loop
        clock.tick(60)
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        # change the ball position base on the collision with straight lines
        for count in range(len(ball_list)):
            ball = ball_list[count]
            ball.rect.center = ball.pos
            if ball.pos[0] < 100:
                ball.move(0, ball.x_move)
            else:
                if map == 0:
                    map1(ball)
                elif map == 1:
                    map2(ball)
                elif map == 2:
                    map3(ball)
            ball.draw(window)
        draw_shooter(map, window, front, back)

        pygame.display.update()


if __name__ == "__main__":
    main()
