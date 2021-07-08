import cv2

# Hiermit kann die Methode für die Berechnung ausgewählt werden
import numpy as np

METHOD = "MANUELL"  # OpenCV

# Einlesen des Bildes
filepath = "../../data/flower.jpeg"
img = cv2.imread(filepath)

h, w, c = img.shape
print("Originale Breite:", w)
print("Originale Höhe:", h)

scales = [4, 8, 13.5]
images = []


# todo Methode MANUELL implementieren und 'images' mit diskretisierten Bildern füllen
def discretize(im, k):
    h_old, w_old, _ = im.shape
    h_bound, w_bound = h_old - 1, w_old - 1
    for i in np.arange(0, h_old, k):
        for j in np.arange(0, w_old, k):
            i_to = min(round(i + k), h_bound)
            j_to = min(round(j + k), w_bound)

            i = min(round(i), h_bound)
            j = min(round(j), w_bound)

            im[i:i_to, j:j_to] = img[i, j]
    return im


cv2.imshow('flower', discretize(img, 41.5214242))
cv2.waitKey()


# todo Methode OpenCV implementieren und 'images' mit diskretisierten Bildern füllen


# todo Bilder darstellen
