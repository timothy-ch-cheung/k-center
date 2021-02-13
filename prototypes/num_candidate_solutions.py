import math


def num_candidate_solutions(num_points: int, k: int) -> int:
    n_factorial = math.factorial(num_points)
    k_factorial = math.factorial(k)
    return n_factorial//(k_factorial * math.factorial(num_points - k))


print(num_candidate_solutions(100, 5))
