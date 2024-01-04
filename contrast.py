import cv2
import numpy as np


image_path = 'girl.png'
input_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

desired_min = 0
desired_max = 255

current_min = np.min(input_image)
current_max = np.max(input_image)

stretched_image = (input_image - current_min) * ((desired_max - desired_min) / (current_max - current_min)) + desired_min

stretched_image = stretched_image.astype(np.uint8)

cv2.imshow('Original Image', input_image)
cv2.imshow('Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
