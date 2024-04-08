import typing

from game_logic.Block import Block


class Figure:
    def __init__(self, name: str, shape: list[Block]):
        self.__name = name
        self.__shape = shape

    @property
    def name(self):
        return self.__name

    @property
    def shape(self):
        return self.__shape

    def __str__(self) -> str:
        return f"Название {self.__name}, координаты блоков: {[str(self.__shape[i]) for i in range(len(self.__shape))]}"



