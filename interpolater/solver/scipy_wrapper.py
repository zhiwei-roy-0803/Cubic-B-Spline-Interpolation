from scipy.linalg import solve

class ScipyWrapper():

    @staticmethod
    def solve(A, b):
        return solve(A, b)