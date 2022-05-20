import pygame.sprite

from lines import *
from balls import *


def main():
    # spiral variable
    x_s, y_s = spiral()
    # straight line rotate variable
    ball_list = []
    pic = pygame.sprite.Sprite()
    pic.rect = Rect((100, 110), (22, 22))
    pic.image = pygame.image.load("balls/00.png")
    for i in range(10):
        ball_list.append(pokeballs(1, 700 - i * 22, 100, 0))
    for i in range(5):
        ball_list.append(pokeballs(4, 700 - 220 - i * 22, 100, 0))

    while True:  # main game loop
        clock.tick(60)
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you quit pygame
                pygame.quit()  # quit pygame
                sys.exit()  # exit the system

        # change the ball position base on the collision with straight lines
        for ball in ball_list:
            ball.rect.center = ball.pos
            follow_lines(ball)
            ball.draw(window)

        # draw the spiral dots
        spiral_lines = draw_spiral(x_s, y_s)
        window.blit(pic.image, pic.rect.topleft)
        for i in range(len(spiral_lines)):
            if pic.rect.colliderect(spiral_lines[i]):
                print(i)

        pygame.display.update()


if __name__ == "__main__":
    main()
