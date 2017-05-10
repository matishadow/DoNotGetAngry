from classes.dice import Dice


class Counter:
    INITIAL_STARTING_POSITION = -1

    def __init__(self, color):
        self.color = color
        self.position = self.INITIAL_STARTING_POSITION
        self.in_on_home_tile = False

    def is_close_to_home(self, player):
        is_before_his_home = self.position <= player.last_index_on_board
        is_max_throw_before = self.position > (player.last_index_on_board - Dice.MAXIMUM_NUMBER_OF_DOTS)

        return is_before_his_home and is_max_throw_before
