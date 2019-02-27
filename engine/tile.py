class Tile:
    # TODO Write Docstring

    def __init__(self, position, name='Unnamed', initial_value=100):
        # TODO Write docstring
        self.name = name
        self.value = initial_value
        self.owner = None
        self.position = position

    def change_hands(self, new_owner):
        # TODO Write docstring
        self.owner.remove_tile(self)
        new_owner.add_tile(self)
        self.value *= 2
        self.owner = new_owner
        print(f'{self.name} now belongs to {self.owner.name} and has a value of ${self.value}')

    @property
    def adjacent_tile_coordinates(self):
        x, y = self.position
        left = (y, x-1)
        right = (y, x+1)
        above = (y+1, x)
        below = (y-1, x)
        adjacent_tiles = [left, right, above, below]
        return adjacent_tiles

    @property
    def diagonal_tile_coordinates(self):
        x, y = self.position
        left_above = (y + 1, x - 1)
        right_above = (y + 1, x + 1)
        left_below = (y-1, x - 1)
        right_below = (y-1, x+1)
        diagonal_tiles = [left_above, right_above, left_below, right_below]
        return diagonal_tiles
