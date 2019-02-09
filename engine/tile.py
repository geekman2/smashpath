from . import *
class Tile:
    #TODO Write Docstring
    
    def __init__(self,x_position, y_position, name='Unnamed',initial_value=100):
        #TODO Write docstring
        self.name = name
        self.value = initial_value
        self.owner = None
        
    def change_hands(self, new_owner):
        #TODO Write docstring
        self.owner.remove_tile(self)
        new_owner.add_tile(self)
        self.value *= 2
        self.owner = new_owner
        print(f'{self.name} now belongs to {self.owner} and has a value of ${self.value}')
        
    def sell(self, game_player):
        if self.owner:
            self.owner.pay(self.value)
        self.owner =  game_player
        game_player.add_tile(self)
        self.value /= 2
        #print(f'{self.name} now belongs to {self.owner} and has a value of ${self.value}')