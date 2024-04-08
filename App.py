import pygame
import json

with open('config_file/settings.json') as file:
    settings = json.load(file)

W = settings['field_size']['width']
H = settings['field_size']['height']
TILE = 40
GAME_RES = W * TILE, H * TILE
FPS = 30

pygame.init()
sc = pygame.display.set_mode(GAME_RES)
pygame.display.set_caption("Тетрис 0.0.1")
pygame.display.set_icon(pygame.image.load("images/icon.png"))
