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

                print('+10')
                game.score += 10

    @staticmethod
    def can_drag_fugire(figure, cell_x, cell_y, board):
        for i in range(len(figure.shape)):
            for j in range(len(figure.shape[0])):
                if figure.shape[i][j] == board[i + cell_x][j + cell_y] == 1:
                    return False

        return True

