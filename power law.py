import cv2
import numpy as np
img_input=cv2.imread("girl.png")
img=10*img_input**0.2
img_output=img.astype(np.uint8)
cv2.imshow(winname='input', mat=img_input)
cv2.imshow(winname='power', mat=img_output)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite(img_output, filename='negative_binary_images' )
    cv2.destroyAllWindows()