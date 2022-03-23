import numpy as np

def parse_result(file):
    with open(file, "r") as f:
        degree = int(f.readline())
        num_control_pts = int(f.readline())
        knots = np.array([float(val) for val in f.readline().strip().split(" ")])
        control_pts = np.zeros((num_control_pts, 2))
        for idx, line in enumerate(f.readlines()):
            control_pts[idx, :] = np.array([float(val) for val in line.strip().split(" ")])
    return degree, num_control_pts, knots, control_pts