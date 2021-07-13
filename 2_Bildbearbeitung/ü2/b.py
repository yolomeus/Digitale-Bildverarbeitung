import cv2
import numpy as np

im = cv2.imread('data/edge_01.png')
sobel = np.array([[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]], dtype='float32')

im = cv2.medianBlur(im, 3)
im = cv2.filter2D(im, -1, sobel)

im = cv2.blur(im, (3, 3))
cv2.imshow('kek', im.astype('uint8'))
cv2.waitKey()
