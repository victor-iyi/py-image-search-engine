"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 22 December, 2017 @ 10:05 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import argparse
import cv2
# import numpy as np
import matplotlib.pyplot as plt


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Command line arguments...
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required=False, help='Path to image.')
# args = vars(parser.parse_args())  # converts list of objects to a dictionary
args = parser.parse_args()

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | loading the image
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
# if the argument - image is set. Otherwise use this image.
args.image = args.image if args.image else '../images/jurassic-park/grant.jpg'

img = cv2.imread(args.image)


################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Computing a Grayscale Histogram
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
# Plot the histogram

cv2.imshow('Image', img)
cv2.imshow('Gray', gray)

plt.figure()
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
