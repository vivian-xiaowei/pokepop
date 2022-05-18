import pygame.sprite

from lines import *
from balls import *


def main():
    # spiral variable
    x_s, y_s = spiral()
    # straight line angle variable
    ball_list = []
    for i in range(5):
        ball_list.append(pokeballs(ball_images[0][0], 600 + i * 22, 100))
    # ball = pokeballs(ball_images[0][0], 100, 100)

    while True:  # main game loop
        clock.tick(60)
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        # change the ball position base on the collision with lines
        for ball in ball_list:
            ball.rect.center = ball.pos
            print(ball.rect.center)
            ball.pos, ball.road_h, ball.road_v = follow_lines(ball.pos, ball.rect, ball.road_h, ball.road_v)

            ball.roll(0.1)
            ball.draw(window)

        # draw the spiral dots
        draw_spiral(x_s, y_s)

        pygame.display.update()


if __name__ == "__main__":
    main()
