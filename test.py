import cv2
img = cv2.imread('Poster_for_Secret_Obsession.png',0)
print(img)
cv2.imshow('netflix',img)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('test.png',img)
    cv2.destroyAllWindows()