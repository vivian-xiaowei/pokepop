import pygame.display
from pygame.time import wait
from gameplay import *
from setup import *
import sys


def choose_map():
    global map
    pygame.draw.polygon(window, red, [(0, 0), (500, 0), (498, 351), (0, 695), (0, 0)])
    pygame.draw.polygon(window, blue, [(500, 0), (1000, 0), (1000, 690), (498, 351), (500, 0)])
    pygame.draw.polygon(window, black, [(498, 351), (0, 695), (0, 750), (1000, 750), (1000, 690), (498, 351)])

    mouse = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if colourCollision(red, mouse):
            map = 0
        if colourCollision(blue, mouse):
            map = 1
        if colourCollision(black, mouse):
            map = 2
        wait(500)
        choose_level()
        blackout()
        game(map, 5)
        aftergame()

    for i in range(3, 0, -1):
        window.blit(load("choose maps/" + str(i) + ".png"), (0, 0))
    pygame.display.update()


def colourCollision(colour, mouse):
    if window.get_at(mouse) == colour:
        return True
    return False


def choose_level():
    global level
    animation = animations[map]
    count = 0
    transition = True
    while True:
        if pygame.mouse.get_pressed()[0] and not transition:
            break
        transition = False
        window.fill((255, 255, 255))
        clock.tick(60)
        count += len(animation)/60
        if int(count) > len(animation) - 1:
            count = 0
        window.blit(animation[int(count)], (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()
                sys.exit()
        pygame.display.update()


def blackout():  # transition between choose map and game
    window.fill((0, 0, 0))
    pygame.display.update()
    wait(1000)


def aftergame():
    wait(3000)


def starting():
    window.blit(load("start.png"), (0, 0))
    pygame.display.update()
    wait(5000)


if __name__ == "__main__":
    map = 0
    level = 5

    start = True
    while start:
        window.blit(load("start.png"), (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                start = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    while True:
        clock.tick(60)
        choose_map()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system
