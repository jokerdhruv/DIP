# import cv2
# import numpy as np
#
#
# image_path = "Poster_for_Secret_Obsession.png"  # Replace with your image path
# input_image = cv2.imread('Poster_for_Secret_Obsession.png', cv2.IMREAD_GRAYSCALE)
#
# padding_size = 20
#
#
# padded_image = cv2.copyMakeBorder(input_image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_CONSTANT, value=0)
#
#
# cv2.imshow('Original Image', input_image)
# cv2.imshow('Padded Image', padded_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np


image_path = 'Poster_for_Secret_Obsession.png'
input_image = cv2.imread('Poster_for_Secret_Obsession.png', cv2.IMREAD_GRAYSCALE)


padding_size = 20
padding_color = 255
padded_image = cv2.copyMakeBorder(input_image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_CONSTANT, value=padding_color)

# Display the original and padded images
cv2.imshow('Original Image', input_image)
cv2.imshow('Padded Image', padded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


