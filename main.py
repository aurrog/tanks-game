import pygame
from settings import *
from player import Player
from map import world_map


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    sc.fill(BLACK)

    pygame.draw.circle(sc, GREEN, player.pos, 12)

    for x, y in world_map:
        pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE))

    pygame.display.flip()
    clock.tick(FPS)
