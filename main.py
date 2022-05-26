import pygame.sprite

from lines import *
from balls import *


def main():
    # spiral variable
    x_s, y_s, a = spiral()
    ball_list = []
    map = 0
    for i in range(10):
        ball_list.append(pokeballs(1, 550 - i * 22, 100))
    for i in range(5):
        ball_list.append(pokeballs(4, 550 - 220 - i * 22, 100))

    while True:  # main game loop
        clock.tick(300)
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        # change the ball position base on the collision with straight lines
        for count in range(len(ball_list)):
            ball = ball_list[count]
            ball.rect.center = ball.pos
            if map == 0:
                map1(ball)
            elif map == 1:
                follow_spiral(ball, a, x_s, y_s)
            elif map == 2:
                map2(ball)
            ball.draw(window)

        pygame.display.update()


if __name__ == "__main__":
    main()
