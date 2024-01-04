
import numpy as np

def nearest_neighbor(source, target, source_corner, target_corner):
    for i in range(target_corner[0], target_corner[0] + source.shape[0]):
        for j in range(target_corner[1], target_corner[1] + source.shape[1]):
            source_row = i - target_corner[0]
            source_col = j - target_corner[1]
            target[i, j] = source[source_row, source_col]


random_4x4_matrix = np.random.randint(1, 11, size=(4, 4))


zero_8x8_matrix = np.zeros((8, 8), dtype=int)


nearest_neighbor(random_4x4_matrix, zero_8x8_matrix, (0, 0), (0, 0))
nearest_neighbor(random_4x4_matrix, zero_8x8_matrix, (0, 3), (0, 4))
nearest_neighbor(random_4x4_matrix, zero_8x8_matrix, (3, 0), (4, 0))
nearest_neighbor(random_4x4_matrix, zero_8x8_matrix, (3, 3), (4, 4))


print("Random 4x4 matrix:")
print(random_4x4_matrix)


print("\nPopulated 8x8 matrix:")
print(zero_8x8_matrix)
