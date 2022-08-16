from settings import *
import pygame
from map import collision_walls
from bullet import Bullet


class Player:
    def __init__(self, screen, bullets):
        self.screen = screen
        self.x, self.y = player_pos
        print(self.x, self.y)
        self.side = 25
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.player_turn = 'up'
        print(self.rect)
        self.bullets = bullets

    @property
    def pos(self):
        return self.x, self.y

    def detect_collisions(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(collision_walls)
        print(hit_indexes)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = collision_walls[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self, screen, player):
        self.key_move(screen, player)
        self.rect.center = self.x, self.y

    def key_move(self, screen, player):
        keys = pygame.key.get_pressed()
        # self.x += player_speed
        # if self.x > 770:
        #     self.x = 770

        if keys[pygame.K_w]:
            self.player_turn = 'up'
            if self.y <= 15:
                self.y = 15
            else:
                self.detect_collisions(0, self.y - self.y - player_speed)
        elif keys[pygame.K_s]:
            self.player_turn = 'down'
            if self.y >= 765:
                self.y = 765
            else:
                self.detect_collisions(0, self.y - self.y + player_speed)
        elif keys[pygame.K_a]:
            self.player_turn = 'left'
            if self.x <= 15:
                self.x = 15
            else:
                self.detect_collisions(self.x - self.x - player_speed, 0)
        elif keys[pygame.K_d]:
            self.player_turn = 'right'
            if self.x >= 765:
                self.x = 765
            else:
                self.detect_collisions(self.x - self.x + player_speed, 0)
        if keys[pygame.K_SPACE]:
            # if bullets_len != 2:
            new_bullet = Bullet(screen, player)
            self.bullets.add(new_bullet)

    def draw_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

