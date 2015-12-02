import skimage.io as skio
import matplotlib.pyplot as plt

from skimage import img_as_float

def plotImage(image):
	figure, axe = plt.subplots(ncols=1)
	axe.imshow(image, vmin=0, vmax=1, interpolation="nearest", zorder=0)
	plt.show()

def readImage(image_path):
	img = skio.imread(image_path)
	float_img = img_as_float(img)
	return float_img