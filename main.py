import pygame.display
from pygame.time import wait
from gameplay import *


def choose_map():
    for i in range(3, 0, -1):
        window.blit(load("choose maps/" + str(i) + ".png"), (0, 0))
    pygame.display.update()
    if pygame.mouse.get_pressed()[0]:
        blackout()


def blackout():  # transition between choose map and game
    window.fill((0, 0, 0))
    pygame.display.update()
    wait(1000)
    game(map, level)


if __name__ == "__main__":
    map = 0
    level = 0
    while True:
        clock.tick(60)
        choose_map()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system
