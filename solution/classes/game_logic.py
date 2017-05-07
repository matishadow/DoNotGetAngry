import random
from enum import Enum
from itertools import cycle


def player_has_all_counters_in_starting_position(player):
    return len(player.starting_tiles) == player.SPECIAL_TILES_COUNT


def throw_was_maximum(throw):
    return throw == Game.MAXIMUM_NUMBER_OF_DOTS


class Game:
    MINIMAL_NUMBER_OF_PLAYERS = 2
    ALL_COUNTERS_IN_STARTING_THROWS = 3
    MAXIMUM_NUMBER_OF_DOTS = 6
    NORMAL_THROWS = 1
    MAXIMUM_THROW_RETRIES = 3

    def __init__(self, number_of_players):
        if number_of_players < self.MINIMAL_NUMBER_OF_PLAYERS:
            raise Exception("You need at least two players")

        self.colors = list(Color)[:number_of_players]
        self.color_cycle = cycle(self.colors)
        self.current_color = next(self.color_cycle)
        self.players = [Player(color) for color in self.colors]
        self.board = Board(number_of_players)

    def turn(self, user_decision_callback):
        player_index = self.current_color.value
        current_player = self.players[player_index]

        if player_has_all_counters_in_starting_position(current_player):
            for i in range(self.ALL_COUNTERS_IN_STARTING_THROWS):
                throw = Dice.throw_the_dice()

                if throw_was_maximum(throw):
                    counter_index = self.board.bring_out_counter(current_player, player_index)

                    throw = Dice.throw_the_dice()
                    if throw_was_maximum(throw):
                        counter_index = self.board.move_counter(counter_index, throw)

                        throw = Dice.throw_the_dice()
                        if throw_was_maximum(throw):
                            decision = user_decision_callback()
                            if decision == UserDecision.OUT.name:
                                self.board.bring_out_counter(current_player, player_index)
                                break

                            elif decision == UserDecision.MOVE.name:
                                self.board.move_counter(counter_index, throw)
                                break
                            else:
                                raise Exception("User input is not valid. Use 'OUT[0] or MOVE[1]'")
                        else:
                            self.board.move_counter(counter_index, throw)
                            break
                    else:
                        self.board.move_counter(counter_index, throw)
                        break

        else:
            for i in range(self.NORMAL_THROWS):
                throw = Dice.throw_the_dice()

        self.current_color = next(self.color_cycle)


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3


class UserDecision(Enum):
    OUT = 0
    MOVE = 1


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
    TILES_PER_PLAYER = 10

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.tiles = [None] * self.TILES_COUNT

    def move_counter(self, current_position, offset):
        counter = self.tiles[current_position]
        self.tiles[current_position] = None
        new_position = current_position + offset
        self.tiles[new_position] = counter

        return new_position

    def bring_out_counter(self, player, player_index):
        counter = player.starting_tiles.pop()
        counter_index = player_index * self.TILES_PER_PLAYER
        self.tiles[counter_index] = counter

        return counter_index


class Dice:
    @staticmethod
    def throw_the_dice():
        return random.randint(1, 6)
