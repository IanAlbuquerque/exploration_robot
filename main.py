import numpy as np
import skimage.io as skio
import matplotlib.pyplot as plt

import grid

if __name__ == '__main__':
	img = skio.imread("map.jpg")
	my_grid = grid.Grid((30,30),img)

	my_grid.plot()

	my_grid.growBorders()

	my_grid.plot()