import hero
import grid
import direction

import skimage.io as skio
import matplotlib.pyplot as plt

class Game:

	def __init__(self, walls_grid, game_hero):

		if not isinstance(walls_grid,grid.Grid):
			raise ValueError("Invalid type for game grid.")
		if not isinstance(game_hero,hero.Hero):
			raise ValueError("Invalid type for game hero.")

		if not game_hero.isInRange(0,walls_grid.shape[0],0,walls_grid.shape[1]):
			raise ValueError("Game hero out of the bounds of the grid.")

		self.hero = game_hero
		self.walls = walls_grid

	def toImage(self):
		image = self.walls.toImage()

		hero_position = self.hero.getPosition()
		hero_direction = self.hero.getDirection()

		hero_color = [0,0,0]
		if hero_direction == direction.NORTH:
			hero_color = [1,0,0]
		elif hero_direction == direction.EAST:
			hero_color = [0,1,0]
		elif hero_direction == direction.SOUTH:
			hero_color = [0,0,1]
		elif hero_direction == direction.WEST:
			hero_color = [1,0,1]
		image[hero_position.y,hero_position.x] = hero_color

		return image
		

