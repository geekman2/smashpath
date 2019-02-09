from .tile import Tile
from .player import Player
from .bet import Bet
from matplotlib.pyplot import imshow 
from PIL import Image, ImageDraw, ImageColor
import random
class Game:
    #TODO Write docstring
    
    def __init__(self, size, players):
        #TODO Write Docstring
        self.board = self.__generate_board__(size)
        self.players = players
        self.player_names = [player.name for player in self.players]
        self.game_player = Player('Game', 'grey')
        self.players.append(self.game_player)
        for row in self.board:
            for tile in row:
                tile.sell(self.game_player)
    
    def __generate_board__(self, size):
        #TODO Write Docstring
        #We use a for loop instead of a nested list comprehension here
        #for clarity
        board = []
        for y in range(size):
            row = [Tile(x, y) for x in range(size)]
            board.append(row)
        return board
    
    @staticmethod
    def bet(better, betee, bet1, bet2):
        bet = Bet(better, betee, bet1, bet2)
        bet.run()
    
    def find_adjacent_tiles(self, tile):
        x_position = tile.x_position
        y_position = tile.y_position
        left = self.board[y_position][x_position-1]
        right = self.board[y_position][x_position+1]
        above = self.board[y_position+1][x_position]
        below = self.board[y_position-1][x_position]
        adjacent_tiles = [left, right, above, below]
        return adjacent_tiles
    
    def find_diagonal_tiles(self, tile):
        x_position = tile.x_position
        y_position = tile.y_position
        left_above = self.board[y_position+1][x_position-1]
        right_above = self.board[y_position+1][x_position+1]
        left_below = self.board[y_position-1][x_position-1]
        right_below = self.board[y_position-1][x_position+1]
        diagonal_tiles = [left_above, right_above, left_below, right_below]
        return diagonal_tiles
        
        
        
    def buy(player, tile):
        for adjacent_tile in find_adjacent_tiles(tile):
            if adjacent_tile.owner == player or not player.tiles: 
                tile.change_hands(player)
            else:
                print(f'{player.name} owns at least one tile and none are adjacent to the selected tile')
    
    def sell():
        tile.sell()
    
    