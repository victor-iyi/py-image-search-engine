import cv2

# Reading an image file
img = cv2.imread('images/jurassic-park-tour-jeep.jpg')

print(f'Image shape: {img.shape}')

# displaying image
cv2.imshow('Original', img)

# Resizing image
new_width = 250
ratio = new_width / img.shape[1]  # 100 / width
dim = (new_width, int(img.shape[0] * ratio))

resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Resized', resized)

# Press any key to exit...
cv2.waitKey(0)
cv2.destroyAllWindows()
