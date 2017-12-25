"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 25 December, 2017 @ 7:18 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import cv2


class RGBHistogram:

    def __init__(self, bins=(8, 8, 8)):
        """
        Image descriptor using color histogram.

        :param bins: list,
        """
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
        :return:
            Flattened descriptor.
        """
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        hist = cv2.calcHist(images=[image], channels=[0, 1, 2], mask=None,
                            histSize=self.bins, ranges=[0, 256] * 3)
        hist = cv2.normalize(hist)
        return hist.flatten()
