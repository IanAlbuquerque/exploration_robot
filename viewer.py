import time
import images

def view_actions(game,actions,timestep):

	game_image = game.toImage()
	images.plotImage(game_image)

	for action in actions:
		game.doAction(action)
		game_image = game.toImage()
		images.plotImage(game_image)
		time.sleep(timestep)

	return game