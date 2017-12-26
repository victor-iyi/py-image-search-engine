"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 22 December, 2017 @ 10:05 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import argparse
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Default images
image_folder = '../images/jurassic-park/'
default_images = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img[0] is not '.']

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Command line arguments
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image',
                    default=default_images[0],
                    help='Image to find it\'s color histogram')
args = parser.parse_args()

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Calculating the Histogram
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
fig = plt.figure()

image = cv2.imread(args.image)
hist = cv2.calcHist(images=[image], channels=[0], mask=None,
                    histSize=[256], ranges=[0, 256])
ax = plt.subplot2grid(shape=(2, 3), loc=(0, 0))
ax.plot(hist)
ax.set_title('Single Histogram')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_hist = cv2.calcHist(images=[gray], channels=[0], mask=None,
                         histSize=[256], ranges=[0, 256])
ax = plt.subplot2grid(shape=(2, 3), loc=(0, 1))
ax.plot(gray_hist)
ax.set_title('Gray Histogram')
################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Computing histogram for each color channel
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
features = []
colors = ('b', 'g', 'r')
channels = cv2.split(image)

# Loop through each channel. one at a time
# computing each channel's histogram
ax = plt.subplot2grid(shape=(2, 3), loc=(0, 2))
for (channel, color) in zip(channels, colors):
    channel_hist = cv2.calcHist([channel], channels=[0], mask=None,
                                histSize=[256], ranges=[0, 256])
    features.extend(channel_hist)  # extend list by appending elements 4rm d iterable
    # Plot the histogram
    ax.plot(channel_hist, color=color, label=f'Channel {color}', linewidth=1)
    ax.set_title('Channel Histogram')

print('Flatten features shape = {}'.format(np.ravel(features).shape))

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Multi-dimensional Histogram [3-D]
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
hist_3D = cv2.calcHist(images=[image], channels=[0, 1, 2], mask=None,
                       histSize=[32, 32, 32], ranges=[0, 256] * 3)
print('3D histogram has shape of {} with {:,} feature values'.format(hist_3D.shape,
                                                                     hist_3D.flatten().shape[0]))

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Multi-dimensional histogram [2-D]
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
# Retrieve the color channels
blue, green, red = channels

# Green and Blue
ax = plt.subplot2grid(shape=(2, 3), loc=(1, 0))
green_blue_hist = cv2.calcHist(images=[green, blue], channels=[0, 1], mask=None,
                               histSize=[32, 32], ranges=[0, 256] * 2)
p = ax.imshow(green_blue_hist, interpolation='nearest')
ax.set_title('Green and Blue')
plt.colorbar(p)

# Green and Red
ax = plt.subplot2grid(shape=(2, 3), loc=(1, 1))
green_red_hist = cv2.calcHist(images=[green, red], channels=[0, 1], mask=None,
                              histSize=[32, 32], ranges=[0, 256] * 2)
p = ax.imshow(green_red_hist, interpolation='nearest')
ax.set_title('Green and Red')
plt.colorbar(p)

# Blue and Red
ax = plt.subplot2grid(shape=(2, 3), loc=(1, 2))
blue_red_hist = cv2.calcHist(images=[blue, red], channels=[0, 1], mask=None,
                             histSize=[32, 32], ranges=[0, 256] * 2)
p = ax.imshow(blue_red_hist, interpolation='nearest')
ax.set_title('Blue and Red')
plt.colorbar(p)

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Plot the histogram & display image
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
plt.subplots_adjust(left=0.08, bottom=0.04, right=0.94, top=0.92, wspace=0.44, hspace=0.23)
plt.show()

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Display images
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
