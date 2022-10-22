import pygame, sys
from pygame.locals import *
import functions
pygame.init()
score = None

while True:
    pygame.display.set_caption('Astrorun')
    screen = pygame.display.set_mode((512, 480))
    clock = pygame.time.Clock()

    player = functions.Player(20, 440, 20, 30)
    obstacle = functions.Objects(512, 440, 10, 10)
    powerup = functions.Powers(400, 350, 29, 48)
    title = functions.Title(250, 1)
    game_over = functions.Gameover(20, player.y)
    background = functions.Background(0, 0, 0)
    while True:
        pygame.event.get()
        screen.fill((0, 0, 0))
        k = pygame.key.get_pressed()
        title.main(screen, score)
        pygame.mixer.music.load('Sound\song.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        if title.main(screen, score) == 1:
            break

        if k[K_ESCAPE]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)

    while True:
        pygame.event.get()
        k = pygame.key.get_pressed()
        screen.fill((255, 255, 255))

        background.main(screen, obstacle.object_vel)
        powerup.main(screen)
        obstacle.main(screen)
        score = obstacle.point
        player.main(screen, powerup.power_rect)

        if player.collision1(obstacle.obstacle_rect) == 2:
            game_over = functions.Gameover(20, player.y)
            break

        if k[K_ESCAPE]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)

    while True:
        pygame.event.get()
        k = pygame.key.get_pressed()
        dim = game_over.screen_dim
        screen.fill((dim, dim, dim))
        game_over.main(screen)
        if game_over.game_over == 1:
            break

        if k[K_ESCAPE]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)
