import math


def calculate_combinations(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)
