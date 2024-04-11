import json
import random
import string
import time
from datetime import date

from game_logic import Figure
from gui import GameSessionWindow


class Game:

    def __init__(self, settings_file):
        with open(settings_file) as file:
            settings = json.load(file)
        self._board_width = settings['field_size']['width']
        self._board_height = settings['field_size']['height']
        self._figures = [Figure.ShapeT, Figure.ShapeLine,
                         Figure.ShapeReverseG, Figure.ShapeSquare,
                         Figure.ShapeT, Figure.ShapeZ,
                         Figure.ShapeReverseZ]


        if not 'field' in settings:
            self._game_field = [[0 for _ in range(self._board_width)] for _ in range(self._board_height)]
        else:
            self._game_field = settings['field']

        if not 'token' in settings:
            characters = string.ascii_letters + string.digits
            self.__GAME_KEY = ''.join(random.choice(characters) for _ in range(10))
        else:
            self.__GAME_KEY = settings["token"]

        print(f"The game with token={self.__GAME_KEY} was successfully created with the following settings:\n"
              f"game_field width: {self._board_width} \ngame_field height: {self._board_height}\n")

        if not 'score' in settings:
            self._score = 0
        else:
            self._score = settings['score']

        print(self._game_field)

    @property
    def figures(self):
        return self._figures

    def save_game(self):
        from datetime import datetime
        game_info = {
            "field_size": {
                "width": self._board_width,
                "height": self._board_height
            },
            "token": self.__GAME_KEY,
            "field": self._game_field,
            "score": self._score,
            "date": datetime.now().isoformat()
        }

        with open(f"game_sessions/{self.__GAME_KEY}.json", 'w') as file:
            json.dump(game_info, file)
            file.close()

        print("Игра успешно сохранена!")

    @property
    def width(self):
        return self._board_width

    @property
    def height(self):
        return self._board_height

    @property
    def token(self):
        return self.__GAME_KEY

    @property
    def board(self):
        return self._game_field

    @property
    def score(self):
        return self._score
