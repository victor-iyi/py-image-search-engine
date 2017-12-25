"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 25 December, 2017 @ 7:18 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import os
import glob
import argparse

import cv2

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dataset', default='../images/lord-of-the-rings/',
                    help='Path to dataset.')
parser.add_argument('i', '--index', default='../saved/index.pkl',
                    help='Path to the index file.')
args = parser.parse_args()


class RGBHistogram:
    """
    Image descriptor using color histogram.

    :param bins: list
        Histogram size. 1-D list containing ideal values
        between 8 and 128; but you can go up till 0 - 256.

    Example:
        >>> histogram = RGBHistogram(bins=[32, 32, 32])
        >>> feature_vector = histogram.describe(image='folder/image.jpg')
        >>> print(feature_vector.shape)
    """

    def __init__(self, bins):
        self.bins = bins

    def describe(self, image):
        """
        Color description of a given image

        compute a 3D histogram in the RGB color space,
        then normalize the histogram so that images
        with the same content, but either scaled larger
        or smaller will have (roughly) the same histogram

        :param image:
            Image to be described.
        :return: flattened 3-D histogram
            Flattened descriptor [feature vector].
        """
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        hist = cv2.calcHist(images=[image], channels=[0, 1, 2], mask=None,
                            histSize=self.bins, ranges=[0, 256] * 3)
        hist = cv2.normalize(hist, dst=hist.shape)
        return hist.flatten()


# key - image file name, value - computed feature vector/descriptor
index = {}
descriptor = RGBHistogram(bins=[8, 8, 8])

for image in glob.glob(os.path.join(args.dataset, '*.png')):
    print(image)
