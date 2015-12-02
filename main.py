import numpy as np

import grid
import images
import game
import hero
import vector
import direction

if __name__ == '__main__':
	img = images.readImage("map.jpg")
	walls_grid = grid.Grid((30,30),img)

	#grid_image = walls_grid.toImage()
	#images.plotImage(grid_image)

	walls_grid.growBorders()

	#grid_image = walls_grid.toImage()
	#images.plotImage(grid_image)

	hero_starting_position = vector.Vector((1,1))
	hero_starting_direction = direction.NORTH

	my_hero = hero.Hero(hero_starting_position,hero_starting_direction)

	my_game = game.Game(walls_grid,my_hero)

	game_image = my_game.toImage()
	images.plotImage(game_image)