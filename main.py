import pygame
from settings import *
from player import Player
from map import world_map


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(BLACK)

    player.draw_player()
    for x, y in world_map:
        pygame.draw.rect(screen, BRICK_COLOR, (x, y, TILE, TILE))

    pygame.display.flip()
    clock.tick(FPS)
