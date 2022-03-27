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

    if T[0] <= x < T[1]:
        return func_dict["func1"](x)

    elif T[1] <= x < T[2]:
        return func_dict["func2"](x)

    elif T[2] <= x < T[3]:
        return func_dict["func3"](x)

    elif T[3] <= x < T[4]:
        return func_dict["func4"](x)
    else:
        raise RuntimeError

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

    if T[0] <= x < T[1]:
        return derivative(func_dict["func1"], x0=x, dx=1e-3, n=2)

    elif T[1] <= x < T[2]:
        return derivative(func_dict["func2"], x0=x, dx=1e-3, n=2)

    elif T[2] <= x < T[3]:
        return derivative(func_dict["func3"], x0=x, dx=1e-3, n=2)

    elif T[3] <= x < T[4]:
        return derivative(func_dict["func4"], x0=x, dx=1e-3, n=2)
    else:
        raise RuntimeError