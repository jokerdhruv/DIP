import cv2
import numpy as np
img_input=cv2.imread("girl.png")
above=img_input>200
img_output=np.zeros_like(img_input)
img_output[above]=255
cv2.imshow(winname='input', mat=img_input)
cv2.imshow(winname='power', mat=img_output)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite(img_output, filename='negative_binary_images' )
    cv2.destroyAllWindows()