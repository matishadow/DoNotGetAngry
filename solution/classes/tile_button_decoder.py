class TileButtonDecoder:
    @staticmethod
    def decode_button_name(button_name):
        parts = button_name.split('_')
        if len(parts) == 2:
            tile_index = parts[1]
            colour = None
            is_home_tile = False
            is_starting_tile = False
        elif len(parts) == 4:
            tile_index = parts[3]
            colour = parts[0]
            is_home_tile = parts[1] == 'home'
            is_starting_tile = parts[1] == 'starting'

        return tile_index, colour, is_home_tile, is_starting_tile
