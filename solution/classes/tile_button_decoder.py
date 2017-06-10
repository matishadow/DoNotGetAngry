class TileButtonDecoder:
    @staticmethod
    def decode_button_name(button_name):
        parts = button_name.split('_')
        if len(parts) == 2:
            tile_index = parts[1]
            color = None
            is_home_tile = False
            is_starting_tile = False
        elif len(parts) == 4:
            tile_index = parts[3]
            color = parts[0]
            is_home_tile = parts[1] == 'home'
            is_starting_tile = parts[1] == 'starting'

        return tile_index, color, is_home_tile, is_starting_tile
