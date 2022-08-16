import pygame
from settings import *


def draw_walls(walls):
    for brick in walls.sprites():
        brick.draw_walls()


def draw_player(player, screen, bullets, walls):
    player.movement(screen, player)
    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, player.pos, 12)
    bullets.update()
    player.draw_bullets(walls)
    # player.draw_player()

    draw_walls(walls)

    pygame.display.flip()

