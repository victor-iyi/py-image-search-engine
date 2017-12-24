"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 22 December, 2017 @ 9:57 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image',
                    default='../images/jurassic-park/grant.jpg',
                    help='Image to find color histogram')
args = parser.parse_args()

image = cv2.imread(args.image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
multi_hist = cv2.calcHist(images=[image, gray], channels=[0, 1], mask=None,
                          histSize=[64, 64], ranges=[0, 256, 0, 256])
plt.plot(multi_hist)

channels, colors, features = cv2.split(image), ('b', 'g', 'r'), []

# Histogram for each color channels
for channel, color in zip(channels, colors):
    hist = cv2.calcHist([channel], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    features.extend(hist)
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

print('Channels shape: {}'.format(np.shape(channels)))
print('Flattened histogram shape: {}'.format(np.ravel(features).shape))

plt.title('Color histogram')
plt.xlabel('Histogram range')
plt.ylabel('No of pixels')
plt.show()

cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
