import pygame, sys
from pygame.locals import *
import functions
pygame.init()

while True:
    pygame.display.set_caption('Astrorun')
    screen = pygame.display.set_mode((512, 480))
    clock = pygame.time.Clock()

    player = functions.Player(20, 440, 20, 30)
    player_flying = functions.Playerflying(20, 440, 20, 30)
    obstacle = functions.Objects(512, 440, 10, 10)
    powerup = functions.Powers(512, 350, 10, 10)
    title = functions.Title(250, 1)
    game_state = 0
    power_state = 0

    while True:
        pygame.event.get()
        screen.fill((0, 0, 0))
        k = pygame.key.get_pressed()
        title.main(screen)

        if title.main(screen) == 1:
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

        if power_state == 2:
            None

        player.main(screen)
        obstacle.main(screen)
        powerup.main(screen)

        if game_state == 2:
            pygame.quit()
            sys.exit()

        if k[K_ESCAPE]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)
