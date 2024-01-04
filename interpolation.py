import random

def generate_random_int_matrix(rows, cols, min_value, max_value):
    matrix = [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]
    return matrix

# Example: Populate a 4x4 matrix with integers between 1 and 10
rows = 4
cols = 4
min_value = 1
max_value = 10
random_int_matrix = generate_random_int_matrix(rows, cols, min_value, max_value)
new_matrix = random_int_matrix
print(new_matrix)

