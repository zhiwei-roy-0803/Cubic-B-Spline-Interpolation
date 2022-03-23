import matplotlib.pyplot as plt
import yaml
import numpy as np
from interpolater.interpolate.utils import interpolate
from interpolater.utils.parser import parse_result
from interpolater.utils.reader import read_input_data

def visualize():

    # read config file
    with open("plot.yaml", "r") as f:
        config = yaml.safe_load(f)

    # parse result file
    degree, num_control_pts, knots, control_pts = parse_result(config["res"])

    # do interpolation with control points
    X = control_pts[:, 0]
    Y = control_pts[:, 1]
    tt = np.linspace(start=0.0, stop=0.999, num=100)
    x = [interpolate(t, knots, X, degree) for t in tt]
    y = [interpolate(t, knots, Y, degree) for t in tt]

    # read input data points
    data_points = read_input_data(config["data_points"])


    # visualize interpolation result
    plt.figure(dpi=300)
    plt.plot(X, Y, "k--", marker='s', markerfacecolor='r', label='control points')
    plt.plot(data_points[:, 0], data_points[:, 1], ' ', marker='o', markerfacecolor='c', label='data points')
    plt.plot(x, y, "g-", lw=2, label="Cubic B-Spline")
    plt.grid(axis="y")
    plt.legend(["control points", "data points", "interpolation"])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

if __name__ == "__main__":
    visualize()