import cv2

# Reading an image file
image = cv2.imread('images/jurassic-park-tour-jeep.jpg')

# displaying image
cv2.imshow('Original', image)

# press any key to exit...
cv2.waitKey(0)
cv2.destroyAllWindows()
