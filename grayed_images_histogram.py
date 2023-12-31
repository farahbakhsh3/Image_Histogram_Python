import copy

import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage.io import imread

def printDetals(image, description):
    print(description)
    print("-"*20)
    print(type(image))
    print(image.dtype)
    print(image.shape)
    print()


image_o = imread("01.jpg")
printDetals(image_o, "Original imge details:")

image = rgb2gray(image_o)
printDetals(image, "Grayed imge details:")

image = (image * 255).astype(np.uint8)
printDetals(image, "Grayed (uint8) imge details:")

fig, ax = plt.subplots(3)
ax[0].imshow(image_o)
ax[1].imshow(image,  cmap="gray")

histogram_array = np.zeros((256,))
for row in image:
    for pixel in row:
        histogram_array[pixel] += 1

x = np.linspace(0, 255, 256)
y = copy.deepcopy(histogram_array)

ax[2].bar(x, y)
plt.show()
