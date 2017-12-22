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
img_original_shape = img_original.shape   # (height, width, channel)
print(f'Original image shape = {img_original_shape}')

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Resizing images
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
"""
We have to keep the aspect ratio of the image in mind, which is the 
proportional relationship of the width and the height of the image. 
In this case, we are resizing the image to have a 200 pixel width, 
therefore, we need to calculate r, the ratio of the new width to 
the old width. Then, we construct the new dimensions of the image 
by using 100 pixels for the width, and r x the old image height. 
Doing this allows us to maintain the aspect ratio of the image.
"""
new_height = 200
r = new_height / img_original_shape[1]  # new_height / old_width = aspect_ratio[width]
dim = (new_height, int(img_original_shape[0] * r))  # [new_height, (old_height * ratio)]

img_resized = cv2.resize(img_original, dim, interpolation=cv2.INTER_AREA)
img_resized_shape = img_resized.shape
print(f'Resized image shape = {img_resized_shape}')

################################################################################################
# +———————————————————————————————————————————————————————————————————————————————————————————+
# | Rotating images
# +———————————————————————————————————————————————————————————————————————————————————————————+
################################################################################################
(h, w) = img_original_shape[:2]
center = (h/2, w/2)

rotation_matrix = cv2.getRotationMatrix2D(center, 180, 1.0)
img_rotated = cv2.warpAffine(img_original, rotation_matrix, (w, h))

# Display images
cv2.imshow('Original', img_original)
cv2.imshow('Resized', img_resized)
cv2.imshow('Rotated', img_rotated)

# Press any key to exit...
cv2.waitKey(0)
cv2.destroyAllWindows()
