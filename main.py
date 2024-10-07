import matplotlib.image as mpimg
from sklearn.cluster import KMeans 
from matplotlib import pyplot as plt
import numpy as np

img = mpimg.imread('cityview.png')
height, width = img.shape[0], img.shape[1]
img = img.reshape(height//3, 3, width//3, 3, 3)
img = img.transpose(0,2,1,3,4)
img = img.reshape(height//3,width//3, 27)
img = img.reshape(-1,27)

for k in [2, 5, 10, 50, 200, 500, 1000, 2000]:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(img)
    centroids  = kmeans.cluster_centers_
    labels = kmeans.labels_
    labels = labels.reshape(height//3, width//3)
    newImage = np.zeros((height, width, 3))
    for row in range(height//3):
        for col in range(width//3):
            centroid = centroids[labels[row, col]].reshape(3, 3, 3)  # Shape it back to 3x3x3
            newImage[row*3:(row+1)*3, col*3:(col+1)*3, :] = centroid
    plt.imshow(newImage)
    plt.title(f'Image compression with {k} clusters')
    plt.show()