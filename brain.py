import numpy as np

import grid
import images
import game
import hero
import vector
import direction
import simple_exe
import action
import offline_deterministic_know_planner
import astar_recalc_exe
import camera_astar_exe

MAP_FILE_NAME = "maps/map.jpg"

def createGame():
	img = images.readImage(MAP_FILE_NAME)
	MAZE_SIZE_Y = 30
	MAZE_SIZE_X = 30

	walls_grid = grid.Grid((MAZE_SIZE_Y,MAZE_SIZE_X),img)
	known_grid = grid.Grid(walls_grid.shape)

	walls_grid.growBorders()
	known_grid.growBorders()

	hero_starting_position = vector.Vector((1,1))
	hero_starting_direction = direction.SOUTH
	goal_position = vector.Vector((MAZE_SIZE_Y,MAZE_SIZE_X))

	my_hero = hero.Hero(hero_starting_position,hero_starting_direction)

	my_game = game.Game(walls_grid,my_hero,goal_position,known_grid)

	return my_game

def solveGame(game_to_solve):
	game_image = game_to_solve.toImage()
	images.plotImage(game_image,True)

	#astar_recalc_exe.run(game_to_solve,0.01,True)
	camera_astar_exe.run(game_to_solve,0.01,True)

	game_image = game_to_solve.toImage()
	images.plotImage(game_image,True)

if __name__ == '__main__':
	my_game = createGame()
	solveGame(my_game)


