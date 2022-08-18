import pygame
from pygame.sprite import Sprite
from settings import *


class Bullet(Sprite):
    def __init__(self, screen, player):
        super().__init__()
        self.screen = screen
        self.player = player
        self.direction = self.player.player_turn
        self.rect = pygame.Rect(self.player.x, self.player.y, bullet_width, bullet_height)
        self.rect.top = self.player.rect.top

        self.y_b = float(self.rect.y)
        self.x_b = float(self.rect.x)

    def update(self):
        if self.direction == 'up':
            self.y_b -= bullet_speed
            self.rect.y = self.y_b
        elif self.direction == 'down':
            self.y_b += bullet_speed
            self.rect.y = self.y_b
        elif self.direction == 'left':
            self.x_b -= bullet_speed
            self.rect.x = self.x_b
        elif self.direction == 'right':
            self.x_b += bullet_speed
            self.rect.x = self.x_b

    def draw_bullet(self):
        pygame.draw.rect(self.screen, GREEN, self.rect)
