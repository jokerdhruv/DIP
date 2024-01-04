# import cv2
# import numpy as py
#
# img = cv2.imread("girl.png")
# img_output = cv2.rotate(img,cv2.ROTATE_180)
# cv2.imshow('input img' , img)
# cv2.imshow('Rotated img', img_output)
# key = cv2.waitKey(0)
# if key == 27:
#     cv2.destroyAllWindows()
# elif key == ord('s'):
#     cv2.imwrite(img_output, filename='Exam_rotated_img')
#     cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# img_inp = cv2.imread("girl.png")
# img_inp = np.size
# img_inp =
# img_output = np.zeros_like(img_inp)
# for i in range(x-1):
#     for j in range (y-1)):
#         img_output[i,j] = img_inp [x-i,j]
#
# cv2.imshow(winname='input', mat=img_inp)
# cv2.imshow(winname='contrast', mat=img_output)
#
# key=cv2.waitKey(0)
# if key==27:
#     cv2.destroyAllWindows()
# elif key==ord('s'):
#     cv2.imwrite(img_output, filename='contrast strateched img' )
#     cv2.destroyAllWindows()


import cv2
import numpy as np

img_inp = cv2.imread("girl.png")


x, y, _ = img_inp.shape

img_output = np.zeros_like(img_inp)


for i in range(x):
    for j in range(y):
        img_output[i, j] = img_inp[x - i - 1, j]


cv2.imshow(winname='input', mat=img_inp)
cv2.imshow(winname='contrast', mat=img_output)

key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('contrast_stretched_img.png', img_output)
    cv2.destroyAllWindows()
