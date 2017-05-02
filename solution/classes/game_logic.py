import random
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


class Counter:
    def __init__(self, color):
        self.color = color


class Player:
    SPECIAL_TILES_COUNT = 4

    def __init__(self, color):
        self.color = color
        self.starting_tiles = self.SPECIAL_TILES_COUNT * [None]
        self.home_tiles = self.SPECIAL_TILES_COUNT * [None]


class Board:
    TILES_COUNT = 40

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.tiles = [None] * self.TILES_COUNT


class Dice:
    @staticmethod
    def throw_the_dice():
        return random.randint(1, 6)
