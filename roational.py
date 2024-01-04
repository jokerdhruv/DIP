# import numpy as np
#
# def rotate_matrix(matrix, angle):
#     if len(matrix) == 0:
#         return []
#
#     rows, cols = len(matrix), len(matrix[0])
#
#     rotated_matrix = []
#
#     if angle == 90:
#         rotated_matrix = [[0] * rows for _ in range(cols)]
#         for i in range(rows):
#             for j in range(cols):
#                 rotated_matrix[j][rows - i - 1] = matrix[i][j]
#     elif angle == 180:
#         rotated_matrix = [[0] * cols for _ in range(rows)]
#         for i in range(rows):
#             for j in range(cols):
#                 rotated_matrix[rows - i - 1][cols - j - 1] = matrix[i][j]
#     else:
#         print("Invalid angle. Supported angles are 90 and 180 degrees.")
#         return []
#
#     return rotated_matrix
#
# current_matrix = np.random.randint(0, 40, size=(3, 3))
#
# while True:
#     print("Matrix:\n", current_matrix)
#
#     rotation_angle = int(input("Enter rotation angle (90, 180): "))
#
#     current_matrix = rotate_matrix(current_matrix, rotation_angle)
#
#     print("Rotated Matrix:")
#     for row in current_matrix:
#         print(row)
#
#     continue_option = input("Do you want to continue rotating? (yes/no): ")
#     if continue_option.lower() != 'yes':
#         break
#
#
#
# # Print the rotated matrix
# for row in rotated_matrix:
#     print(row)

import cv2

# Load the image
image = cv2.imread('your_image.jpg')

# Rotate the image by 180 degrees
rotated_image = cv2.rotate(image, cv2.ROTATE_180)

# Display the rotated image (optional)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the rotated image (optional)
cv2.imwrite('rotated_image.jpg', rotated_image)
