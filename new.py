import numpy as np

def nearest_neighbor_interpolation(input_matrix, new_shape):
    input_height, input_width = input_matrix.shape
    output_height, output_width = new_shape

    y_scale = input_height / output_height
    x_scale = input_width / output_width

    output_matrix = np.zeros(new_shape, dtype=input_matrix.dtype)

    for y_out in range(output_height):
        for x_out in range(output_width):
            y_in = min(int(y_out * y_scale), input_height - 1)
            x_in = min(int(x_out * x_scale), input_width - 1)
            output_matrix[y_out, x_out] = input_matrix[y_in, x_in]

    return output_matrix


input_matrix = np.array([[1, 2], [3, 4]])


new_shape = (4, 4)
output_matrix = nearest_neighbor_interpolation(input_matrix, new_shape)

print("Input Matrix:")
print(input_matrix)

print("\nOutput Matrix:")
print(output_matrix)
