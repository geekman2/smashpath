from ..engine import Tile, Game, Player, Bet
from PIL import Image, ImageDraw
from matplotlib.pyplot import imshow 
class Cli:

    def __init__(self, size=None, players=None):
        self.players, self.game = self.make_game(size, players)

    @staticmethod
    def make_game(size=None, players=None):
        if not players:
            players = []
            num_players = input('How many players?: ')
            for i in range(int(num_players)):
                player_name = input('Player Name: ')
                player_color = input('Player Color: ')
                players.append(Player(player_name, player_color))

        if not size:
            size = input('Number of tiles per side: ')
        

        game = Game(int(size), players)
        return players,game

    def render_board(self):
        #TODO Write Docstring
        height = 2000
        width = height
        x_offset = 0
        y_offset = 0
        x_length = height/len(self.game.board)
        y_length = x_length
        board = Image.new(mode='RGB', size=(height, width), color='#ffffff')
        for row in self.game.board:
            for tile in row:
                draw = ImageDraw.Draw(board)
                draw.rectangle(((x_offset,y_offset),(x_offset+x_length,y_offset+y_length)), fill=tile.owner.color)
                x_offset += x_length
            x_offset = 0
            y_offset += y_length

        imshow(board)
    
    @staticmethod
    def _number_listify_(formatted_string):
        banned_characters = [',', '.']
        clean_string = formatted_string
        for character in banned_characters:
            clean_string = clean_string.replace(character, ' ')
        listified = clean_string.split()
        number_list =  [int(x) for x in listified]
        return number_list
    
    def _select_(self, display_iterable, select_iterable, message):
        for i, item in enumerate(display_iterable):
            print(f'{i}:{item}')
        selection = self._number_listify_(input(message))
        output = [select_iterable[x] for x in selection]
        return output

    def bet(self, player):
        wager_who = self._select_(self.game.player_names, self.game.players, 'Who would you like to bet against?: ')[0]
        wager_for = self._select_(wager_who.tile_names, wager_who.tiles, 'What do you want to wager for?: ')
        wager_with = self._select_(player.tile_names, player_tiles, 'What will you bet for it?: ')
        self.game.bet(better=player,
                      betee=wager_who,
                      bet1=wager_with,
                      bet2=wager_what)

    def buy(self, player):
        if player.tiles:
            available_tiles = []
            for player_tile in player.tiles:
                available_tiles.append(self.game.find_adjacent_tiles(player_tile))
            available_tiles = list(set(available_tiles))
            for i, tile in enumerate(available_tiles):
                print(f'{i}:{tile.name}')
            available_tile_names = [tile.name for tile in available_tiles]
            buy_order = self._select_(available_tile_names, available_tiles, 'Which tiles would you like to buy?: ')
            for tile in buy_order:
                game.buy(player, tile)
        else:
            available_tiles = self.game.tiles
            self._select_(self.available_tiles.names, self.available_tiles, 'Which tiles would you like to buy?')

    def run(self):
        while True:
            for player in self.players:
                print(f'It is now {player.name}\'s turn')
                action = input('bet, buy, or pass?: ').lower()
                if action == 'bet':
                    self.bet(player)
                elif action == 'buy':
                    self.buy(player)
                else:
                    continue
                self.render_board()
                break

if __name__ == '__main__':
	cli = Cli(10)
	cli.run()