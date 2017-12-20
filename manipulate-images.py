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


# Display images
cv2.imshow('Original', img_original)

# Press any key to exit...
cv2.waitKey(0)
cv2.destroyAllWindows()
