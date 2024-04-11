from game_logic.GameTetris import GameTetris
from game_logic.Logic import Logic


class Test:
    @staticmethod
    def test_lines_func():
        game = GameTetris("C:\\Users\\HUAWEI\\Tetris\\config_file\\test.json")
        for i in range(0, len(game.board)):
            for j in range(0, len(game.board[i])):
                game.board[0][j] = 1
                game.board[i][0] = 1

        print("after:")
        print(game.board)
        Logic.check_lines(game)
        print(game.board)
        print(game.score)


def main():
    Test.test_lines_func()


if __name__ == '__main__':
    main()
