class Player:
    
    def __init__(self, name, color, starting_money=500):
        self.name = name
        self.color = color
        self.tiles = []
        self.tile_names = [tile.name for tile in self.tiles]
        self.money = starting_money
    
    def add_tile(self, tile):
        self.tiles.append(tile)
    
    def remove_tile(self, tile):
        self.tiles.remove(tile)
    
    def pay(self, amount):
        self.money += amount

    def deduct(self, amount):
        self.money -= amount


class GamePlayer(Player):

    def __init__(self):
        super().__init__()
        self.name = 'Game'
        self.color = 'grey'
        self.money = 1e25
