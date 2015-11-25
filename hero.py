import vector

class Hero:

	def __init__(self, position, direction):

		if type(position) != vector.Vector:
			raise ValueError("Invalid type for hero position.")
		if type(direction) != vector.Vector:
			raise ValueError("Invalid type for hero direction.")

		self.position = position
		self.direction = direction

	def moveFoward():
		self.position = self.position + self.direction.toVector()

	def moveBackwards():
		self.position = self.position - self.direction.toVector()

	def isInRange(self,y_min,y_max,x_min,x_max):
		return self.position.isInRange(y_min,y_max,x_min,x_max)
