class Vector:

	def __init__(self, value):
		if len(value) != 2:
			raise ValueError("The value of a vector object must be a tuple of 2 elements.")

		self.y = value[0]
		self.x = value[1]

	def __add__(self,other):
		if type(other) == Vector:
			self.y += other.y
			self.x += other.x
		elif type(other) == Vector:
			if len(other) != 2:
				raise ValueError("Vectors can only be added with tuples with 2 values.")
			self.y += other[0]
			self.x += other[1]
		else:
			raise ValueError("Invalid type for operation.")

	def __radd__(self,other):
		self.__add__(other)

	def __sub__(self,other):
		if type(other) == Vector:
			self.y -= other.y
			self.x -= other.x
		elif type(other) == Vector:
			if len(other) != 2:
				raise ValueError("Vectors can only be subtracted with tuples with 2 values.")
			self.y -= other[0]
			self.x -= other[1]
		else:
			raise ValueError("Invalid type for operation.")

	def __rsub__(self,other):
		self.__sub__(other)

	def __mul__(self,other):
		if type(other) == int or type(other) == float:
			self.y *= other
			self.x *= other
		else:
			raise ValueError("Invalid type for operation.")

	def __rmul__(self,other):
		self.__mul__(other)

	def isInRange(self,y_min,y_max,x_min,x_max):
		return self.x >= x_min and self.x < x_max and self.y >= y_min and self.y < y_max


