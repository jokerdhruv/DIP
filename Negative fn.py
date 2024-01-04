# import cv2
# import numpy as np


# image_path = 'girl.png'
# binary_image = cv2.imread('girl.png', cv2.IMREAD_GRAYSCALE)

# binary_image[binary_image > 0] = 255

# inverted_image = 255 - binary_image


# cv2.imshow('Original Binary Image', binary_image)
# cv2.imshow('Inverted Image', inverted_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

img_inp = cv2.imread("girl.png")
img_inp.size = [x,y]
img_output = np.zeros_like(img_inp)
for i in range( x=0 <= x-1):
    for j in range(y=0 <= y-1)  :
        img_output[i,j] = img_inp [x-i,j]

cv2.imshow(winname='input', mat=img_inp)
cv2.imshow(winname='contrast', mat=img_output)

key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite(img_output, filename='contrast strateched img' )
    cv2.destroyAllWindows()