import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load(r'C:\tristan\python\flappybird\flappy-bird-assets-master\sprites\bluebird-downflap.png').convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (68, 48))
        self.image2 = pygame.image.load(r'C:\tristan\python\flappybird\flappy-bird-assets-master\sprites\bluebird-midflap.png').convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (68, 48))
        self.image3 = pygame.image.load(r'C:\tristan\python\flappybird\flappy-bird-assets-master\sprites\bluebird-upflap.png').convert_alpha()
        self.image3 = pygame.transform.scale(self.image3, (68, 48))

        self.animation_list = [self.image1, self.image2, self.image3]
        self.image = self.animation_list[0]
        self.anim_index = 0

        self.jump = pygame.mixer.Sound(r'C:\tristan\python\flappybird\flappy-bird-assets-master\audio\wing.wav')
        self.jump.set_volume(0.02)

        self.rect = self.image.get_rect(midbottom=(WINDOW_SIZE[0] / 2 - self.image.get_rect().width, WINDOW_SIZE[1] / 2))
        self.gravity = 0

    def animation(self):
        self.image = self.animation_list[int(self.anim_index)]
        self.anim_index += 0.1

        if self.anim_index > 2.5:
            self.anim_index = 0

    def input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self.gravity = -8
            if pygame.mixer.get_busy() == 0:
                self.jump.play()

    def apply_gravity(self):
        self.gravity += 0.7
        self.rect.y += self.gravity

    def update(self):
        self.input()
        self.apply_gravity()
        self.animation()

