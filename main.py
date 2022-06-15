import pygame.display
from pygame.time import wait
from gameplay import *


map1_animation = []
map2_animation = []
map3_animation = []

for i in range(1, 9):
    map3_animation.append(transform.scale(load("cube" + str(i) + ".png"), (100, 103)))
for i in range(1, 5):
    map1_animation.append(transform.scale(load("leaf" + str(i) + ".png"), (85, 100)))

animations = [map1_animation, map2_animation, map3_animation]


def choose_map():
    global map
    map1 = pygame.draw.polygon(window, (0, 0, 0), [(0, 0), (500, 0), (498, 351), (0, 695), (0, 0)], 1)
    map2 = pygame.draw.polygon(window, (0, 0, 0), [(500, 0), (1000, 0), (1000, 690), (498, 351), (500, 0)], 1)
    map3 = pygame.draw.polygon(window, (0, 0, 0),
                               [(498, 351), (0, 695), (0, 750), (1000, 750), (1000, 690), (498, 351)], 1)
    maps = [map1, map2, map3]
    for i in range(3, 0, -1):
        window.blit(load("choose maps/" + str(i) + ".png"), (0, 0))

    pygame.display.update()
    if map3.collidepoint(pygame.mouse.get_pos()):
        print(3)
    # if map2.collidepoint(pygame.mouse.get_pos()):
    #     print(2)
    # if map1.collidepoint(pygame.mouse.get_pos()):
    #     print(1)
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        for i in range(3):
            if maps[i].collidepoint(pos):
                map = i
                break
        wait(500)
        choose_level()
        blackout()
        game(map, level)
        freeze()


def choose_level():
    global level
    animation = animations[map]
    count = -1 * len(animation)/60
    while True:
        if pygame.mouse.get_pressed()[0] and count != -1 * len(animation)/60:
            break
        window.fill((255, 255, 255))
        clock.tick(60)
        count += len(animation)/60
        if int(count) == len(animation):
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
