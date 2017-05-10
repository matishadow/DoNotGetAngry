from itertools import cycle

from classes.board import Board
from classes.enums import *
from classes.player import Player
from classes.dice import Dice


class Game:
    MINIMAL_NUMBER_OF_PLAYERS = 2
    ALL_COUNTERS_IN_STARTING_THROWS = 3
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

        if current_player.has_all_counters_in_starting_position():
            for i in range(self.ALL_COUNTERS_IN_STARTING_THROWS):
                throw = Dice.throw_the_dice()

                if Dice.throw_was_maximum(throw):
                    counter_index = self.board.bring_out_counter(current_player, self.players)

                    throw = Dice.throw_the_dice()
                    if Dice.throw_was_maximum(throw):
                        counter_index = self.board.move_counter(counter_index, throw, self.players)

                        throw = Dice.throw_the_dice()
                        if Dice.throw_was_maximum(throw):
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

                can_decision_be_valid = self.board.can_decision_be_valid(current_player, throw)
                if not can_decision_be_valid:
                    break
                if Dice.throw_was_maximum(throw):
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

                if throw_count > self.MAXIMUM_THROW_RETRIES or throw != Dice.MAXIMUM_NUMBER_OF_DOTS:
                    break

        self.current_color = next(self.color_cycle)

