import vector
import action

class Hero:

	def __init__(self, position, direction):

		if type(position) != vector.Vector:
			raise ValueError("Invalid type for hero position.")
		if type(direction) != vector.Vector:
			raise ValueError("Invalid type for hero direction.")

		self.position = position
		self.direction = direction

	def doAction(self, action):
		if type(action) != action.Action:
			raise ValueError("Invalid type for action.")

		if action == action.FOWARD:
			self.moveFoward()
		elif action == action.BACKWARD:
			self.moveBackwards()
		elif action == action.LEFT:
			self.turnLeft()
		elif action == action.RIGHT:
			self.turnRight()

	def moveFoward(self):
		self.position = self.position + self.direction.toVector()

	def moveBackwards(self):
		self.position = self.position - self.direction.toVector()

	def turnLeft(self):
		self.direction = self.direction.turnLeft()

	def turnRight(self):
		self.direction = self.direction.turnRight()

	def isInRange(self,y_min,y_max,x_min,x_max):
		return self.position.isInRange(y_min,y_max,x_min,x_max)
