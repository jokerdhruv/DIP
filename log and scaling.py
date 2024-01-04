import cv2 as cv2
import numpy as np
image = cv2.imread('girl.png')
# Ensure the image is in grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the log transformation
log_transformed: None = np.log1p(gray_image)
# Normalize the log-transformed image to the 0-255 range
# scaled_image = cv2.normalize(log_transformed, None, 0, 255, cv2.NORM_MINMAX)


cv2.imshow('Original Image', gray_image)
cv2.imshow('Scaled Image',log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('scaled_image.jpg', log_transformed)
