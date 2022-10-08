import pygame, sys
from pygame.locals import *
import functions

# l
pygame.init()
screen = pygame.display.set_mode((512, 480))
clock = pygame.time.Clock()

player = functions.Player(20, 440, 20, 30)
obstacle = functions.Objects(512, 440, 10, 10)
game_state = 0

while True:
    pygame.event.get()
    k = pygame.key.get_pressed()
    screen.fill((255, 255, 255))
    player.main(screen)
    obstacle.main(screen)
    game_state = player.collision(obstacle.obstacle_rect)
    if game_state == 1:
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