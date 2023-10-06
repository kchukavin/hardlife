#!/usr/bin/env python3

import pygame

import modules.constants as constants
import modules.direction as direction
from modules.field import Field
from modules.generator import Generator
from modules.player import Player
from modules.sprite import Sprite

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(
    (constants.FIELD_WIDTH * constants.CELL_WIDTH, constants.FIELD_HEIGHT * constants.CELL_HEIGHT))
pygame.display.set_caption("Hard life")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

field = Field()
generator = Generator(field)
generator.generate_walls(100)
generator.generate_food(50)
generator.generate_creatures(20)
player = Player(field, 0, 0, constants.BLUE)
field.add_object(player)

objects = field.get_objects()

sprites = []
for object in objects:
    all_sprites.add(Sprite(object))

last_turn_time = pygame.time.get_ticks()

# Цикл игры
player_direction = direction.DIRECTION_NONE
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(constants.FPS)
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
    if current_time - last_turn_time > 1000 / constants.TPS:
        last_turn_time = current_time
        for object in objects:
            object.make_move()

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(constants.BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
