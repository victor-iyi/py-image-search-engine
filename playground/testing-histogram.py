"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 22 December, 2017 @ 10:05 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import argparse

import cv2
import numpy as np
import matplotlib.pyplot as plt

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Command line arguments
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
parser = argparse.ArgumentParser()
# Arguments
parser.add_argument('-i', '--image',
                    default='../images/jurassic-park/jurassic-park-tour-jeep.jpg',
                    help='Image to find it\'s color histogram')
args = parser.parse_args()

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Calculating the Histogram
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################

image = cv2.imread(args.image)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist(images=[image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Flattened color histogram
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
features = []
colors = ('b', 'g', 'r')
channels = cv2.split(image)

# Loop through each channel. one at a time
# computing each channel's histogram
for (channel, color) in zip(channels, colors):
    channel_hist = cv2.calcHist([channel], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    features.extend(channel_hist)  # extend list by appending elements 4rm d iterable
    # Plot the histogram
    plt.plot(channel_hist, color=color, label=f'Channel {color}', linewidth=1)
    plt.xlim([0, 256])

print('Flatten features shape = {}'.format(np.ravel(features).shape))
################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Plot the histogram & display image
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
# Plot histogram
plt.plot(hist, color='k', label='Image histogram', linewidth=1.5)
plt.title('Color Histogram')
plt.xlabel('# of Bins')
plt.ylabel('Pixel values')
plt.legend()
plt.show()

# Display image
# cv2.imshow('Original', image)
# cv2.imshow('Grayscale', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
