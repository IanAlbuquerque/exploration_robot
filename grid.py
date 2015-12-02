import numpy as np
import skimage.io as skio
import matplotlib.pyplot as plt

class Grid:

	EXIST = 1
	NOT_EXIST = 0

	def __init__(self, shape, image = None):

		if len(shape) != 2:
			raise ValueError("The shape of a Grid object must be a tuple of 2 elements.")
		if shape[0] <= 0 or shape[1] <= 0:
			raise ValueError("Each dimension of the shape of a Grid must be greater than zero.")

		self.shape = shape

		if image is None:
			self.grid = self.NOT_EXIST*np.ones(self.shape)
		else:
			self.grid = self.recoverGridFromImage(image,self.shape)

	def recoverGridFromImage(self, image, shape):
		image_width = image.shape[1]
		image_height = image.shape[0]
		x_step = float(image_width)/shape[1]
		y_step = float(image_height)/shape[0]

		grid = np.zeros(shape)

		for i in xrange(0,shape[1]):
			for j in xrange(0,shape[0]):
				if 0 in image[i*x_step:(i+1)*x_step,j*y_step:(j+1)*y_step]:
					grid[i,j] = self.EXIST
				else:
					grid[i,j] = self.NOT_EXIST

		return grid

	def growBorders(self):
		new_shape = (self.shape[0]+2,self.shape[1]+2)
		new_grid = self.EXIST*np.ones(new_shape)
		new_grid[1:1+self.shape[0],1:1+self.shape[0]] = self.grid
		self.grid = new_grid
		self.shape = new_shape

	def plot(self):
		figure, axe = plt.subplots(ncols=1)
		axe.imshow(np.dstack([self.grid,self.grid,self.grid]), vmin=0, vmax=1, interpolation="nearest", zorder=0)
		plt.show()
