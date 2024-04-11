import random

from game_logic.GameTetris import GameTetris


class Logic:
    @staticmethod
    def generate_cur_figures(game: GameTetris):
        random.shuffle(game.figures)
        cur_figures = [game.figures[0], game.figures[1], game.figures[2]]
        return cur_figures


    @staticmethod
    def check_lines(game: GameTetris):
        for i in range(len(game.board)):
            # Проверка линии по горизонтали
            if all(elem == 1 for elem in game.board[i]):
                game.board[i] = [0] * len(game.board[i])
                print("+10")
                game.score += 10

            # Проверка линии по вертикали
            column = [row[i] for row in game.board]
            if all(elem == 1 for elem in column):
                for j in range(len(game.board)):
                    game.board[j][i] = 0

                print('yes')
                game.score += 10


