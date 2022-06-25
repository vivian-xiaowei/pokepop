import pygame.display
from pygame.time import wait
from gameplay import *
from setup import *
import sys


def try_exit(event):  # create a function for quitting the pygame (going to be recalled many different times)
    if event.type == pygame.QUIT:  # if you quit pygame
        pygame.quit()  # quit pygame
        sys.exit()  # exit the system


def choose_map():  # choose map screen
    global map, level  # globalize variables map and level which stores which map and level the player is using
    clock.tick(60)  # set the framerate to 60fps

    # draw differently coloured polygons for colour collisions for map select
    pygame.draw.polygon(window, red, [(0, 0), (500, 0), (500, 353), (0, 693), (0, 0)])
    pygame.draw.polygon(window, blue, [(500, 0), (1000, 0), (1000, 695), (500, 353), (500, 0)])
    pygame.draw.polygon(window, black, [(500, 353), (0, 693), (0, 750), (1000, 750), (1000, 695), (500, 353)])
    mouse = pygame.mouse.get_pos()  # get the mouse's position

    for event in pygame.event.get():
        try_exit(event)
        for i in range(3):  # loop through the polygon colours for colour collision
            if colourCollision(colours[i], mouse):  # if the mouse is colliding with the given colour
                if event.type == pygame.MOUSEBUTTONDOWN:  # if the user is also clicking their mouse
                    map = i  # map is equal to i (if the user clicks with colour 0 it goes to map 0)
                    wait(500)  # wait half a second
                    choose_level()  # call the choose level screen
                # when the user's mouse hovers over the map select "button", increase the size of the sign which shows
                # which map the user is selecting
                local_sign[i] = transform.scale(signs[i], (int(sign_size[i][0] * 1.2), int(sign_size[i][1] * 1.2)))
            else:  # if the user's mouse is not hovering over the map "button"
                local_sign[i] = signs[i]  # reset the sign size
    window.blit(load("choose maps/maps.png"), (0, 0))  # blit the map select screen button over the colour collision
    # detection
    for i in range(3):  # loop through the 3 map buttons
        sign = local_sign[i]  # update the sign size/image
        # blit the sign
        window.blit(sign, (sign_pos[i][0] - sign.get_width() / 2, sign_pos[i][1] - sign.get_height() / 2))
    pygame.display.update()  # update the screen


def colourCollision(colour, mouse):  # colour collision detection function
    if window.get_at(mouse) == colour:  # if the window colour at the mouse's coordinates is equal to the given colour
        return True  # return true
    return False  # if the window colour at the mouse's coordinate is not equal to the given colour, return false


def choose_level():  # choose level screen
    global level
    level = -1  # reset the level select
    animation = animations[map]  # choose the level button animations for the selected map
    width, height = animation[0].get_width(), animation[0].get_height()  # set the level button width and height
    count = 0  # set count to 0
    coordinates = [(250, 200), (WIN_X / 2, 200), (750, 200), (250, 350), (WIN_X / 2, 350), (750, 350)]  # input the
    # coordinates of the level buttons
    indexes = []  # initialize indexes array to store the index at which the animation is at
    for i in range(6):  # looping through the level buttons
        indexes.append(int(level_lock[map][i]) - 1)  # set locked to -1, unlocked levels to 0
    offset = [(-10, -25), (-15, -40), (-5, -30)]  # store the image offsets (found using trial and error)
    buttons = []  # initialize the button list
    loop = True  # initialize and set loop to true
    transition = 10  # initialize and set transition to 10

    pygame.mixer.music.load("music/Map" + str(map + 1) + " Level Select Music.mp3")  # load the music file
    mixer.music.set_volume(0.7)  # set the volume to 0.7
    pygame.mixer.music.play(-1)  # keep the music on loop unless otherwise mentioned

    while loop:  # while loop is true
        clock.tick(60)  # set fps to 60
        if transition > 0:  # if transition is over 0, decrease transition by 1
            transition -= 1
        window.blit(load("level/" + str(map) + ".png"), (0, 0))  # blit the level select screen background
        back = window.blit(back_button, (50, 30))  # blit and store the back button (x)
        for event in pygame.event.get():
            try_exit(event)
            if event.type == pygame.MOUSEBUTTONDOWN and back.collidepoint(
                    mouse.get_pos()):  # if the user clicks on back
                loop = False  # break out of the choose level screen loop
        count += len(animation) / 30  # count is increased by the length of the animation divided by 30
        if int(count) > len(animation) - 1:  # if count is now higher than the length of the animation minus 1
            count = 0  # reset the count
        for i in range(6):  # loop through the level buttons
            pos = (
            coordinates[i][0] - width / 2, coordinates[i][1] - height / 2)  # set and change the position according
            # to the size of the new image animation (to make it look like it's not moving around)
            if indexes[i] >= 0:  # if the index is more or equal to 0
                buttons.append(window.blit(animation[indexes[i]], pos))  # append the new image animation to buttons
            else:  # f the index is less than 0
                buttons.append(window.blit(grey[map], pos))  # append the greyed out version of the button (level is not
                # accessible)
            # blit the level number
            window.blit(numbers[i], (coordinates[i][0] + offset[map][0], coordinates[i][1] + offset[map][1]))

        for i in range(6):  # loop through the levels
            if buttons[i].collidepoint(pygame.mouse.get_pos()) and indexes[i] >= 0:  # if your mouse is colliding with the
                # button and the level is unlocked
                indexes[i] = int(count)  # the index is equal to count
                if pygame.mouse.get_pressed()[0] and transition == 0:  # if the button is pressed and transition is 0
                    level = i  # set the level
                    loop = False  # end the choose level loop
            elif indexes[i] >= 0:  # if the level is unlocked but the mouse isn't hovered over
                indexes[i] = 0  # set the button image to default
        pygame.display.update()  # update the screen
    # out of loop
    pygame.mixer.music.stop()  # end the level select music
    if level != -1:  # if the level isn't -1
        blackout()  # call blackout function
    else:  # if the level is unselected (-1)
        choose_map()  # go to the choose map screen


def blackout():  # transition between choose map and game
    fill = pygame.Surface((WIN_X, WIN_Y))
    fill.fill((0, 0, 0))  # fill the screen with black
    speed = 0.1  # set speed to 0.1
    alpha = 20  # set alpha (screen opacity) to 20
    for i in range(100):  # loop 100 times
        fill.set_alpha(alpha)  # set the black screen opacity accordingly
        alpha -= speed  # subtract alpha by the speed
        window.blit(fill, (0, 0))  # blit the dark screen
        pygame.display.update()  # update the screen
    import gameplay  # import gameplay file

    gameplay.game(map, level)  # call the game function from the gameplay file (starts the real game)


def aftergame(win, mapC, levelC):  # aftergame function for after the game
    global level, map, level_lock  # globalize level, map, and level_lock
    level = levelC  # set the level to levelC
    map = mapC
    if level != 5 and level_lock[map][level + 1] == False and win:  # if the level isn't 5 (last level) and the level
        # is locked
        level_lock[map][level + 1] = True  # unlock the level
    over = True  # set over to true
    buttons = []  # initialize buttons array
    draw.rect(window, (97, 56, 29), (250, 170, 500, 400), 0, 15, 15, 15, 15)  # draw the game over screen
    draw.rect(window, (207, 159, 111), (270, 190, 460, 360), 0, 15, 15, 15, 15)

    if win and level != 5:  # if the player won the game and isn't on the last level
        pygame.mixer.music.load("music/game won.wav")  # play the game won music
        mixer.music.set_volume(0.7)
        text = load("aftergame/Level_Completed.png")  # blit the level completed text
        for i in range(4):  # append all appropriate buttons
            buttons.append(window.blit(load_button[i], (460 + (len(buttons) - 1.5) * 100, 400)))
    elif win and level == 5:  # if the player won the last level
        pygame.mixer.music.load("music/game won.wav")  # play the game won music
        mixer.music.set_volume(0.7)
        text = load("aftergame/Map_Cleared.png")  # blit map cleared to the screen
    else:  # if the player lost the game
        pygame.mixer.music.load("music/game over.wav")  # play the game over sound
        mixer.music.set_volume(0.7)
        text = load("aftergame/Game_Over.png")  # blit the game over text
    pygame.mixer.music.play()  # play the winning/losing sound effects
    window.blit(text, (500 - text.get_width() / 2, 230))  # blit the appropriate text to the screen
    if len(buttons) == 0:  # if there aren't any buttons in the button array
        for i in range(3):  # append the 3 mandatory buttons in the array (replay, homescreen, level select screen)
            buttons.append(window.blit(load_button[i], (460 + (len(buttons) - 1) * 130, 400)))
    pygame.display.update()  # update the screen
    while over:  # while over is true
        clock.tick(60)  # set fps to 60
        for event in pygame.event.get():
            try_exit(event)
            mouse = pygame.mouse.get_pos()  # get the position of the player's mouse
            if event.type == pygame.MOUSEBUTTONDOWN:  # if the player clicks
                if buttons[0].collidepoint(mouse):  # if the player clicks on button 0
                    level = -1  # reset the level
                    over = False  # end the aftergame screen loop
                    choose_map()  # go to map select screen
                elif buttons[1].collidepoint(mouse):  # if the player clicks on button 1
                    level = -1  # reset the level
                    over = False  # end the aftergame screen loop
                    choose_level()  # go to the choose level screen
                elif buttons[2].collidepoint(mouse):  # if the player clicks on button 2
                    blackout()  # call blackout (replay)
                    over = False  # end the aftergame screen loop
                elif len(buttons) == 4 and buttons[3].collidepoint(mouse):  # if the player clicks on button 3
                    level += 1  # increase the level by 1
                    blackout()  # call blackout (play the next level of the same map)
                    over = False  # end the aftergame screen loop


def starting():  # starting screen
    start = True  # set start to true
    startingImage = load("start/start.png")  # set the starting image to the default image
    # store the mouse gif images in list mouse
    mouse = [transform.scale(load("start/blank.png"), (50, 72)), transform.scale(load("start/left.png"), (50, 72))]
    scaled = transform.scale(startingImage, (int(1000 * 1.1), int(750 * 1.1)))  # set the larger logo image
    count = 1  # set count to 1
    while start:  # while start is true
        clock.tick(30)  # set fps to 30
        for event in pygame.event.get():
            try_exit(event)
        pos = pygame.mouse.get_pos()  # get the mouse position
        if not colourCollision(black, pos):  # if the mouse is not colliding with the colour black (background colour)
            window.blit(scaled,
                        (1000 - int(1000 * 1.2) + 160, 750 - int(750 * 1.2) + 120))  # blit the larger logo image
            # onto the screen
            if pygame.mouse.get_pressed()[0]:  # if the user clicks on the logo
                wait(100)  # wait 100 ms (to prevent spamming which will cause bugs)
                start = False  # end the starting screen
        else:  # if the mouse is colliding with the colour black
            window.blit(startingImage, (0, 0))  # blit the default starting screen logo
        window.blit(mouse[round(count)], (900, 40))  # blit the appropriate mouse gif frame to the screen
        count += 0.03  # increase count by 0.03
        if count > 1:  # if count is above 1
            count = 0  # reset count to 0
        pygame.display.update()  # update the screen


if __name__ == "__main__":  # main
    starting()  # call starting screen
    while True:  # while true
        choose_map()  # call the choose map screen
