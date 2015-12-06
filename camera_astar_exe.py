import images
import offline_deterministic_know_planner
import matplotlib.pyplot as plt
import zumy_interface

def run(game,timestep_in_seconds=0.001,show_results=True):

	actions = offline_deterministic_know_planner.solveAStar(game)
	print actions

	if show_results:
		game_image = game.toImage()
		images.plotImage(game_image,False)

	recalculate_route = True

	while(recalculate_route):
		recalculate_route = False

		for action in actions:
			if game.canDoAction(action):
				game.doAction(action)

				zumy_cam_pos = zumy_interface.getZumyPositionCamera(game)
				zumy_brain_pos = game.getHero().getPosition()

				if zumy_cam_pos != zumy_brain_pos:
					game.setHeroPosition(zumy_cam_pos)

					if show_results:
						game_image = game.toImage()
						images.updateLastPlot(game_image)

					recalculate_route = True

				sensor_readings = game.readSensors()
				game.ackSensor(sensor_readings)

				if show_results:
					print sensor_readings
					game_image = game.toImage()
					images.updateLastPlot(game_image)
			else:
				recalculate_route = True

			if recalculate_route:
				actions = offline_deterministic_know_planner.solveAStar(game)
				print actions
				break

			plt.pause(timestep_in_seconds)

	return game
	