import hero
import grid

class Game:

	def __init__(self, game_grid, game_hero):

		if type(game_grid) != grid.Grid:
			raise ValueError("Invalid type for game grid.")
		if type(game_hero) != hero.Hero:
			raise ValueError("Invalid type for game hero.")

		if not game_hero.isInRange(0,game_grid.shape[0],0,game_grid.shape[1]):
			raise ValueError("Game hero out of the bounds of the grid.")

		self.hero = game_hero

