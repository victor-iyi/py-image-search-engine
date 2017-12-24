"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 22 December, 2017 @ 10:05 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import os
import argparse

import cv2
import numpy as np
import matplotlib.pyplot as plt

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
image = cv2.imread(args.image)
hist = cv2.calcHist(images=[image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray_hist = cv2.calcHist(images=[gray], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

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
# for (channel, color) in zip(channels, colors):
#     channel_hist = cv2.calcHist([channel], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
#     features.extend(channel_hist)  # extend list by appending elements 4rm d iterable
#     # Plot the histogram
#     plt.plot(channel_hist, color=color, label=f'Channel {color}', linewidth=1)
#     plt.xlim([0, 256])
#
# print('Flatten features shape = {}'.format(np.ravel(features).shape))

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Multi-dimensional histogram [2-D]
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
# Retrieve the color channels
blue, green, red = channels

fig = plt.figure()
# Green and Blue
ax = fig.add_subplot(131)
green_blue_hist = cv2.calcHist(images=[green, blue], channels=[0, 1], mask=None,
                               histSize=[32, 32], ranges=[0, 256]*2)
p = ax.imshow(green_blue_hist, interpolation='nearest')
ax.set_title('Green and Blue')
plt.colorbar(p)

# Green and Red
ax = fig.add_subplot(132)
green_red_hist = cv2.calcHist(images=[green, red], channels=[0, 1], mask=None,
                              histSize=[32, 32], ranges=[0, 256]*2)
p = ax.imshow(green_red_hist, interpolation='nearest')
ax.set_title('Green and Red')
plt.colorbar(p)

# Blue and Red
ax = fig.add_subplot(133)
blue_red_hist = cv2.calcHist(images=[blue, red], channels=[0, 1], mask=None,
                             histSize=[32, 32], ranges=[0, 256]*2)
p = ax.imshow(blue_red_hist, interpolation='nearest')
ax.set_title('Blue and Red')
plt.colorbar(p)
################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Plot the histogram & display image
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
# plt.plot(hist, color='k', label='Image histogram', linewidth=1.5)
# plt.title('Color Histogram')
# plt.xlabel('# of Bins')
# plt.ylabel('Pixel values')
# plt.legend()
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.91, top=0.95, wspace=0.00, hspace=0.20)
plt.show()

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Display images
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
# cv2.imshow('Original', image)
# cv2.imshow('Grayscale', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
