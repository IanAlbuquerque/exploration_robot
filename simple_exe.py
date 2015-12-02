import time
import images

def doActions(game,actions,timestep_in_seconds=0.001,show_results=True):

	if show_results:
		game_image = game.toImage()
		images.plotImage(game_image,False)

	for action in actions:
		game.doAction(action)

		if show_results:
			print game.readSensors()
			game_image = game.toImage()
			images.plotImage(game_image,False)

		time.sleep(timestep_in_seconds)

	return game