from settings import *
import pygame
from map import collision_walls


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x, self.y = player_pos
        self.side = 30
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.player_surf = pygame.image.load('images/pixil-frame-0 (8).png').convert_alpha()
        self.player_surf = pygame.transform.scale(self.player_surf, (self.player_surf.get_width()*1.5, self.player_surf.get_width()*1.2))
        self.player_rect = self.player_surf.get_rect(center=player_pos)

        self.player_up = self.player_surf
        self.player_down = pygame.transform.flip(self.player_surf, 0, 1)
        self.player_left = pygame.transform.rotate(self.player_surf, 90)
        self.player_right = pygame.transform.rotate(self.player_surf, -90)
        self.player_now = self.player_up

    @property
    def pos(self):
        return self.x, self.y

    def detect_collisions(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(collision_walls)

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

    def movement(self):
        self.key_move()
        self.rect.center = self.x, self.y

    def key_move(self):
        keys = pygame.key.get_pressed()
        # self.x += player_speed
        # if self.x > 770:
        #     self.x = 770

        if keys[pygame.K_w]:
            self.player_now = self.player_up
            if self.y <= 15:
                self.y = 15
            else:
                self.detect_collisions(0, self.y - self.y - player_speed)
        elif keys[pygame.K_s]:
            self.player_now = self.player_down
            if self.y >= 765:
                self.y = 765
            else:
                self.detect_collisions(0, self.y - self.y + player_speed)
        elif keys[pygame.K_a]:
            self.player_now = self.player_left
            if self.x <= 15:
                self.x = 15
            else:
                self.detect_collisions(self.x - self.x - player_speed, 0)
        elif keys[pygame.K_d]:
            self.player_now = self.player_right
            if self.x >= 765:
                self.x = 765
            else:
                self.detect_collisions(self.x - self.x + player_speed, 0)

    def draw_player(self):
        self.screen.blit(self.player_now, self.pos)
