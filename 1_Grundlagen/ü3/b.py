import cv2
import numpy as np

# Hiermit kann die Methode für die Berechnung ausgewählt werden
METHOD = "MANUELL"  # OpenCV

# Einlesen des Bildes
filepath = "../../data/lena.png"
img = cv2.imread(filepath)

h, w, c = img.shape


def quantize(im, low_new, high_new, low_old=0, high_old=255):
    im = im.astype(float)
    im = low_new + (high_new - low_new) * (im - low_old) / (high_old - low_old)
    return im.astype(np.uint8)


ranges = [(0, 127), (0, 3), (0, 255)]

prev = (0, 255)
for a, b in ranges:
    img = quantize(img, a, b, *prev)
    cv2.imshow('flower', img)
    cv2.waitKey()

    prev = a, b
