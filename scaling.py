import numpy as np

def scale_image(input_image, scaling_factor):
    scaling_matrix = np.array([[1/scaling_factor, 0, 0],
                               [0, 1/scaling_factor, 0],
                               [0, 0, 1]])
    
    output_height = int(input_image.shape[0] * scaling_factor)
    output_width = int(input_image.shape[1] * scaling_factor)
    
    output_image = np.zeros((output_height, output_width), dtype=input_image.dtype)
    
    for y_out in range(output_height):
        for x_out in range(output_width):
            scaled_coords = np.dot(scaling_matrix, [y_out, x_out, 1])
            y_in = int(scaled_coords[0])
            x_in = int(scaled_coords[1])
            
            if 0 <= y_in < input_image.shape[0] and 0 <= x_in < input_image.shape[1]:
                output_image[y_out, x_out] = input_image[y_in, x_in]
    
    return output_image

# Create a sample binary input image
input_image = np.array([[0, 1, 0],
                        [1, 0, 1],
                        [0, 1, 0]])

# Define the scaling factor
scaling_factor = 2

# Perform image scaling
output_image = scale_image(input_image, scaling_factor)

# Print the input and output matrices
print("Input Image:")
print(input_image)
print("\nOutput Image (Scaled):")
print(output_image)
