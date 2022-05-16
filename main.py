import sys
import pygame
from pygame import *
from spiral import *

pygame.init()

# setting up window size
WIN_X = int(1000)

# how tall the screen is going to be
WIN_Y = int(750)

# set the screen
WIN = pygame.display.set_mode((WIN_X, WIN_Y))


def main():

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        WIN.fill((255, 255, 255))

        x_s, y_s = spiral()
        draw_spiral(x_s, y_s)

        follow_lines(horizRoad, xmove, added, vertRoad)

        pygame.display.update()

    # does this work


if __name__ == "__main__":
    main()
