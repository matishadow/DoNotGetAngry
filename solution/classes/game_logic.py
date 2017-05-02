import random
from enum import Enum
from itertools import cycle


class Game:
    MINIMAL_NUMBER_OF_PLAYERS = 2
    ALL_COUNTERS_IN_STARTING_THROWS = 3
    NORMAL_THROWS = 1
    MAXIMUM_NUMBER_OF_DOTS = 6


    def __init__(self, number_of_players):
        if number_of_players < self.MINIMAL_NUMBER_OF_PLAYERS:
            raise Exception("You need at least two players")

        self.colors = list(Color)[:number_of_players]
        self.color_cycle = cycle(self.colors)
        self.current_color = next(self.color_cycle)
        self.players = [Player(color) for color in self.colors]

    def turn(self):
        current_player = self.players[self.current_color.value]

        if len(current_player.starting_tiles) == current_player.SPECIAL_TILES_COUNT:
            for i in range(self.ALL_COUNTERS_IN_STARTING_THROWS):
                throw = Dice.throw_the_dice()

                if throw == self.MAXIMUM_NUMBER_OF_DOTS:

        else:
            for i in range(self.NORMAL_THROWS):
                throw = Dice.throw_the_dice()


        self.current_color = next(self.color_cycle)


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3


class Counter:
    def __init__(self, color):
        self.color = color


class Player:
    SPECIAL_TILES_COUNT = 4

    def __init__(self, color):
        self.color = color
        self.starting_tiles = self.SPECIAL_TILES_COUNT * [Counter(color)]
        self.home_tiles = []


class Board:
    TILES_COUNT = 40

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.tiles = [None] * self.TILES_COUNT


class Dice:
    @staticmethod
    def throw_the_dice():
        return random.randint(1, 6)
