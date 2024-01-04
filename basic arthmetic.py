import numpy as np


matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])


matrix_sum = matrix1 + matrix2
print("Matrix Addition -")
print(matrix_sum)


matrix_diff = matrix1 - matrix2
print("Matrix Subtraction - ")
print(matrix_diff)


# matrix_inverse = np.linalg.inv(matrix1)
# print("INVERSE OF MATRIX 1")
# print(matrix_inverse)


matrix_product = np.dot(matrix1, matrix2)
print("Product of matrix is -")
print(matrix_product)