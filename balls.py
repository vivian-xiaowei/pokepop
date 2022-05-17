import pygame
import pygame.sprite


sprites = [[] for i in range(7)]
for i in range(7):
    for j in range(8):
        sprites[i].append(pygame.image.load("balls/" + str(i) + str(j) + ".png"))


# class Ball(pygame.sprite.Sprite):
#     def __int__(self, image):
#         super().__init__()
#         self.image = image
#         self.rect = self.image.get_rect()

