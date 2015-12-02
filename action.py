class Action:
	FOWARD_VALUE = 0
	BACKWARD_VALUE = 1
	LEFT_VALUE = 2
	RIGHT_VALUE = 3
	ACTIONS_VALUES = [FOWARD_VALUE,BACKWARD_VALUE,LEFT_VALUE,RIGHT_VALUE]

	def __init__(self, action = FOWARD_VALUE):
		if not action in self.ACTIONS_VALUES:
			raise ValueError("The initial action is not a valid action.")

		self.action = action

FOWARD = Action(Action.FOWARD_VALUE)
BACKWARD = Action(Action.BACKWARD_VALUE)
LEFT = Action(Action.LEFT_VALUE)
RIGHT = Action(Action.RIGHT_VALUE)

ACTIONS = [FOWARD,BACKWARD,LEFT,RIGHT]