import numpy as np

# Create a 4x4 matrix with random inputs ranging from 1 to 10
matrix_4x4 = np.random.randint(1, 11, size=(4, 4))

# Perform bilinear interpolation to create an 8x8 matrix
def bilinear_interpolation(matrix):
    m, n = matrix.shape
    new_m, new_n = m * 2, n * 2
    interpolated_matrix = np.zeros((new_m, new_n), dtype=matrix.dtype)
    
    for i in range(new_m):
        for j in range(new_n):
            x = j / 2
            y = i / 2
            x1, y1 = int(np.floor(x)), int(np.floor(y))
            x2, y2 = min(x1 + 1, n - 1), min(y1 + 1, m - 1)
            
            dx = x - x1
            dy = y - y1
            
            top_interpolated = matrix[y1, x1] * (1 - dx) + matrix[y1, x2] * dx
            bottom_interpolated = matrix[y2, x1] * (1 - dx) + matrix[y2, x2] * dx
            
            interpolated_matrix[i, j] = top_interpolated * (1 - dy) + bottom_interpolated * dy
    
    return interpolated_matrix

# Perform bilinear interpolation on the 4x4 matrix to create an 8x8 matrix
interpolated_matrix_8x8 = bilinear_interpolation(matrix_4x4)

# Print the original 4x4 matrix and the interpolated 8x8 matrix
print("Original 4x4 matrix:\n", matrix_4x4)
print("\nInterpolated 8x8 matrix:\n", interpolated_matrix_8x8)
