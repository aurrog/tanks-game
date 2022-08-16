import pygame
from settings import *
from player import Player
from map import world_map
from pygame.sprite import Group


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bullets = Group()
player = Player(screen, bullets)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement(screen, player)
    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, player.pos, 12)
    bullets.update()
    player.draw_bullets()
    # player.draw_player()
    for x, y in world_map:
        pygame.draw.rect(screen, BRICK_COLOR, (x, y, TILE, TILE))

    pygame.display.flip()
    clock.tick(FPS)
