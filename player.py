from settings import *
import pygame
import map as wp
from bullet import Bullet


class Player:
    def __init__(self, screen, bullets):
        self.screen = screen
        self.x, self.y = player_pos
        self.side = 25
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.player_turn = 'up'
        self.bullets = bullets

    @property
    def pos(self):
        return self.x, self.y

    def detect_collisions(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(wp.collision_walls)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = wp.collision_walls[hit_index]
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
            if self.y <= TILE/4:
                self.y = TILE/4
            else:
                self.detect_collisions(0, self.y - self.y - player_speed)
        elif keys[pygame.K_s]:
            self.player_turn = 'down'
            if self.y >= WIDTH-TILE/4:
                self.y = WIDTH-TILE/4
            else:
                self.detect_collisions(0, self.y - self.y + player_speed)
        elif keys[pygame.K_a]:
            self.player_turn = 'left'
            if self.x <= TILE/4:
                self.x = TILE/4
            else:
                self.detect_collisions(self.x - self.x - player_speed, 0)
        elif keys[pygame.K_d]:
            self.player_turn = 'right'
            if self.x >= WIDTH-TILE/4:
                self.x = WIDTH-TILE/4
            else:
                self.detect_collisions(self.x - self.x + player_speed, 0)
        if keys[pygame.K_SPACE]:
            if len(self.bullets) != bullet_allowed:
                new_bullet = Bullet(screen, player)
                self.bullets.add(new_bullet)

    def bullet_collision(self, walls, bullet_x, bullet_y):
        collisions = pygame.sprite.groupcollide(self.bullets, walls, True, True)
        if collisions != {}:
            wp.text_map = self.return_wall_row(bullet_x, bullet_y)
            wp.collision_walls = []
            wp.world_map = set()
            for j, row in enumerate(wp.text_map):
                for i, char in enumerate(row):
                    if char == '1':
                        wp.collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
                        wp.world_map.add((i * TILE, j * TILE))

    def draw_bullets(self, walls):
        for bullet in self.bullets.sprites():
            self.bullet_collision(walls, bullet.rect[0], bullet.rect[1])
            bullet.draw_bullet()

    def return_wall_row(self, bullet_x, bullet_y, tile=60):
        print(self.x, self.y)
        row_num = int(abs(bullet_y / tile - 0.01))
        pos_num = int(abs(bullet_x / tile - 0.01))
        wp.text_map[row_num] = wp.text_map[row_num][:pos_num] + '0' + wp.text_map[row_num][pos_num + 1:]
        return wp.text_map
