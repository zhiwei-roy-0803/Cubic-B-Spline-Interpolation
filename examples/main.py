import yaml
from interpolater.utils.reader import read_input_data
from interpolater.spline.cubic import CubicBSpline


if __name__ == "__main__":
    with open("main.yaml", "r") as f:
        config = yaml.safe_load(f)
    points = read_input_data(file=config["input"]["file_name"])
    interpolator = CubicBSpline(points=points)
    deBoor_points, knots = interpolator.find_control_points()
    interpolator.save(X=deBoor_points, knots=knots, file=config["output"]["deBoor_file"])