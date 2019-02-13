from . import Tile, Player, GamePlayer
import mock

@pytest.fixture
def game_player():
	return GamePlayer()

@pytest.fixture
def tile():
	return Tile(5, 5, 'Test Tile')

@mock.patch('tile.Tile')
def test_sell_owner_paid(tile):
	tile.sell()