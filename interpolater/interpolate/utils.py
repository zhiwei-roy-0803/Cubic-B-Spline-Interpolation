def _Nik(u, knots, i, k):
    if k == 0:
        return 1.0 if knots[i] <= u < knots[i + 1] else 0.0
    if knots[i + k] == knots[i]:
        c1 = 0.0
    else:
        c1 = (u - knots[i]) / (knots[i + k] - knots[i]) * _Nik(u, knots, i, k - 1)
    if knots[i + k + 1] == knots[i + 1]:
        c2 = 0.0
    else:
        c2 = (knots[i + k + 1] - u) / (knots[i + k + 1] - knots[i + 1]) * _Nik(u, knots, i + 1, k - 1)
    return c1 + c2


def interpolate(u, knots, control_pts, degree):
    n = len(control_pts)
    val = 0.0
    for i in range(n):
        val += control_pts[i] * _Nik(u, knots, i, degree)
    return val