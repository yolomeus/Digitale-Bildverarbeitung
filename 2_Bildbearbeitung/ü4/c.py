import cv2
import numpy as np
from scipy.signal import convolve2d

img = cv2.imread('C:\\Users\\Fabian\\Pictures\\memes\\MX_1519172328049.jpg')

sharp_kernel = np.array([[0, 0, 0],
                         [0, 2, 0],
                         [0, 0, 0]]) - np.full((3, 3), 1 / 9)

# sharp_kernel = np.asarray([[-1, -1, -1],
#                            [-1, 9, -1],
#                            [-1, -1, -1]])

mean_kernel = np.full((3, 3), 1 / 9)
edge_kernel = convolve2d(np.array([[1, 0, -1],
                                   [1, 0, -1],
                                   [1, 0, -1]]),
                         np.array([[1, 1, 1],
                                   [0, 0, 0],
                                   [-1, -1, -1]])
                         )

img_sharp = cv2.filter2D(img, -1, sharp_kernel)
img_mean = cv2.filter2D(img, -1, mean_kernel)
img_edge = cv2.filter2D(img, -1, edge_kernel)

cv2.imshow('img', img)
cv2.imshow('img_sharp', img_sharp)
cv2.imshow('img_mean', img_mean)
cv2.imshow('img_edge', img_edge)
cv2.waitKey()
