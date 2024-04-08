import json

import pygame

from game_logic.Game import Game


class MainWindow:
    def __init__(self, settings_file: str, window_name: str, icon: str):
        with open(settings_file) as file:
            settings = json.load(file)

        W = settings['field_size']['width']
        H = settings['field_size']['height']
        TILE = settings['field_size']['tile']

        pygame.init()
        GAME_RES = W * TILE, H * TILE
        self.sc = pygame.display.set_mode(GAME_RES)
        pygame.display.set_caption(window_name)
        pygame.display.set_icon(pygame.image.load(icon))

    def start_game(self):
        clock = pygame.time.Clock()
        isRunning = True

        grid = [pygame.Rect(x * self.TILE, y * App.TILE, App.TILE, App.TILE) for x in range(App.W) for y in range(App.H)]
        game = Game()

