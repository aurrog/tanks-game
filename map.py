import pygame
from settings import *
from pygame.sprite import Sprite


class Wall(Sprite):
    def __init__(self, screen, coordination):
        super().__init__()
        self.screen = screen
        self.coordination = coordination
        self.rect = pygame.Rect(coordination[0], coordination[1], TILE, TILE)

    def draw_walls(self):
        pygame.draw.rect(self.screen, BRICK_COLOR, self.coordination)


text_map = ['0000000000000',
            '0101011101010',
            '0100011100010',
            '0110001000110',
            '0111100011110',
            '0000000000000',
            '1101101011011',
            '0000000000000',
            '0110111110110',
            '0010001000100',
            '0010000000100',
            '0000011100000',
            '1000010100001']

collision_walls = []
world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '1':
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            world_map.add((i * TILE, j * TILE))
