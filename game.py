import hero
import grid
import direction
import action

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

		hero_next_cell = hero_position + direction.toVector(hero_direction)

		hero_color = [1,0,0]

		if not self.walls.exists(hero_next_cell):
			hero_facing_color = [0.5,0,0]
		else:
			hero_facing_color = [0.5,0.7,0.7]

		image[hero_position.y,hero_position.x] = hero_color
		image[hero_next_cell.y,hero_next_cell.x] = hero_facing_color

		return image

	def doAction(self,action_taken):
		if action_taken not in action.ACTIONS:
			raise ValueError("Invalid action.")

		hero_next_state = self.hero.copy()
		hero_next_state.doAction(action_taken)

		hero_next_position = hero_next_state.getPosition()

		if not self.walls.exists(hero_next_position):
			self.hero = hero_next_state

	def readSensors(self):
		hero_position = self.hero.getPosition()
		hero_direction = self.hero.getDirection()

		# -------
		# Read the sensors in the hero referential
		hero_readings_referenced_hero = {}
		for direct in direction.DIRECTIONS:
			true_direction = direction.changeReferential(direct,hero_direction)

			position_to_check = hero_position + direction.toVector(true_direction)
			if self.walls.exists(position_to_check):
				hero_readings_referenced_hero[direct] = True
			else:
				hero_readings_referenced_hero[direct] = False
		# -------

		hero_readings_referenced_game = {}
		for direct in hero_readings_referenced_hero:
			true_direction = direction.changeReferential(direct,hero_direction)
			hero_readings_referenced_game[true_direction] = hero_readings_referenced_hero[direct]

		return hero_readings_referenced_game


		

