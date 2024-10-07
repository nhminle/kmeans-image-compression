import matplotlib.image as mpimg
from sklearn.cluster import KMeans 
from matplotlib import pyplot as plt
import numpy as np

img = mpimg.imread('cityview.png')
img = img.reshape(260, 3, 428, 3, 3)
img = img.transpose(0,2,1,3,4)
img = img.reshape(260,428, 27)
img = img.reshape(-1,27)

kmeans = KMeans(n_clusters=2)
kmeans.fit(img)
centroids  = kmeans.cluster_centers_
labels = kmeans.labels_
labels = labels.reshape(260, 428)
newImage = np.zeros((260, 428, 3))
for row in range(260):
    for col in range(428):
        for channel in range(3):
            newImage[row, col, channel] = np.mean(centroids[labels[row, col]][channel::3])
plt.imshow(newImage)
plt.show()