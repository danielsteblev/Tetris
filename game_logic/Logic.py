import random

from game_logic.Game import Game


class Logic:
    @staticmethod
    def generate_cur_figures(game: Game):
        random.shuffle(game.figures)
        cur_figures = [game.figures[0], game.figures[1], game.figures[2]]
        return cur_figures

    @staticmethod
    def start_game(game: Game):
        cur_figures = Logic.generate_cur_figures(game)  # массив из 3 фигур которые будем таскать
