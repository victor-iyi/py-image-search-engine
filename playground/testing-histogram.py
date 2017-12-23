"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 22 December, 2017 @ 10:05 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import argparse

import cv2
import matplotlib.pyplot as plt

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Command line arguments
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
parser = argparse.ArgumentParser()
# Arguments
parser.add_argument('-i', '--image',
                    default='../images/jurassic-park/grant.jpg',
                    help='Image to find it\'s color histogram')
args = parser.parse_args()

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Loading images
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
args.image = args.image if args.image else '../images/jurassic-park/grant.jpg'

img = cv2.imread(args.image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Plot the histogram & display image
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
# Display image
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plot histogram
plt.figure()
plt.plot(hist)
plt.title('Color Histogram')
plt.xlabel('# of Bins')
plt.ylabel('Pixel values')
plt.show()

