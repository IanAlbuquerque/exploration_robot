import numpy as np

import grid
import images
import game
import hero
import vector
import direction
import viewer
import action

F, B, L, R = action.FOWARD, action.BACKWARD, action.LEFT, action.RIGHT

if __name__ == '__main__':
	img = images.readImage("map.jpg")
	walls_grid = grid.Grid((30,30),img)

	#grid_image = walls_grid.toImage()
	#images.plotImage(grid_image,True)

	walls_grid.growBorders()

	#grid_image = walls_grid.toImage()
	#images.plotImage(grid_image,True)

	hero_starting_position = vector.Vector((1,1))
	hero_starting_direction = direction.NORTH

	my_hero = hero.Hero(hero_starting_position,hero_starting_direction)

	my_game = game.Game(walls_grid,my_hero)

	game_image = my_game.toImage()
	images.plotImage(game_image,True)

	actions = [R,F,R,F,R,F,R,F,R,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,R,F,F,F,F,F,F,F,F,F,F,L,L,F,F,F,B,B,B,L,F,F,F,F,F,F,F,F,F,F,F]
	viewer.viewActions(my_game,actions,0.2)

	game_image = my_game.toImage()
	images.plotImage(game_image,True)

