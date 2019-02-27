class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.tiles = {}

    def add_tile(self, tile):
        self.tiles[tile.name] = tile

    def remove_tile(self, tile):
        self.tiles.pop(tile.name, None)
