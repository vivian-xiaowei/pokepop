import sys
import pygame
from pygame import *
from spiral import *

pygame.init()
clock = time.Clock()

# setting up window size
WIN_X = int(1000)

# how tall the screen is going to be
WIN_Y = int(750)

# set the screen
window = pygame.display.set_mode((WIN_X, WIN_Y))


def main():
    x_s, y_s = spiral()

    while True:  # main game loop
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        window.fill((255, 255, 255))

        draw_spiral(x_s, y_s)

        follow_lines()

        pygame.display.update()


if __name__ == "__main__":
    main()
