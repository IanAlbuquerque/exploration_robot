import vector
import math
import game
import action
import hero
import direction

import time

import heapq

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
		goal_position = game_to_solve.getGoalPosition()
		return manhattanDistance(hero_state.getPosition(),goal_position)

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
			dist = functionToMinimize(game_to_solve,next_hero_state)
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

def solveAStar(game_to_solve):
	if not isinstance(game_to_solve,game.Game):
		raise ValueError("Variable is not a Game.")

	def heuristic(game_to_solve,hero_state):
		goal_position = game_to_solve.getGoalPosition()
		return manhattanDistance(hero_state.getPosition(),goal_position)

	goal_position = game_to_solve.getGoalPosition()
	hero_start_state = game_to_solve.getHero().copy()

	heap = [(heuristic(game_to_solve,hero_start_state),hero_start_state,None,None)]
	visited = []
	recover_map = {}

	while True:
		#print "----"
		#print heap
		#print visited
		v = heapq.heappop(heap)
		while v[1].toTuple() in visited:
			if len(heap) == 0:
				return []
			v = heapq.heappop(heap)
		visited.append(v[1].toTuple())
		recover_map[v[1].toTuple()] = (v[2], v[3])

		#print v[1].toTuple()

		if goal_position == v[1].getPosition():
			recover_map[hero_start_state.toTuple()] = None
			actions = []

			state_tuple = v[1].toTuple()
			recover = recover_map[state_tuple]
			while recover != None:
				#time.sleep(1)
				#print "a"
				actions.append(recover[0])
				new_state = recover[1]
				state_tuple = new_state.toTuple()
				#print state_tuple
				recover = recover_map[state_tuple]
			actions.reverse()
			return actions

		#print "Actions-----------------------"

		actions_possible = action.ACTIONS
		for act in actions_possible:
			c = game_to_solve.transitionModel(v[1], act)
			#print c.toTuple()
			cost = 1	   
			heapq.heappush(heap, (v[0] + cost + heuristic(game_to_solve,c) - heuristic(game_to_solve,v[1]), c, act, v[1]))


