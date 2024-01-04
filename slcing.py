import cv2
import numpy as np

image_path = 'girl.png'
input_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

lower_threshold = 100
upper_threshold = 200

mask = np.logical_and(input_image >= lower_threshold, input_image <= upper_threshold)

output_image = np.zeros_like(input_image)
output_image[mask] = input_image[mask]

cv2.imshow('Original Image', input_image)
cv2.imshow('Intensity-Sliced Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
