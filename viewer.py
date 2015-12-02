import time
import images

def viewActions(game,actions,timestep_in_seconds):

	game_image = game.toImage()
	images.plotImage(game_image,False)

	for action in actions:
		game.doAction(action)
		game_image = game.toImage()
		images.plotImage(game_image,False)
		time.sleep(timestep_in_seconds)

	return game