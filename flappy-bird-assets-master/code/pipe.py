import pygame
from random import randint
from random import choice
from settings import *


class Pipe(pygame.sprite.Sprite):
    def __init__(self, playing):
        super().__init__()

        self.y_pos = randint(200, 680)

        self.image = choice([pygame.image.load(r'../sprites/pipe-green.png').convert_alpha(),
                             pygame.image.load(r'../sprites/pipe-red.png').convert_alpha()])

        self.image = pygame.transform.scale(self.image, (104, 640))
        self.rect = self.image.get_rect(topleft=(700, self.y_pos))

        self.image2 = pygame.transform.rotate(self.image, 180)
        self.image2 = pygame.transform.flip(self.image2, True, False)
        self.rect2 = self.image2.get_rect(topleft=(700, self.y_pos - 800))
        self.display_surface = pygame.display.get_surface()

        if playing:
            self.speed = PIPESPEED
        else:
            self.speed = 0

    def custom_draw(self):
        self.display_surface.blit(self.image, self.rect)
        self.display_surface.blit(self.image2, self.rect2)

    def movement(self):
        self.rect.x -= self.speed
        self.rect2.x -= self.speed

    def get_bottom_rect(self):
        return self.rect2

    def get_top_rect(self):
        return self.rect

    def update(self):
        self.custom_draw()
        self.movement()
