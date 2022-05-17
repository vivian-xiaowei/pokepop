import pygame.sprite

from lines import *
from balls import *


def main():
    # spiral variable
    x_s, y_s = spiral()
    # straight line angle variable
    pos = 0
    # rolling_balls = pygame.sprite.Group()
    # first_ball = Ball(sprites[0][0])
    # rolling_balls.add([first_ball])

    while True:  # main game loop
        clock.tick(60)
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        follow_lines(0, int(pos))

        pos += 0.15
        if pos >= 8:
            pos = 0

        # rolling_balls.draw()

        # draw the spiral dots
        draw_spiral(x_s, y_s)

        pygame.display.update()


if __name__ == "__main__":
    main()
