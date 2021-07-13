import cv2
import numpy as np

KERNEL_SIZE = 20

# Einlesen des Bildes
filepath = "../../data/text_%s.jpg"
images = list()
for i in [1, 2, 3]:
    img = cv2.imread(filepath % i)
    img = cv2.resize(img, (500, 500))
    images.append(img)


def brightness_adjust(im, k):
    bg = cv2.blur(im, (k, k))
    im_new = im / bg
    im_new = 255.0 * (im_new - im_new.min()) / (im_new.max() - im_new.min())
    return im_new.astype(np.uint8)


for img in images:
    cv2.imshow('kke', brightness_adjust(img, 13))
    cv2.waitKey()
