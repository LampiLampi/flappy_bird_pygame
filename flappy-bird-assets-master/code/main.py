import pygame
import sys
from settings import *
from player import Player
from pipe import Pipe


class Game:
    def __init__(self):
        icon = pygame.image.load(r'../favicon.ico')
        pygame.display.set_caption('Flappy Bird')
        pygame.display.set_icon(icon)
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        self.death_sound = pygame.mixer.Sound(r'../audio/die.wav')
        self.death_sound.set_volume(0.4)
        self.point_sound = pygame.mixer.Sound(r'../audio/point.wav')
        self.point_sound.set_volume(0.4)

        self.background_image = pygame.image.load(r'../sprites/background-day.png').convert()
        self.background_image = pygame.transform.scale(self.background_image, (576, 1024))
        self.background_rect = self.background_image.get_rect(topleft=(0, 0))

        self.ground = pygame.image.load(r'../sprites/base.png')
        self.ground = pygame.transform.scale(self.ground, (672, 224))
        self.ground_rect = self.ground.get_rect(topleft=(0, 700))
        self.moved = 0

        self.pipenew_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.pipenew_event, 2800)

        self.clock = pygame.time.Clock()
        self.player = pygame.sprite.GroupSingle()
        self.pipes = pygame.sprite.Group()
        self.player.add(Player())
        self.alive = True

        self.title_screen = pygame.image.load(r'../sprites/message.png').convert_alpha()
        self.title_screen = pygame.transform.scale(self.title_screen, (368, 534))
        self.title_screen_rect = self.title_screen.get_rect(topleft=(100, 100))

        self.score_0 = pygame.image.load(r'../sprites/0.png').convert_alpha()
        self.score_1 = pygame.image.load(r'../sprites/1.png').convert_alpha()
        self.score_2 = pygame.image.load(r'../sprites/2.png').convert_alpha()
        self.score_3 = pygame.image.load(r'../sprites/3.png').convert_alpha()
        self.score_4 = pygame.image.load(r'../sprites/4.png').convert_alpha()
        self.score_5 = pygame.image.load(r'../sprites/5.png').convert_alpha()
        self.score_6 = pygame.image.load(r'../sprites/6.png').convert_alpha()
        self.score_7 = pygame.image.load(r'../sprites/7.png').convert_alpha()
        self.score_8 = pygame.image.load(r'../sprites/8.png').convert_alpha()
        self.score_9 = pygame.image.load(r'../sprites/9.png').convert_alpha()
        self.scorelist = []
        self.passed_time = 0


    def spawn_handling(self):
        self.pipes.add(Pipe(playing=True))
        for pipe in self.pipes:
            if pipe.rect.x < -100:
                self.pipes.remove(pipe)

    def update_score(self):
        curr_score = (pygame.time.get_ticks() - self.passed_time) // 1000

        for num in list(str(curr_score))[0]:
            num = int(num)
            if num == 0:
                self.screen.blit(self.score_0, self.score_0.get_rect(topleft=(260, 20)))
            if num == 1:
                self.screen.blit(self.score_1, self.score_1.get_rect(topleft=(260, 20)))
            if num == 2:
                self.screen.blit(self.score_2, self.score_2.get_rect(topleft=(260, 20)))
            if num == 3:
                self.screen.blit(self.score_3, self.score_3.get_rect(topleft=(260, 20)))
            if num == 4:
                self.screen.blit(self.score_4, self.score_4.get_rect(topleft=(260, 20)))
            if num == 5:
                self.screen.blit(self.score_5, self.score_5.get_rect(topleft=(260, 20)))
            if num == 6:
                self.screen.blit(self.score_6, self.score_6.get_rect(topleft=(260, 20)))
            if num == 7:
                self.screen.blit(self.score_7, self.score_7.get_rect(topleft=(260, 20)))
            if num == 8:
                self.screen.blit(self.score_8, self.score_8.get_rect(topleft=(260, 20)))
            if num == 9:
                self.screen.blit(self.score_9, self.score_9.get_rect(topleft=(260, 20)))

        if len(str(curr_score)) > 1:
            for num in list(str(curr_score))[1]:
                num = int(num)
                if num == 0:
                    self.screen.blit(self.score_0, self.score_0.get_rect(topleft=(280, 20)))
                if num == 1:
                    self.screen.blit(self.score_1, self.score_0.get_rect(topleft=(280, 20)))
                if num == 2:
                    self.screen.blit(self.score_2, self.score_0.get_rect(topleft=(280, 20)))
                if num == 3:
                    self.screen.blit(self.score_3, self.score_0.get_rect(topleft=(280, 20)))
                if num == 4:
                    self.screen.blit(self.score_4, self.score_0.get_rect(topleft=(280, 20)))
                if num == 5:
                    self.screen.blit(self.score_5, self.score_0.get_rect(topleft=(280, 20)))
                if num == 6:
                    self.screen.blit(self.score_6, self.score_0.get_rect(topleft=(280, 20)))
                if num == 7:
                    self.screen.blit(self.score_7, self.score_0.get_rect(topleft=(280, 20)))
                if num == 8:
                    self.screen.blit(self.score_8, self.score_0.get_rect(topleft=(280, 20)))
                if num == 9:
                    self.screen.blit(self.score_9, self.score_0.get_rect(topleft=(280, 20)))

    def move_ground(self):
        self.ground_rect.right -= PIPESPEED
        self.moved += 1

        if self.moved >= 16:
            self.ground_rect.right = 650
            self.moved = 0

    def collision(self):
        if self.player.sprite.rect.colliderect(self.ground_rect):
            self.alive = False
            self.death_sound.play()
            print('collided with ground')

        if pygame.sprite.spritecollide(self.player.sprite, self.pipes, False):
            self.alive = False
            self.death_sound.play()
            print('collided with pipes')

    def run(self):
        while True:
            while self.alive:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == self.pipenew_event:
                        self.spawn_handling()

                self.screen.fill('black')
                self.screen.blit(self.background_image, self.background_rect)
                self.player.draw(self.screen)
                self.player.update()
                self.pipes.update()
                self.move_ground()
                self.screen.blit(self.ground, self.ground_rect)
                self.collision()
                self.update_score()

                pygame.display.update()
                self.clock.tick(FPS)

            while not self.alive:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()

                        if keys[pygame.K_SPACE]:
                            self.alive = True
                            self.passed_time = pygame.time.get_ticks()
                            self.player = pygame.sprite.GroupSingle()
                            self.pipes = pygame.sprite.Group()
                            self.player.add(Player())

                self.screen.blit(self.title_screen, self.title_screen_rect)
                pygame.display.update()
                self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
