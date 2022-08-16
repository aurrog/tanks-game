import pygame
from pygame.sprite import Sprite
from settings import *


class Bullet(Sprite):
    def __init__(self, screen, player):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(player.x, player.y, bullet_width, bullet_height)
        self.rect.top = player.rect.top

        self.y_b = float(self.rect.y)

    def update(self):
        self.y_b -= bullet_speed
        self.rect.y = self.y_b

    def draw_bullet(self):
        pygame.draw.rect(self.screen, GREEN, self.rect)
