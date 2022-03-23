from scipy.misc import derivative


def basis_func(T, x):

    func_dict = {
        "func1": lambda x: (x - T[0]) * (x - T[0]) * (x - T[0]) / (T[1] - T[0]) / (T[2] - T[0]) / (T[3] - T[0]),

        "func2": lambda x: (x - T[0]) * (x - T[0]) * (T[2] - x) / (T[2] - T[1]) / (T[3] - T[0]) / (T[2] - T[0]) +
                           (T[3] - x) * (x - T[0]) * (x - T[1]) / (T[2] - T[1]) / (T[3] - T[1]) / (T[3] - T[0]) +
                           (T[4] - x) * (x - T[1]) * (x - T[1]) / (T[2] - T[1]) / (T[4] - T[1]) / (T[3] - T[1]),

        "func3": lambda x: (x - T[0]) * (T[3] - x) * (T[3] - x) / (T[3] - T[2]) / (T[3] - T[1]) / (T[3] - T[0]) +
                           (T[4] - x) * (T[3] - x) * (x - T[1]) / (T[3] - T[2]) / (T[4] - T[1]) / (T[3] - T[1]) +
                           (T[4] - x) * (T[4] - x) * (x - T[2]) / (T[3] - T[2]) / (T[4] - T[2]) / (T[4] - T[1]),

        "func4": lambda x: (T[4] - x) * (T[4] - x) * (T[4] - x) / (T[4] - T[3]) / (T[4] - T[2]) / (T[4] - T[1])
    }

    if T[0]<= x <= T[1] and (x != T[0] or x != T[1]):
        try:
            return func_dict["func1"](x)
        except ZeroDivisionError:
            return 0.0
    elif T[1]<= x <= T[2]:
        try:
            return func_dict["func2"](x)
        except ZeroDivisionError:
            return 0.0
    elif T[2]<= x <= T[3] and (x != T[2] or x != T[3]):
        try:
            return func_dict["func3"](x)
        except ZeroDivisionError:
            return 0.0
    elif T[3] <= x <= T[4] and (x != T[3] or x != T[4]):
        try:
            return func_dict["func4"](x)
        except ZeroDivisionError:
            return 0.0
    else:
        return 0

def basis_derivative2(T, x):

    func_dict = {
        "func1": lambda x: (x - T[0]) * (x - T[0]) * (x - T[0]) / (T[1] - T[0]) / (T[2] - T[0]) / (T[3] - T[0]),

        "func2": lambda x: (x - T[0]) * (x - T[0]) * (T[2] - x) / (T[2] - T[1]) / (T[3] - T[0]) / (T[2] - T[0]) +
                           (T[3] - x) * (x - T[0]) * (x - T[1]) / (T[2] - T[1]) / (T[3] - T[1]) / (T[3] - T[0]) +
                           (T[4] - x) * (x - T[1]) * (x - T[1]) / (T[2] - T[1]) / (T[4] - T[1]) / (T[3] - T[1]),

        "func3": lambda x: (x - T[0]) * (T[3] - x) * (T[3] - x) / (T[3] - T[2]) / (T[3] - T[1]) / (T[3] - T[0]) +
                           (T[4] - x) * (T[3] - x) * (x - T[1]) / (T[3] - T[2]) / (T[4] - T[1]) / (T[3] - T[1]) +
                           (T[4] - x) * (T[4] - x) * (x - T[2]) / (T[3] - T[2]) / (T[4] - T[2]) / (T[4] - T[1]),

        "func4": lambda x: (T[4] - x) * (T[4] - x) * (T[4] - x) / (T[4] - T[3]) / (T[4] - T[2]) / (T[4] - T[1])
    }

    if T[0] <= x <= T[1] and (x != T[0] or x != T[1]):
        try:
            return derivative(func_dict["func1"], x0=x, dx=1e-3, n=2)
        except ZeroDivisionError:
            return 0.0
    elif T[1] <= x <= T[2] and (x != T[1] or x != T[2]):
        try:
            return derivative(func_dict["func2"], x0=x, dx=1e-3, n=2)
        except ZeroDivisionError:
            return 0.0
    elif T[2] <= x <= T[3] and (x != T[2] or x != T[3]):
        try:
            return derivative(func_dict["func3"], x0=x, dx=1e-3, n=2)
        except ZeroDivisionError:
            return 0.0
    elif T[3] <= x <= T[4] and (x != T[3] or x != T[4]):
        try:
            return derivative(func_dict["func4"], x0=x, dx=1e-3, n=2)
        except ZeroDivisionError:
            return 0.0
    else:
        return 0.0