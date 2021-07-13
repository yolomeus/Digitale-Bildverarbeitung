import itertools

import cv2
import numpy as np
from numpy import linalg

''' Einlesen des Bildes '''
img = cv2.imread("data/normal.jpg")

''' 
Schritt 1: Geben Sie eine Transformationvorschrift T an, die das Eingangsbild
    - mit dem Faktor s_x ungleich 0 in x-Richtung skaliert 
    - mit dem Faktor s_y ungleich 0 in y-Richtung skaliert 
'''
s_x = 2
s_y = 2

T = np.array([[s_x, 0],
              [0, s_y]])
''' 
Schritt 2: Geben Sie geben sie die Inverse T_inv zu T an
'''
T_inv = linalg.inv(T)

'''
Schritt 3: Implementieren Sie eine Funktion scale(img, sx, sy), welche das Bild nach der Skalierung wiedergibt.
Verwenden Sie für die Transformation das Backward-Mapping und für die Interpolation Nearest-Neighbour Interpolation.
'''


def scale(img, s_x, s_y):
    h, w, c = img.shape
    h_new, w_new = round(s_y * h), round(s_x * w)

    coords_new = tuple(itertools.product(range(w_new), range(h_new)))
    coords_new = np.stack(coords_new)

    T = np.array([[s_x, 0],
                  [0, s_y]])

    T_inv = linalg.inv(T)
    coords = T_inv @ coords_new.T

    # round to nearest neighbour
    coords = np.round(coords).astype('uint8')
    coords[0, coords[0] >= w] = w - 1
    coords[1, coords[1] >= h] = h - 1

    new_im = np.zeros((h_new, w_new, c), dtype='uint8')

    coords_new = coords_new.T
    x_old, y_old = coords
    x_new, y_new = coords_new

    new_im[y_new, x_new] = img[y_old, x_old]

    return new_im


''' Ausgabe des Bildes '''
new_img = scale(img, 10, 2)
cv2.imshow('img_old', img)
cv2.imshow('img', new_img)
cv2.waitKey(0)
