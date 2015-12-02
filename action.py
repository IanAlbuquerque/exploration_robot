class Action:
	FOWARD = 0
	BACKWARD = 1
	LEFT = 2
	RIGHT = 3
	ACTIONS = [FOWARD,BACKWARD,LEFT,RIGHT]

	def __init__(self, action = FOWARD):
		if not action in self.ACTIONS:
			raise ValueError("The initial action is not a valid action.")

		self.action = action