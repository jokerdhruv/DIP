import numpy as np

def bilinear_interpolation(source, target, source_corner, target_corner):
    for i in range(target_corner[0], target_corner[0] + source.shape[0]):
        for j in range(target_corner[1], target_corner[1] + source.shape[1]):
            source_row = i - target_corner[0]
            source_col = j - target_corner[1]
            
            # Calculate the fractional coordinates within the source matrix
            x = source_col
            y = source_row
            
            # Calculate integer and fractional parts of coordinates
            x_int = int(x)
            y_int = int(y)
            x_frac = x - x_int
            y_frac = y - y_int
            
            # Perform bilinear interpolation
            top_left = source[y_int, x_int]
            top_right = source[y_int, min(x_int + 1, source.shape[1] - 1)]
            bottom_left = source[min(y_int + 1, source.shape[0] - 1), x_int]
            bottom_right = source[min(y_int + 1, source.shape[0] - 1), min(x_int + 1, source.shape[1] - 1)]
            
            interpolated_value = (1 - x_frac) * (1 - y_frac) * top_left + \
                                 x_frac * (1 - y_frac) * top_right + \
                                 (1 - x_frac) * y_frac * bottom_left + \
                                 x_frac * y_frac * bottom_right
            
            target[i, j] = interpolated_value

# Create a 4x4 matrix with random integer values between 1 and 10
random_4x4_matrix = np.random.randint(1, 11, size=(4, 4))

# Create an 8x8 matrix filled with zeros
bilinear_8x8_matrix = np.zeros((8, 8), dtype=int)

# Populate the 8x8 matrix using bilinear interpolation
bilinear_interpolation(random_4x4_matrix, bilinear_8x8_matrix, (0, 0), (0, 0))
bilinear_interpolation(random_4x4_matrix, bilinear_8x8_matrix, (0, 3), (0, 4))
bilinear_interpolation(random_4x4_matrix, bilinear_8x8_matrix, (3, 0), (4, 0))
bilinear_interpolation(random_4x4_matrix, bilinear_8x8_matrix, (3, 3), (4, 4))

# # Define a threshold value for converting to binary intensity
# threshold = 5

# # Convert the values in the 8x8 matrix to binary intensity values
# binary_8x8_matrix = (bilinear_8x8_matrix >= threshold).astype(int)

# # Function to check if neighbors have the same intensity value
# def has_same_intensity(matrix, row, col):
#     intensity = matrix[row, col]
    
#     neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1),
#                  (row, col-1),                 (row, col+1),
#                  (row+1, col-1), (row+1, col), (row+1, col+1)]
    
#     for r, c in neighbors:
#         if 0 <= r < matrix.shape[0] and 0 <= c < matrix.shape[1]:
#             if matrix[r, c] != intensity:
#                 return False
#     return True

# # Check neighboring intensity values
# for i in range(binary_8x8_matrix.shape[0]):
#     for j in range(binary_8x8_matrix.shape[1]):
#         if has_same_intensity(binary_8x8_matrix, i, j):
#             print(f"Element at ({i}, {j}) has neighbors with the same intensity.")
#         else:
#             print(f"Element at ({i}, {j}) does not have neighbors with the same intensity.")

# # Print the binary intensity 8x8 matrix
# print("\nBinary Intensity 8x8 matrix:")
# print(binary_8x8_matrix)
# import numpy as np

# def bilinear_interpolation(source, target, source_corner, target_corner):
#     for i in range(target_corner[0], target_corner[0] + source.shape[0]):
#         for j in range(target_corner[1], target_corner[1] + source.shape[1]):
#             source_row = i - target_corner[0]
#             source_col = j - target_corner[1]
            
#             # Calculate the fractional coordinates within the source matrix
#             x = source_col
#             y = source_row
            
#             # Calculate integer and fractional parts of coordinates
#             x_int = int(x)
#             y_int = int(y)
#             x_frac = x - x_int
#             y_frac = y - y_int
            
#             # Perform bilinear interpolation
#             top_left = source[y_int, x_int]
#             top_right = source[y_int, min(x_int + 1, source.shape[1] - 1)]
#             bottom_left = source[min(y_int + 1, source.shape[0] - 1), x_int]
#             bottom_right = source[min(y_int + 1, source.shape[0] - 1), min(x_int + 1, source.shape[1] - 1)]
            
#             interpolated_value = (1 - x_frac) * (1 - y_frac) * top_left + \
#                                  x_frac * (1 - y_frac) * top_right + \
#                                  (1 - x_frac) * y_frac * bottom_left + \
#                                  x_frac * y_frac * bottom_right
            
#             target[i, j] = interpolated_value

# # Create a 4x4 matrix with random integer values between 1 and 10
# random_4x4_matrix = np.random.randint(1, 11, size=(4, 4))

# # Create an 8x8 matrix filled with zeros
# bilinear_8x8_matrix = np.zeros((8, 8), dtype=int)

# # Populate the 8x8 matrix using bilinear interpolation
# bilinear_interpolation(random_4x4_matrix, bilinear_8x8_matrix, (0, 0), (0, 0))
# bilinear_interpolation(random_4x4_matrix, bilinear_8x8_matrix, (0, 3), (0, 4))
# bilinear_interpolation(random_4x4_matrix, bilinear_8x8_matrix, (3, 0), (4, 0))
# bilinear_interpolation(random_4x4_matrix, bilinear_8x8_matrix, (3, 3), (4, 4))

# # Define a threshold value for converting to binary intensity
# threshold = 5

# # Convert the values in the 8x8 matrix to binary intensity values
# binary_8x8_matrix = (bilinear_8x8_matrix >= threshold).astype(int)

# # Function to check if neighbors have the same intensity value
# def has_same_intensity(matrix, row, col):
#     intensity = matrix[row, col]
    
#     neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1),
#                  (row, col-1),                 (row, col+1),
#                  (row+1, col-1), (row+1, col), (row+1, col+1)]
    
#     for r, c in neighbors:
#         if 0 <= r < matrix.shape[0] and 0 <= c < matrix.shape[1]:
#             if matrix[r, c] != intensity:
#                 return False
#     return True

# # Check neighboring intensity values
# for i in range(binary_8x8_matrix.shape[0]):
#     for j in range(binary_8x8_matrix.shape[1]):
#         if has_same_intensity(binary_8x8_matrix, i, j):
#             print(f"Element at ({i}, {j}) has neighbors with the same intensity.")
#         else:
#             print(f"Element at ({i}, {j}) does not have neighbors with the same intensity.")

# # Print the binary intensity 8x8 matrix
# print("\nBinary Intensity 8x8 matrix:")
# print(binary_8x8_matrix)
