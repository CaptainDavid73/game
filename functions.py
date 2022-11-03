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
        self.tp_animation = 1
        self.run_ani = 0
        self.jump_ani = 0
        self.tp_ani = 0
        self.power_state = 1
        self.tick = 0
        self.player_tick = 0
        self.power_percent = 0
        self.play_soundjump = False
        self.play_soundslide = False
        self.run_blit = pygame.image.load(f'Art\Run_animation\{self.animation_run}.png')
        self.jump_blit = pygame.image.load(f'Art\Jump_animation\{self.animation_jump}.png')
        self.slide_blit = pygame.image.load('Art\Slide_animation\slide.png')
        self.tp_blit = pygame.image.load(f'Art\TP_animation\{self.tp_animation}.png')
        self.font = pygame.font.Font('Fonts\jdide.ttf', 10)
        self.jump_sound = pygame.mixer.Sound('Sound\Jump.ogg')
        self.slide_sound = pygame.mixer.Sound('Sound\slide.ogg')

    # main loop function.
    def main(self, screen, power_rect):
        self.player_rect = pygame.Rect(self.x, self.y, self.run_blit.get_width(), self.run_blit.get_height())
        # pygame.draw.rect(screen, (0, 0, 0), self.player_rect)
        self.collision2(power_rect)
        if self.power_state == 1:
            self.power_percent = 0
            if self.y > 440:
                screen.blit(self.run_blit, (self.x, 445))
            else:
                screen.blit(self.run_blit, (self.x, self.y))
            self.move()
        else:
            self.power_percent = 100
            self.tick += 1
            if self.tick > 300:
                self.power_state = 1
                self.tick = 0
            if self.y > 440:
                screen.blit(self.run_blit, (self.x, 445))
            else:
                screen.blit(self.run_blit, (self.x, self.y))
            self.flying()
        self.sound()
        self.animation()
        self.player_tick = self.font.render(('POWER: ' + str(round(self.power_percent-(self.tick / 3), 1)) + ' %'), True, '#FFFFFF')
        screen.blit(self.player_tick, (10, 30))

    # movement mechanics for jumping and sliding.
    def move(self):
        pygame.event.get()
        k = pygame.key.get_pressed()

        if self.jump is False and k[K_UP]:
            self.jump = True

        if self.jump is True:
            self.y -= self.vel * 1.0
            self.vel -= 0.5
            if self.y > 450:
                self.y = 440
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

    def sound(self):
        if self.jump is True:
            if self.play_soundjump is False:
                self.play_soundjump = True
                self.jump_sound.play()
        else:
            self.play_soundjump = False

        if self.slide is True:
            if self.play_soundslide is False:
                self.play_soundslide = True
                self.slide_sound.play()
        else:
            self.play_soundslide = False
    # animations for running, jumping and sliding.
    def animation(self):
        self.run_ani += 1
        if self.run_ani >= 7 and self.jump is False and self.slide is False:
            self.animation_run += 1
            self.run_ani = 1
            if self.animation_run > 4:
                self.animation_run = 1
            self.run_blit = pygame.image.load(f'Art\Run_animation\{self.animation_run}.png')

        if self.jump is True and self.power_state == 1:
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

        if self.jump is True and self.power_state == 2:
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

    def flying(self):
        pygame.event.get()
        k = pygame.key.get_pressed()
        if k[K_UP]:
            self.jump = True
            self.vel = 7

        if self.jump is True:
            self.y -= self.vel * 1.0
            self.vel -= 0.5
            if self.y > 439:
                self.y = 440
                self.jump = False
                self.vel = 0
        if self.slide is False and k[K_DOWN]:
            self.slide = True
        if self.slide is True:
            self.y += self.slide_time * 0.2
            self.slide_time -= 0.5
            if self.slide_time < -10:
                self.slide = False
                self.slide_time = 10

    # Collision detection
    def collision1(self, obs_rect):
        game_state = 1
        if self.player_rect.colliderect(obs_rect):
            game_state = 2
        if self.y < 0:
            game_state = 2
        return game_state

    def collision2(self, pow_rect):
        if self.player_rect.colliderect(pow_rect):
            self.power_state = 2


class Objects():

    # Object values and init
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.object_vel = 5
        self.height_change = 0
        self.point = 0
        self.font = pygame.font.Font('Fonts\jdide.ttf', 10)

    # Main loop function
    def main(self, screen):
        self.obstacle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # pygame.draw.rect(screen, (0, 0, 0), self.obstacle_rect)
        self.player_points = self.font.render(('POINTS: ' + str(self.point)), True, '#FFFFFF')
        self.move()
        self.points()
        self.object_blit = pygame.image.load(f'Art\Object_animation\{self.object_animation}.png')
        self.object_animation = 1
        screen.blit(self.player_points, (10, 10))
        screen.blit(self.object_blit, (self.x, self.y - 17))

    # object movements and mechanics
    def move(self):
        self.x -= self.object_vel
        if self.x < 0 - self.width:
            self.x = 512
            self.height_change = random.randint(0, 4)
        if self.height_change == 0:
            self.y = 430
            self.width = 50
            self.height = 50
            self.object_animation = 1
        elif self.height_change == 1:
            self.y = 410
            self.width = 40
            self.height = 70
            self.object_animation = 2
        elif self.height_change == 2:
            self.y = 400
            self.width = 30
            self.height = 80
            self.object_animation = 3
        elif self.height_change == 3:
            self.y = 300
            self.width = 30
            self.height = 150
            self.object_animation = 4
        elif self.height_change == 4:
            self.y = 300
            self.width = 40
            self.height = 150
            self.object_animation = 5

    # point system and speed
    def points(self):
        if self.x < 0:
            self.point = self.point + 10
            if self.point <= 1000:
                self.object_vel += 0.01
            else:
                self.object_vel += 0.01 + (self.point / 100000)
            if self.object_vel > 11:
                self.object_vel = 10


class Title():

    def __init__(self, y, vel):
        self.y = y
        self.vel = vel
        self.title_blit = pygame.image.load('Art\Titlescreen_animation\TitleScreen.png.')
        self.title_start_blit = pygame.image.load('Art\Titlescreen_animation\TitleScreenStart.png.')
        self.font = pygame.font.Font('Fonts\jdide.ttf', 20)

    def main(self, screen, score):
        if score is not None:
            self.font = pygame.font.Font('Fonts\jdide.ttf', 10)
            self.player_points = self.font.render(('YOUR SCORE WAS: ' + str(score)), True, '#FFFFFF')
            screen.blit(self.player_points, (10, 20))
        pygame.event.get()
        k = pygame.key.get_pressed()

        self.y -= self.vel
        screen.blit(self.title_blit, (0, self.y))
        if k[K_RETURN]:
            self.vel = 3
        else:
            self.vel = 1
        if self.y < 0:
            self.vel = 0
            screen.blit(self.title_start_blit, (0, self.y))
            if k[K_RETURN]:
                return 1
        return 0


class Powers():

    # Object values and init
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.object_vel = 5
        self.power_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.power_blit = pygame.image.load('Art\Background\Powerup.png')

    # Main loop function
    def main(self, screen):
        self.power_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # pygame.draw.rect(screen, (0, 0, 0), self.power_rect)
        if self.x > 19:
            screen.blit(self.power_blit, (self.x, self.y))
        self.move()

    # object movements and mechanics
    def move(self):
        self.x -= self.object_vel
        if self.x < 0:
            self.x = 5000


class Gameover():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.tp_ani = 0
        self.tp_animation = 1
        self.game_over = 0
        self.screen_dim = 255
        self.dead_blit = pygame.image.load(f'Art\Dead_animation\gOver.png')
        self.tp_blit = pygame.image.load(f'Art\TP_animation\{self.tp_animation}.png')

    def main(self, screen):
        if self.y < 0:
            self.y = 0
        self.screen_dim -= 10
        if self.screen_dim <= 0:
            self.screen_dim = 0
        if self.y < 441:
            screen.blit(self.dead_blit, (self.x, self.y))
        self.y -= self.vel * 1.0
        self.vel -= 0.5
        if self.y >= 441:
            self.y = 441
            self.tp_ani += 1
            if self.tp_ani >= 4:
                self.tp_animation += 1
                self.tp_ani = 0
                if self.tp_animation > 5:
                    self.game_over = 1
                    self.tp_animation = 1
                    pygame.time.delay(500)
            self.tp_blit = pygame.image.load(f'Art\TP_animation\{self.tp_animation}.png')
            screen.blit(self.tp_blit, (self.x, self.y))


class Background():

    def __init__(self, x, y, x1):
        self.x, self.y = x, y
        self.x_accent = x1
        self.speed_indicator = 0
        self.background_blit = pygame.image.load(f'Art\Background\Background.png')
        self.stars_blit = pygame.image.load(f'Art\Background\StarsBackground1.png')

    def main(self, screen, vel):
        self.vel = vel
        self.x -= self.vel
        self.x_accent -= self.vel/2
        if self.x < -1040:
            self.x = 0
        if self.x_accent < -1040:
            self.x_accent = 0
        screen.blit(self.background_blit, (self.x, self.y))
        screen.blit(self.stars_blit, (self.x_accent, self.y))

