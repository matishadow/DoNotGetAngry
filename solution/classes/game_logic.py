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

    def turn(self, user_decision_callback, user_counter_chosen_callback):
        player_index = self.current_color.value
        current_player = self.players[player_index]

        if player_has_all_counters_in_starting_position(current_player):
            for i in range(self.ALL_COUNTERS_IN_STARTING_THROWS):
                throw = Dice.throw_the_dice()

                if throw_was_maximum(throw):
                    counter_index = self.board.bring_out_counter(current_player, self.players)

                    throw = Dice.throw_the_dice()
                    if throw_was_maximum(throw):
                        counter_index = self.board.move_counter(counter_index, throw, self.players)

                        throw = Dice.throw_the_dice()
                        if throw_was_maximum(throw):
                            decision = user_decision_callback()
                            if decision == UserDecision.OUT.name:
                                self.board.bring_out_counter(current_player, self.players)
                                break
                            elif decision == UserDecision.MOVE.name:
                                self.board.move_counter(counter_index, throw, self.players)
                                break
                            else:
                                raise Exception("User input is not valid. Use 'OUT[0] or MOVE[1]'")
                        else:
                            self.board.move_counter(counter_index, throw, self.players)
                            break
                    else:
                        self.board.move_counter(counter_index, throw, self.players)
                        break

        else:
            throw_count = 0
            while True:
                throw = Dice.throw_the_dice()
                throw_count += 1

                if throw_was_maximum(throw):
                    alert = ""
                    while True:
                        decision = user_decision_callback(alert)

                        if decision == UserDecision.OUT.name:
                            decision_was_valid = self.board.bring_out_counter(current_player, self.players)
                        elif decision == UserDecision.MOVE.name:
                            decision_was_valid = self.board.move_when_out(current_player, throw,
                                                                          user_counter_chosen_callback, self.players)
                        else:
                            raise Exception("User input is not valid. Use 'OUT[0] or MOVE[1]'")

                        if decision_was_valid:
                            break
                        else:
                            alert = "You cannot do that"
                else:
                    self.board.move_when_out(current_player, throw, user_counter_chosen_callback, self.players)

                if throw_count > self.MAXIMUM_THROW_RETRIES or throw != self.MAXIMUM_NUMBER_OF_DOTS:
                    break

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
    INITIAL_STARTING_POSITION = -1

    def __init__(self, color):
        self.color = color
        self.position = self.INITIAL_STARTING_POSITION


class Player:
    SPECIAL_TILES_COUNT = 4

    def __init__(self, color):
        self.color = color
        self.starting_tiles = [Counter(color) for _ in range(self.SPECIAL_TILES_COUNT)]
        self.home_tiles = []
        self.on_board_counters = []
        self.first_index_on_board = color.value * Board.TILES_PER_PLAYER


class Board:
    TILES_COUNT = 40
    TILES_PER_PLAYER = 10

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.tiles = [None] * self.TILES_COUNT

    def move_counter(self, current_position, offset, players):
        counter = self.tiles[current_position]
        self.tiles[current_position] = None
        new_position = current_position + offset

        self.try_eliminate(players, counter, new_position)

        self.tiles[new_position] = counter
        counter.position = new_position

        return new_position

    def move_when_out(self, current_player, throw, user_counter_chosen_callback, players):
        if len(current_player.on_board_counters) == 1:
            [counter] = current_player.on_board_counters

            is_decision_valid = self.validate_user_decision(counter.position + throw, current_player)
            if not is_decision_valid:
                return False

            self.move_counter(counter.position, throw, players)
        else:
            counter_to_move_index = user_counter_chosen_callback()

            is_decision_valid = self.validate_user_decision(counter_to_move_index + throw, current_player)
            if not is_decision_valid:
                return False

            counter = self.tiles[counter_to_move_index]
            if not counter:
                raise Exception("This field is empty")
            if counter.color != current_player.color:
                raise Exception("This is not your counter!")

            self.move_counter(counter.position, throw, players)

    def check_eliminate(self, moving_color, position):
        counter_on_position = self.tiles[position]
        if counter_on_position is not None:
            if counter_on_position.color != moving_color:
                return True
            else:
                raise Exception("You cannot eliminate your own counter")
        else:
            return False

    def eliminate_counter(self, players, position):
        counter_to_eliminate = self.tiles[position]
        counter_to_eliminate.position = Counter.INITIAL_STARTING_POSITION
        self.tiles[position] = None
        player = players[counter_to_eliminate.color.value]
        player.starting_tiles.append(counter_to_eliminate)
        player.on_board_counters.remove(counter_to_eliminate)

    def try_eliminate(self, players, counter, counter_index):
        is_eliminating = self.check_eliminate(counter.color, counter_index)
        if is_eliminating:
            self.eliminate_counter(players, counter_index)

    def validate_user_decision(self, position_to_validate, current_player):
        counter_on_position = self.tiles[position_to_validate]
        if counter_on_position is not None and counter_on_position.color == current_player.color:
            return False
        else:
            return True

    def bring_out_counter(self, current_player, players):
        counter = current_player.starting_tiles.pop()
        counter_index = current_player.first_index_on_board

        is_decision_valid = self.validate_user_decision(counter_index, current_player)
        if not is_decision_valid:
            current_player.starting_tiles.append(counter)
            return False

        self.try_eliminate(players, counter, counter_index)

        counter.position = counter_index

        self.tiles[counter_index] = counter
        current_player.on_board_counters.append(counter)

        return counter_index


class Dice:
    @staticmethod
    def throw_the_dice():
        return random.randint(1, 6)
