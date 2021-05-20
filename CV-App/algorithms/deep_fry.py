import cv2
import numpy as np

from . import Algorithm


class DeepFry(Algorithm):
    fry_level = 1.0

    def process(self, img):
        x = img.astype(np.float32)
        x = x * self.fry_level
        x = x.astype(np.uint8)
        return x

    def mouse_callback(self, event, x, y, flags, param):
        """increase the fry level
        """
        if event == cv2.EVENT_LBUTTONUP:
            self.fry_level += 0.5
