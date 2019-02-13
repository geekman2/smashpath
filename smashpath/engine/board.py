from .tile import Tile
import yaml


class Board:

	def __init__(self, size):
		with open('config/tile_names.yaml') as f:
			self.tile_names = yaml.load(f)
		self.board = []
		self.tiles = {}
        for y in range(size):
        	row = []
        	for x in range(size):
        		tile_name = self.tile_names.pop(0)
        		new_tile = Tile((x, y), tile_name)
        		row.append(new_tile)
        		self.tiles[tile_name] = new_tile
            self.board.append(row)

    
