# Cubic-B-Spline-Interpolation
Implementation of cubic B-spline interpolation for Assignment 1 of CE7453
Numerical Algorithm @ NTU, Singapore. 

# How to use
Step 1:

Provide your input data points in the following format
```
x0 y0
x1 y1
...
xn yn
```
and store them into ./data directory. 

Step 2:
Enter the examples directory and modify the main.yaml configuration
file. The format of the yaml file is shown in the following.
```yaml
input:
  file_name: "../data/<your input data point file>"
output:
  deBoor_file: "log/<your output file>"
```
You should specify the input data file path and the output file path

Step 3: After the configuration, you can run the main.py:
```bash
python main.py
```
The control points as well as the knot vector will be computed and stored into the output file as
specified in the main.yaml file

Step 4: Modify the plot.yaml configuration file:
```yaml
data_points: "../data/<your input data point file>"
res: "log/<corresponding output file>"
```

Step 5: Run visualization program to see the interpolation result
```bash
python plot.py
```

# Examples

We have provided several examples in the ./data directory and you can
directly get the interpolation result by running:
```bash
cd examples
python main.py
python plot.py
```

# Technical Details
We provide the technical document for the implemented cubic B-spline
interpolation algorithm in ./docs directory. Please refer to the document
for the technical details.
