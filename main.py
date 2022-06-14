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

    pos = pygame.mouse.get_pos()
    print(pygame.mouse.get_pressed())
    if pygame.mouse.get_pressed()[0]:
        if map1.collidepoint(pos):
            map = 0
        if map2.collidepoint(pos):
            map = 1
        if map3.collidepoint(pos):
            map = 2
        print()
        print()
        wait(500)
        choose_level()
        blackout()
        game(map, level)
        freeze()


def choose_level():
    global level
    count = 0.99
    while True:
        if pygame.mouse.get_pressed()[0] and count != 0.99:
            break
        window.fill((255, 255, 255))
        clock.tick(60)
        window.blit(transform.scale(load("cube"+str(round(count))+".png"), (100, 103)), (0, 0))
        count += 0.1
        if round(count) > 8:
            count = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()
                sys.exit()
        pygame.display.update()


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
