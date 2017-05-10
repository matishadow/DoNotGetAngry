from classes.counter import Counter


def is_position_beyond_home(current_position, throw, player, is_home_tile):
    new_position = current_position + throw
    if is_home_tile:
        return new_position > (player.SPECIAL_TILES_COUNT - 1);
    else:
        return new_position > player.last_index_with_home


class Board:
    TILES_COUNT = 40
    TILES_PER_PLAYER = 10

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.tiles = [None] * self.TILES_COUNT

    def move_counter(self, counter, offset, players, is_home_tile=False):
        current_position = counter.position
        current_player = players[counter.color.value]
        if is_home_tile:
            counter_collection = current_player.home_tiles
        else:
            counter_collection = self.tiles

        counter = counter_collection[current_position]
        counter_collection[current_position] = None
        new_position = current_position + offset
        counter_collection[new_position] = counter
        counter.position = new_position

        if not is_home_tile:
            self.try_eliminate(players, counter, new_position)

        return new_position

    def move_when_out(self, current_player, throw, user_counter_chosen_callback, players):
        if len(current_player.on_board_counters) == 1:
            [counter] = current_player.on_board_counters

            is_decision_valid = self.validate_user_decision(counter.position, throw, current_player)
            if not is_decision_valid:
                return False

            self.move_counter(counter, throw, players)
        else:
            counter_to_move_index, is_home_tile = user_counter_chosen_callback()

            is_decision_valid = self.validate_user_decision(counter_to_move_index, throw, current_player)
            if not is_decision_valid:
                return False

            if is_home_tile:
                counter = current_player.home_tiles[counter_to_move_index]
            else:
                counter = self.tiles[counter_to_move_index]

            if not counter:
                raise Exception("This field is empty")
            if counter.color != current_player.color:
                raise Exception("This is not your counter!")

            self.move_counter(counter, throw, players, is_home_tile)

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

    def validate_user_decision(self, current_position, throw, current_player, is_home_tile=False):
        if is_home_tile:
            counter_collection = current_player.home_tiles
        else:
            counter_collection = self.tiles

        position_to_validate = current_position + throw
        current_counter = counter_collection[current_position]

        if current_counter.is_close_to_home(current_player) and \
                is_position_beyond_home(current_position, throw, current_player):
            return False

        counter_on_desired_position = counter_collection[position_to_validate]
        if counter_on_desired_position is not None \
                and counter_on_desired_position.color == current_player.color:
            return False
        else:
            return True

    def bring_out_counter(self, current_player, players):
        counter = current_player.starting_tiles.pop()
        counter_index = current_player.first_index_on_board

        is_decision_valid = self.validate_user_decision(counter_index, 0, current_player)
        if not is_decision_valid:
            current_player.starting_tiles.append(counter)
            return False

        self.try_eliminate(players, counter, counter_index)

        counter.position = counter_index

        self.tiles[counter_index] = counter
        current_player.on_board_counters.append(counter)

        return counter_index
