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

		hero_next_cell = hero_position + hero_direction.toVector()
		#print (hero_next_cell.x, hero_next_cell.y)

		hero_color = [1,0,0]

		if not self.walls.exists(hero_next_cell):
			hero_facing_color = [0.5,0,0]
		else:
			hero_facing_color = [0.5,0.7,0.7]

		image[hero_position.y,hero_position.x] = hero_color
		image[hero_next_cell.y,hero_next_cell.x] = hero_facing_color

		return image

	def doAction(self,action):
		self.hero.doAction(action)
		

