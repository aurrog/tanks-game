import pygame
from settings import *
from player import Player
from map import world_map
from pygame.sprite import Group
from map import Wall
import drawing as dg


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bullets = Group()
walls = Group()
player = Player(screen, bullets)

for x, y in world_map:
    new_wall = Wall(screen, (x, y, TILE, TILE))
    walls.add(new_wall)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    dg.draw_player(player, screen, bullets, walls)
    clock.tick(FPS)

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
