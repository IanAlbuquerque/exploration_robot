import numpy as np
import skimage.io as skio
import matplotlib.pyplot as plt

import grid

if __name__ == '__main__':
	img = skio.imread("map.jpg")
	my_grid = grid.Grid((30,30),img)

	figure, axe = plt.subplots(ncols=1)
	axe.imshow(np.dstack([my_grid.grid,my_grid.grid,my_grid.grid]), vmin=0, vmax=1, interpolation="nearest", zorder=0)
	plt.show()
	plt.draw()

	my_grid.growBorders()

	figure, axe = plt.subplots(ncols=1)
	axe.imshow(np.dstack([my_grid.grid,my_grid.grid,my_grid.grid]), vmin=0, vmax=1, interpolation="nearest", zorder=0)
	plt.show()
	plt.draw()