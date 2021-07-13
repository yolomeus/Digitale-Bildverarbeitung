import cv2
import numpy as np

I_in = np.array([
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
    [100, 100, 100, 100, 100],
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
], dtype=np.float32)

highpass = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
], dtype=np.float32)

edge_h = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
], dtype=np.float32)

edge_v = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
], dtype=np.float32)


def threshold(img, at=128):
    img[img >= at] = 255.0
    img[img < at] = 0.0
    return img


im = I_in.copy()
print(im)
im = cv2.filter2D(im, -1, edge_v)
print(im)
im = cv2.filter2D(im, -1, edge_v)
print(im)

im = threshold(im)
print(im)
