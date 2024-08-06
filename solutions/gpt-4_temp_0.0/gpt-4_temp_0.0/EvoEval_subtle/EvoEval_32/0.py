import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list, tolerance=1e-07, max_iterations=1000):
    """
    xs are coefficients of a polynomial xs[0] + xs[1] * x^1 + xs[2] * x^3 + .... xs[n] * x^(2*n-1)
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having at least two coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    x = 0.0
    for _ in range(max_iterations):
        fx = poly(xs, x)
        if abs(fx) < tolerance:
            return x
        dfx = poly(poly_derivative(xs), x)
        x -= fx / dfx
    return x