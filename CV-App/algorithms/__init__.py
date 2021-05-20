class Algorithm:
    """ An abstract class to create custom algorithms """

    def process(self, img):
        """ Processes the input image"""
        return img

    def mouse_callback(self, event, x, y, flags, param):
        """ Reacts on mouse callbacks """
        return


''' Import algorithms to use'''
from .deep_fry import DeepFry
from .image_to_gray import ImageToGray
from .image_to_hue import ImageToHue
from .motion_detector import MotionDetector
from .segmentation_tracker import SegmentationTracker
from .spin import Spin
from .white_balancing import WhiteBalancing
from .tutorial_algorithm import TutorialAlgorithm

''' Link Algorithms to keys '''
algorithms = dict()
algorithms["0"] = Algorithm
algorithms["1"] = ImageToGray
algorithms["2"] = ImageToHue
algorithms["3"] = MotionDetector
algorithms["4"] = WhiteBalancing
algorithms["5"] = Spin
algorithms["6"] = SegmentationTracker
algorithms["7"] = TutorialAlgorithm
algorithms["d"] = DeepFry
