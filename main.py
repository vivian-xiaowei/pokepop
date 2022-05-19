import pygame.sprite

from lines import *
from balls import *


def main():
    # spiral variable
    x_s, y_s = spiral()
    # straight line angle variable
    ball_list = []
    for i in range(5):
        ball_list.append(pokeballs(0, 600 + i * 22, 100))

    while True:  # main game loop
        clock.tick(60)
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        # change the ball position base on the collision with straight lines
        for ball in ball_list:
            ball.rect.center = ball.pos
            ball.pos, ball.road_h, ball.road_v, ball.x_move = follow_lines(ball.pos, ball.rect, ball.road_h, ball.road_v, ball.x_move)

            ball.roll(0.1)
            ball.draw(window)

        # draw the spiral dots
        draw_spiral(x_s, y_s)

        pygame.display.update()


if __name__ == "__main__":
    main()
