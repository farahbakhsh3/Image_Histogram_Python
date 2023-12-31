import copy
import numpy as np
from matplotlib import pyplot as plt
from skimage.io import imread
from tqdm import tqdm


def printDetals(image, description):
    print(description)
    print("-" * 20)
    print(type(image))
    print(image.dtype)
    print(image.shape)
    print()


image = imread("04.jpg")
printDetals(image, "Original imge details:")

fig, ax = plt.subplots(4)
ax[0].imshow(image)

histogram_array = np.zeros((3, 256))
for row in tqdm(image):
    for pixel in row:
        for idx, color in enumerate(pixel):
            histogram_array[idx, color] += 1

x = np.linspace(0, 255, 256)
yR = copy.deepcopy(histogram_array[0])
yG = copy.deepcopy(histogram_array[1])
yB = copy.deepcopy(histogram_array[2])

ax[1].bar(x, yR, align="center", color="Red")
ax[2].bar(x, yG, align="center", color="Green")
ax[3].bar(x, yB, align="center", color="Blue")
plt.show()
