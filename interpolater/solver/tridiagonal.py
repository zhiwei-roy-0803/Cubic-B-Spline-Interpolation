import numpy as np

class TriDiagonalSolver():

    @staticmethod
    def solve(A: np.ndarray, b:np.ndarray) -> np.ndarray:
        n = len(b)
        c = np.zeros(n - 1)
        d = np.zeros(n)

        # prepare vector c and d
        c[0] = A[0, 1] / A[0, 0]
        for i in range(1, n - 1):
            c[i] = A[i, i + 1] / (A[i, i] - A[i, i - 1] * c[i - 1])

        d[0] = b[0] / A[0, 0]
        for i in range(1, n):
            d[i] = (b[i] - A[i, i - 1] * d[i - 1]) / (A[i, i] - A[i, i - 1] * c[i - 1])

        # backward substitution for solving x
        x = np.zeros(n)
        x[-1] = d[-1]
        for i in range(n - 2, -1, -1):
            x[i] = d[i] - c[i] * x[i + 1]

        return x