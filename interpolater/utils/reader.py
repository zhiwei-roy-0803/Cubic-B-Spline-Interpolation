import numpy as np

def read_input_data(file):
    points = []
    with open(file, "r") as f:
        for line in f.readlines():
            points.append([float(val) for val in  line.split(" ")])
    points = np.array(points)
    return points
