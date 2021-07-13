import itertools
import math

import cv2
import numpy as np
from numpy.linalg import inv


def apply_transform(img, mat):
    h, w, c = img.shape
    new_coords = tuple(itertools.product(range(w), range(h)))
    new_coords = np.array(new_coords)

    translate = mat[:, -1][np.newaxis].T
    old_coords = inv(mat[:, :2]) @ new_coords.T - translate

    old_coords = np.round(old_coords).astype(int)
    # discard coordinates outside the image frame
    is_in_bounds = (old_coords[0] < w - 1) & (old_coords[0] >= 0) & (old_coords[1] < h - 1) & (old_coords[1] >= 0)

    old_coords = old_coords[:, is_in_bounds]
    new_coords = new_coords.T[:, is_in_bounds]

    new_img = np.zeros((h, w, c), dtype='uint8')

    x_old, y_old = old_coords
    x_new, y_new = new_coords
    new_img[y_new, x_new] = img[y_old, x_old]
    return new_img


def main():
    p = 1.0
    c = .2
    x = math.pi / 4.0

    rot = np.array([[np.cos(x), np.sin(x), 0.0],
                    [-np.sin(x), np.cos(x), 50]])

    m_0 = p * rot
    m_1 = c + (p - c) * rot
    m_2 = c + (p - c) * np.array([[1, 0.8],
                                  [0, 1]])

    img = cv2.imread('data/normal.jpg')
    for m_i in [m_0, m_1, m_2]:
        img_t = apply_transform(img, m_i)
        cv2.imshow('kek', img_t)
        cv2.waitKey()


if __name__ == '__main__':
    main()
