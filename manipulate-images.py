"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 20 December, 2017 @ 8:04 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import cv2

# Load images
img_file = 'images/jurassic-park-tour-jeep.jpg'
img_original = cv2.imread(img_file)

# image shape
img_original_shape = img_original.shape
print(f'Original image shape = {img_original_shape}')

# Resize dimensions [aspect ratio]
# ratio of the new image to the old one
r = 100 / img_original_shape[1]  # new_height / old_width
dim = (100, int(img_original_shape[0] * r))  # [new_height, (old_height * ratio)]

img_resized = cv2.resize(img_original, dim, interpolation=cv2.INTER_AREA)

# Display images
cv2.imshow('Original', img_original)
cv2.imshow('Resized', img_resized)

# Press any key to exit...
cv2.waitKey(0)
cv2.destroyAllWindows()
