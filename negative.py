import cv2
img_input=cv2.imread("girl.png")
img_output=255 - img_input
cv2.imshow(winname='input', mat=img_input)
cv2.imshow(winname='negative', mat=img_output)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite(img_output, filename='negative_binary_images' )
    cv2.destroyAllWindows()
