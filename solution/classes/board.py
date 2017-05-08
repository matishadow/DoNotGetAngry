from classes.counter import Counter


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
