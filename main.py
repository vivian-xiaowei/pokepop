import pygame.display
from pygame.time import wait
from gameplay import *
from setup import *
import sys


def try_exit(event):
    if event.type == pygame.QUIT:  # if you quit pygame
        pygame.quit()  # quit pygame
        sys.exit()  # exit the system


def choose_map():
    global map, level
    clock.tick(60)
    pygame.draw.polygon(window, red, [(0, 0), (500, 0), (500, 353), (0, 693), (0, 0)])
    pygame.draw.polygon(window, blue, [(500, 0), (1000, 0), (1000, 695), (500, 353), (500, 0)])
    pygame.draw.polygon(window, black, [(500, 353), (0, 693), (0, 750), (1000, 750), (1000, 695), (500, 353)])
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        try_exit(event)
        for i in range(3):
            if colourCollision(colours[i], mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    map = i
                    wait(500)
                    level = -1
                    choose_level()
                local_sign[i] = transform.scale(signs[i], (sign_size[i][0] * 1.2, sign_size[i][1] * 1.2))
            else:
                local_sign[i] = signs[i]
    window.blit(load("choose maps/maps.png"), (0, 0))
    for i in range(3):
        sign = local_sign[i]
        window.blit(sign, (sign_pos[i][0] - sign.get_width() / 2, sign_pos[i][1] - sign.get_height() / 2))
    pygame.display.update()


def colourCollision(colour, mouse):
    if window.get_at(mouse) == colour:
        return True
    return False


def choose_level():
    global level
    animation = animations[map]
    width, height = animation[0].get_width(), animation[0].get_height()
    count = 0
    coordinates = [(250, 200), (WIN_X / 2, 200), (750, 200), (250, 350), (WIN_X / 2, 350), (750, 350)]
    indexes = []
    for i in range(6):
        indexes.append(int(level_lock[map][i]) - 1)
    offset = [(-10, -25), (-15, -40), (-5, -30)]
    buttons = []
    loop = True
    transition = 10
    while loop:
        clock.tick(60)
        if transition > 0:
            transition -= 1
        window.blit(load("level/" + str(map) + ".png"), (0, 0))
        back = window.blit(back_button, (50, 30))
        for event in pygame.event.get():
            try_exit(event)
            if event.type == pygame.MOUSEBUTTONDOWN and back.collidepoint(mouse.get_pos()):
                loop = False
        count += len(animation) / 30
        if int(count) > len(animation) - 1:
            count = 0
        for i in range(6):
            pos = (coordinates[i][0] - width / 2, coordinates[i][1] - height / 2)
            if indexes[i] >= 0:
                buttons.append(window.blit(animation[indexes[i]], pos))
            else:
                buttons.append(window.blit(grey[map], pos))
            window.blit(numbers[i], (coordinates[i][0] + offset[map][0], coordinates[i][1] + offset[map][1]))

        for i in range(6):
            if buttons[i].collidepoint(pygame.mouse.get_pos()) and indexes[i] >= 0:
                indexes[i] = int(count)
                if pygame.mouse.get_pressed()[0] and transition == 0:
                    level = i
                    loop = False
            elif indexes[i] >= 0:
                indexes[i] = 0
        pygame.display.update()
    if level != -1:
        blackout()


def blackout():  # transition between choose map and game
    fill = pygame.Surface((WIN_X, WIN_Y))
    fill.fill((0, 0, 0))
    speed = 0.1
    alpha = 20
    for i in range(100):
        fill.set_alpha(alpha)
        alpha -= speed
        window.blit(fill, (0, 0))
        pygame.display.update()
    import gameplay
    print(level)
    gameplay.game(map, level)


def aftergame(win, mapC, levelC):
    global level, map, level_lock
    map = mapC
    level = levelC
    if level != 5 and level_lock[map][level + 1] == False and win:
        level_lock[map][level + 1] = True
    over = True
    buttons = []
    draw.rect(window, (97, 56, 29), (250, 170, 500, 400), 0, 15, 15, 15, 15)
    draw.rect(window, (207, 159, 111), (270, 190, 460, 360), 0, 15, 15, 15, 15)
    if win and level != 6:
        text = load("aftergame/Level_Completed.png")
    elif win and level == 6:
        text = load("aftergame/Map_Cleared.png")
    else:
        text = load("aftergame/Game_Over.png")
    window.blit(text, (500 - text.get_width() / 2, 230))
    if win and level != 6:
        for i in range(4):
            buttons.append(window.blit(load_button[i], (460 + (len(buttons) - 1.5) * 100, 400)))
    else:
        for i in range(3):
            buttons.append(window.blit(load_button[i], (460 + (len(buttons) - 1) * 130, 400)))
    pygame.display.update()
    while over:
        clock.tick(60)
        for event in pygame.event.get():
            try_exit(event)
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(mouse):
                    level = -1
                    over = False
                    choose_map()
                elif buttons[1].collidepoint(mouse):
                    level = -1
                    over = False
                    choose_level()
                elif buttons[2].collidepoint(mouse):
                    blackout()
                    over = False
                elif len(buttons) == 4 and buttons[3].collidepoint(mouse):
                    level += 1
                    blackout()
                    over = False


def starting():
    start = True
    startingImage = load("start/start.png")
    mouse = [transform.scale(load("start/blank.png"), (50, 72)), transform.scale(load("start/left.png"), (50, 72))]
    scaled = transform.scale(startingImage, (int(1000 * 1.1), int(750 * 1.1)))
    count = 1
    while start:
        clock.tick(30)
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
        window.blit(mouse[round(count)], (900, 40))
        count += 0.03
        if count > 1:
            count = 0
        pygame.display.update()


if __name__ == "__main__":
    starting()
    while True:
        choose_map()
