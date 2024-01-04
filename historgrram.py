import numpy as py
import cv2 as cv2
def histogram(matrix):
    row,col = len(matrix), len(matrix[0])
    hist =[0 for i in range(0, 256)]

    for i in range(row):
        for j in range(col):
            r = matrix[i][j]
            hist[r] += 1

    return hist
if __name__ =='__main__':
    image = cv2.imread('girl.png',flags=0)
    intensity_histogram = histogram(image)
    print(intensity_histogram)
    cv2.imshow('input_image',image)
    k = cv2.waitKey(0)

    plt.figure(figsize)