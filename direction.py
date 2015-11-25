import vector

class Direction:
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3
	DIRECTIONS = [NORTH,EAST,WEST,SOUTH]

	def __init__(self, initial_direction = NORTH):
		if not initial_direction in self.DIRECTIONS:
			raise ValueError("The initial direction is not a valid direction.")

		self.direction = initial_direction

	def turnRight():
		if self.direction == self.NORTH:
			self.direction = self.EAST
		elif self.direction == self.EAST:
			self.direction = self.SOUTH
		elif self.direction == self.SOUTH:
			self.direction = self.WEST
		elif self.direction == self.WEST:
			self.direction = self.NORTH

	def turnLeft():
		if self.direction == self.NORTH:
			self.direction = self.WEST
		elif self.direction == self.EAST:
			self.direction = self.NORTH
		elif self.direction == self.SOUTH:
			self.direction = self.EAST
		elif self.direction == self.WEST:
			self.direction = self.SOUTH

	def toVector():
		if self.direction == self.NORTH:
			return vector.Vector((-1,0))
		elif self.direction == self.EAST:
			return vector.Vector((0,1))
		elif self.direction == self.SOUTH:
			return vector.Vector((1,0))
		elif self.direction == self.WEST:
			return vector.Vector((0,-1))