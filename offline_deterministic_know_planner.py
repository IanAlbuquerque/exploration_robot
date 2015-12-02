import vector
import math
import game
import action

def manhattanDistance(p,q):
	if not isinstance(p,vector.Vector):
		raise ValueError("Variable is not a Vector.")
	if not isinstance(q,vector.Vector):
		raise ValueError("Variable is not a Vector.")

	return math.fabs(p.x - q.x) + math.fabs(p.y - q.y)

def solveGameGradientDescending(game_to_solve,max_steps = 1000):
	if not isinstance(game_to_solve,game.Game):
		raise ValueError("Variable is not a Game.")

	def functionToMinimize(game_to_solve,hero_state):
		return manhattanDistance(next_hero_state.getPosition(),goal_position) + manhattanDistance(game_to_solve.transitionModel(game_to_solve.transitionModel(hero_state,act),action.FOWARD).getPosition(),goal_position)

	goal_position = game_to_solve.getGoalPosition()
	hero_state = game_to_solve.getHero().copy()

	actions_to_take = []

	steps = 0
	while True:
		steps += 1

		min_dist = float("inf")
		best_action = None
		for act in action.ACTIONS:
			next_hero_state = game_to_solve.transitionModel(hero_state,act)
			dist = functionToMinimize(game_to_solve,hero_state)
			if dist < min_dist:
				min_dist = dist
				best_action = act

		hero_state = game_to_solve.transitionModel(hero_state,best_action)
		actions_to_take.append(best_action)

		print "--"
		print goal_position.toTuple()
		print hero_state.getPosition().toTuple()

		if goal_position == hero_state.getPosition() or steps > max_steps:
			break

	return actions_to_take
