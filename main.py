import pygame.display
from pygame.time import wait

import gameplay
from gameplay import *
from setup import *
import sys


def try_exit(event):
    if event.type == pygame.QUIT:  # if you quit pygame
        pygame.quit()  # quit pygame
        sys.exit()  # exit the system


def choose_map():
    global map
    clock.tick(60)
    pygame.draw.polygon(window, red, [(0, 0), (500, 0), (498, 351), (0, 695), (0, 0)])
    pygame.draw.polygon(window, blue, [(500, 0), (1000, 0), (1000, 690), (498, 351), (500, 0)])
    pygame.draw.polygon(window, black, [(498, 351), (0, 695), (0, 750), (1000, 750), (1000, 690), (498, 351)])
    for event in pygame.event.get():
        try_exit(event)
        mouse = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if colourCollision(red, mouse):
                map = 0
            if colourCollision(blue, mouse):
                map = 1
            if colourCollision(black, mouse):
                map = 2
            wait(500)
            choose_level()

    for i in range(3, 0, -1):
        window.blit(load("choose maps/" + str(i) + ".png"), (0, 0))
    pygame.display.update()


def colourCollision(colour, mouse):
    if window.get_at(mouse) == colour:
        return True
    return False


def choose_level():
    global level
    level = -1
    animation = animations[map]
    width, height = animation[0].get_width(), animation[0].get_height()
    count = 0
    coordinates = [(250, 200), (WIN_X / 2, 200), (750, 200), (250, 400), (WIN_X / 2, 400), (750, 400)]
    indexes = [0, 0, 0, 0, 0, 0]
    offset = [(-10, -25), (-15, -40), (0, -30)]
    buttons = []
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            try_exit(event)
        window.fill((255, 255, 255))
        count += len(animation) / 50
        if int(count) > len(animation) - 1:
            count = 0
        for i in range(0, 6):
            pos = (coordinates[i][0] - width/2, coordinates[i][1] - height/2)
            buttons.append(window.blit(animation[indexes[i]], pos))

        for i in range(0, 6):
            if buttons[i].collidepoint(pygame.mouse.get_pos()):
                indexes[i] = int(count)
                if mouse.get_pressed()[0]:
                    level = i + 1
                    for i in range(0, 6):
                        window.blit(numbers[i],
                                    (coordinates[i][0] + offset[map][0], coordinates[i][1] + offset[map][1]))

                    blackout()
            else:
                indexes[level] = 0
        for i in range(0, 6):
            window.blit(numbers[i], (coordinates[i][0] + offset[map][0], coordinates[i][1] + offset[map][1]))
        pygame.display.update()


def blackout():  # transition between choose map and game
    fill = pygame.Surface((WIN_X, WIN_Y))
    fill.fill((0, 0, 0))
    speed = 0.1
    alpha = 20
    for i in range(0, 100):
        fill.set_alpha(alpha)
        alpha -= speed
        window.blit(fill, (0, 0))
        pygame.display.update()
    game(map, level)


def aftergame():
    wait(1000)
    choose_map()


def starting():
    window.blit(load("start.png"), (0, 0))
    pygame.display.update()
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                start = False
            try_exit(event)
    start = True
    startingImage = load("start.png")
    scaled = transform.scale(startingImage, (int(1000 * 1.1), int(750 * 1.1)))
    window.blit(startingImage, (0, 0))
    while start:
        clock.tick(60)
        for event in pygame.event.get():
            try_exit(event)
            pos = pygame.mouse.get_pos()
            if not colourCollision(black, pos):
                window.blit(scaled, (1000 - int(1000 * 1.2) + 160, 750 - int(750 * 1.2) + 120))
                if pygame.mouse.get_pressed()[0]:
                    wait(100)
                    start = False
            else:
                window.blit(startingImage, (0, 0))
            pygame.display.update()
    choose_map()


if __name__ == "__main__":
    map, level = 0, 0
    starting()
    while True:
        choose_map()
