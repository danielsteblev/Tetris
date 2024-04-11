import json
import random
import string
from game_logic import Figure


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
        self._game_field = [[0 for _ in range(self._board_width)] for _ in range(self._board_height)]
        characters = string.ascii_letters + string.digits
        self.__GAME_KEY = ''.join(random.choice(characters) for _ in range(10))
        print(f"The game with token={self.__GAME_KEY} was successfully created with the following settings:\n"
              f"game_field width: {self._board_width} \ngame_field height: {self._board_height}\n")

        self._score = 0
        print(self._game_field)
        self.save_game()

    @property
    def figures(self):
        return self._figures

    def save_game(self):
        game_info = {
            "field_size": {
                "width": self._board_width,
                "height": self._board_height
            },
            "token": self.__GAME_KEY,
            "field": self._game_field,
            "score": self._score
        }

        with open(f"game_sessions/{self.__GAME_KEY}.json", 'w') as file:
            json.dump(game_info, file)

            file.close()

    @property
    def width(self):
        return self._board_width

    @property
    def height(self):
        return self._board_height

    @property
    def token(self):
        return self.__GAME_KEY


