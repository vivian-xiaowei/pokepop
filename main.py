import pygame.display
from pygame.time import wait
from gameplay import *


def choose_map():
    global map
    map1 = pygame.draw.polygon(window, (0, 0, 0), [(0, 0), (500, 0), (498, 351), (0, 695), (0, 0)], 1)
    map2 = pygame.draw.polygon(window, (0, 0, 0), [(500, 0), (1000, 0), (1000, 690), (498, 351), (500, 0)], 1)
    map3 = pygame.draw.polygon(window, (0, 0, 0),
                               [(498, 351), (0, 695), (0, 750), (1000, 750), (1000, 690), (498, 351)], 1)
    for i in range(3, 0, -1):
        window.blit(load("choose maps/" + str(i) + ".png"), (0, 0))

    pygame.display.update()

    mouse=pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if(map1.collidepoint(mouse)):
            map=0
        if(map2.collidepoint(mouse)):
            map=1
        if(map3.collidepoint(mouse)):
            map=2
        blackout()
        game(map, level)
        freeze()


def blackout():  # transition between choose map and game
    window.fill((0, 0, 0))
    pygame.display.update()
    wait(1000)


def freeze():
    wait(3000)


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
