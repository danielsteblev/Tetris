import json
import random
import string


from game_logic.Block import Block
from game_logic.Figure import Figure


class Game:
    def __init__(self, settings_file):
        with open(settings_file) as file:
            settings = json.load(file)

        figures = []  # список с координатами кубов фигур
        for figure_data in settings['figures']:
            figure = Figure(figure_data['name'], [Block(block['x'], block['y']) for block in figure_data['shape']])
            figures.append(figure)

        W = settings['field_size']['width']
        H = settings['field_size']['height']

        game_field = [[(0) for _ in range(W)] for _ in range(H)]

        characters = string.ascii_letters + string.digits
        self.__GAME_KEY = ''.join(random.choice(characters) for _ in range(10))

        print(f"The game with token={self.__GAME_KEY} was successfully created with the following settings:\n"
              f"game_field width: {W} \ngame_field height: {H}\n"
              f"input_figures: {[str(figure) for figure in figures]}")
