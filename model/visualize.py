import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

labeled_images = pd.read_csv('data/train.csv')

row, col = (10, 16)

nums = []
for i in range(10):
    nums.append(labeled_images[labeled_images['label'] == i].sample(col))

fig, axes = plt.subplots(row, col)

for axe in axes.flat:
    axe.get_xaxis().set_visible(False)
    axe.get_yaxis().set_visible(False)

fig.suptitle("Samples of Digit")

for i, num in enumerate(nums):
    for k in range(col): 
        img = num.iloc[k].to_numpy()
        img = img[1:].reshape((28,28))
        axes[i][k].imshow(img,cmap='gray_r')

plt.show()