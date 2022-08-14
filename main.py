import sys

import pygame


WIDTH = 500
HEIGHT = 500
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

tank_surf = pygame.image.load('images/tank.png').convert()
tank_rect = tank_surf.get_rect(center=(WIDTH//2, HEIGHT//2))

tank_up = tank_surf
tank_down = pygame.transform.flip(tank_surf, 0, 1)
tank_left = pygame.transform.rotate(tank_surf, 90)
tank_right = pygame.transform.rotate(tank_surf, -90)

tank_surf = pygame.transform.scale(tank_surf, (tank_surf.get_width()*2, tank_surf.get_height()*2))

tank = tank_up
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tank = tank_left
        tank_rect.x -= speed
        if tank_rect.x < 0:
            tank_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        tank = tank_right
        tank_rect.x += speed
        if tank_rect.x > WIDTH-tank_rect.height:
            tank_rect.x = WIDTH-tank_rect.height
    elif keys[pygame.K_UP]:
        tank = tank_up
        tank_rect.y -= speed
        if tank_rect.y < 0:
            tank_rect.y = 0
    elif keys[pygame.K_DOWN]:
        tank = tank_down
        tank_rect.y += speed
        if tank_rect.y > HEIGHT-tank_rect.height:
            tank_rect.y = HEIGHT-tank_rect.height

    screen.fill((0, 0, 0))
    screen.blit(tank, tank_rect)

    pygame.display.update()

    clock.tick(FPS)
