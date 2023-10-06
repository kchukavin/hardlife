#!/usr/bin/env python3

import pygame

from modules.constants import *
import modules.direction as direction
from modules.field import Field
from modules.generator import Generator
from modules.player import Player
from modules.sprite import Sprite

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(
    (FIELD_WIDTH * CELL_WIDTH, FIELD_HEIGHT * CELL_HEIGHT))
pygame.display.set_caption("Hard life")
clock = pygame.time.Clock()

field = Field()
generator = Generator(field)
generator.generate_walls(100)
generator.generate_food(50)
generator.generate_creatures(20)
player = Player(field, 0, 0, BLUE)
field.add_object(player)

all_sprites = pygame.sprite.Group()
for object in field.get_objects():
    all_sprites.add(Sprite(object))

last_turn_time = pygame.time.get_ticks()

# Цикл игры
player_direction = direction.DIRECTION_NONE
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():

        match event.type:
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        player_direction = direction.DIRECTION_UP
                    case pygame.K_RIGHT:
                        player_direction = direction.DIRECTION_RIGHT
                    case pygame.K_DOWN:
                        player_direction = direction.DIRECTION_DOWN
                    case pygame.K_LEFT:
                        player_direction = direction.DIRECTION_LEFT
                    case pygame.K_ESCAPE:
                        running = False

                player.want_to_move_to(player_direction)

            case pygame.KEYUP:
                if (event.key == pygame.K_UP and player_direction == direction.DIRECTION_UP
                        or event.key == pygame.K_RIGHT and player_direction == direction.DIRECTION_RIGHT
                        or event.key == pygame.K_DOWN and player_direction == direction.DIRECTION_DOWN
                        or event.key == pygame.K_LEFT and player_direction == direction.DIRECTION_LEFT):
                    player_direction = direction.DIRECTION_NONE

            case pygame.QUIT:
                running = False

        player.want_to_move_to(player_direction)

    current_time = pygame.time.get_ticks()
    if current_time - last_turn_time > 1000 / TPS:
        for object in field.get_objects():
            object.make_move()

        all_sprites.empty()
        for object in field.get_objects():
            all_sprites.add(Sprite(object))

        last_turn_time = current_time

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
