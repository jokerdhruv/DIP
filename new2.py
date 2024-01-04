import numpy as py
def nearest_neightbour(inp_matrix,new):
    inp_height , inp_width = inp_matrix.shape
    new_height , new_width = new.shape

    y_scale = inp_height / new_height
    x_scale = inp_width / new_width

    output_matrix = py.zeros(new, dtype=inp_matrix.dtype)
    for y_out in range(new_height):
        for x_out in range (new_width):
            y_in = min(int(y_out * y_scale), inp_height - 1)
            x_in = min(int(x_out * x_scale), inp_width - 1)
