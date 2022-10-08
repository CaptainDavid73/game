import pygame, sys
from pygame.locals import *
import random


class Player():
    # player values and init.
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.jump = False
        self.slide = False
        self.slide_time = 10
        self.vel = 10
        self.animation_run = 1
        self.animation_jump = 1
        self.run_ani = 0
        self.jump_ani = 0
        self.run_blit = pygame.image.load(f'Art\Run_animation\{self.animation_run}.png')
        self.jump_blit = pygame.image.load(f'Art\Jump_animation\{self.animation_jump}.png')
        self.slide_blit = pygame.image.load('Art\Slide_animation\slide.png')

    # main loop function.
    def main(self, screen):
        self.player_rect = pygame.Rect(self.x, self.y, self.run_blit.get_width(), self.run_blit.get_height())
        # pygame.draw.rect(screen, (0, 0, 0), self.player_rect)
        if self.y > 440:
            screen.blit(self.run_blit, (self.x, 450))
        else:
            screen.blit(self.run_blit, (self.x, self.y))
        self.move()
        self.animation()

    # movement mechanics for jumping and sliding.
    def move(self):
        pygame.event.get()
        k = pygame.key.get_pressed()
        if self.jump is False and k[K_SPACE] or k[K_UP]:
            self.jump = True
        if self.jump is True:
            self.y -= self.vel * 1.0
            self.vel -= 0.5
            if self.vel < -10:
                self.jump = False
                self.vel = 10

        if self.slide is False and k[K_DOWN]:
            self.slide = True
        if self.slide is True:
            self.y += self.slide_time * 0.2
            self.slide_time -= 0.5
            if self.slide_time < -10:
                self.slide = False
                self.slide_time = 10

    # animations for running, jumping and sliding.
    def animation(self):
        self.run_ani += 1
        if self.run_ani >= 7 and self.jump is False and self.slide is False:
            self.animation_run += 1
            self.run_ani = 1
            if self.animation_run > 4:
                self.animation_run = 1
            self.run_blit = pygame.image.load(f'Art\Run_animation\{self.animation_run}.png')

        if self.jump is True:
            if 400 >= self.y >= 355 and self.vel > 0:
                self.jump_ani += 1
                if self.jump_ani == 4:
                    self.jump_ani = 0
                if self.jump_ani <= 2:
                    self.animation_jump = 2
                else:
                    self.animation_jump = 3
            if 335 < self.y <= 400 and self.vel < 0:
                self.jump_ani += 1
                if self.jump_ani == 4:
                    self.jump_ani = 0
                if self.jump_ani <= 2:
                    self.animation_jump = 4
                else:
                    self.animation_jump = 5
            if self.y > 400 and self.vel < 0:
                self.animation_jump = 6
            self.run_blit = pygame.image.load(f'Art\Jump_animation\{self.animation_jump}.png')

        if self.y > 440:
            self.animation_run = 5
            self.run_blit = pygame.image.load('Art\Slide_animation\slide.png')

    def collision(self, obs_rect):
        game_state = 0
        if self.player_rect.colliderect(obs_rect):
            game_state = 1
        return game_state


class Objects():

    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.object_vel = 5

    def main(self, screen):
        self.obstacle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (0, 0, 0), self.obstacle_rect)
        self.move()

    def move(self):
        self.x -= self.object_vel
        if self.x < 0 - self.width:
            self.x = 512
