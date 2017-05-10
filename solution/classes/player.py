from classes.counter import Counter
from classes.board import Board


class Player:
    SPECIAL_TILES_COUNT = 4

    def __init__(self, color):
        self.color = color
        self.starting_tiles = [Counter(color) for _ in range(self.SPECIAL_TILES_COUNT)]
        self.home_tiles = [None] * self.SPECIAL_TILES_COUNT
        self.on_board_counters = []
        self.first_index_on_board = color.value * Board.TILES_PER_PLAYER
        self.last_index_on_board = (self.first_index_on_board + (Board.TILES_COUNT - 1)) % Board.TILES_COUNT
        self.last_index_with_home = self.last_index_on_board + self.SPECIAL_TILES_COUNT

    def has_all_counters_in_starting_position(self):
        return len(self.starting_tiles) == self.SPECIAL_TILES_COUNT

    def has_won(self):
        not_none_count = sum(counter is not None for counter in self.home_tiles)
        return not_none_count == self.SPECIAL_TILES_COUNT
