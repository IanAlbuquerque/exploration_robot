import vector

class Direction:
	NORTH_VALUE = 0
	EAST_VALUE = 1
	SOUTH_VALUE = 2
	WEST_VALUE = 3
	DIRECTIONS_VALUES = [NORTH_VALUE,EAST_VALUE,WEST_VALUE,SOUTH_VALUE]

	def __init__(self, initial_direction = NORTH_VALUE):
		if not initial_direction in self.DIRECTIONS_VALUES:
			raise ValueError("The initial direction is not a valid direction.")

		self.direction = initial_direction

	def turnRight(self):
		if self.direction == self.NORTH_VALUE:
			self.direction = self.EAST_VALUE
		elif self.direction == self.EAST_VALUE:
			self.direction = self.SOUTH_VALUE
		elif self.direction == self.SOUTH_VALUE:
			self.direction = self.WEST_VALUE
		elif self.direction == self.WEST_VALUE:
			self.direction = self.NORTH_VALUE

	def turnLeft(self):
		if self.direction == self.NORTH_VALUE:
			self.direction = self.WEST_VALUE
		elif self.direction == self.EAST_VALUE:
			self.direction = self.NORTH_VALUE
		elif self.direction == self.SOUTH_VALUE:
			self.direction = self.EAST_VALUE
		elif self.direction == self.WEST_VALUE:
			self.direction = self.SOUTH_VALUE

	def toVector(self):
		if self.direction == self.NORTH_VALUE:
			return vector.Vector((-1,0))
		elif self.direction == self.EAST_VALUE:
			return vector.Vector((0,1))
		elif self.direction == self.SOUTH_VALUE:
			return vector.Vector((1,0))
		elif self.direction == self.WEST_VALUE:
			return vector.Vector((0,-1))

NORTH = Direction(Direction.NORTH_VALUE)
EAST = Direction(Direction.EAST_VALUE)
SOUTH = Direction(Direction.SOUTH_VALUE)
WEST = Direction(Direction.WEST_VALUE)

DIRECTIONS = [NORTH,EAST,SOUTH,WEST]
