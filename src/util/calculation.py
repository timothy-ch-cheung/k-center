import math


def calculate_combinations(n, r):
    """Calculate number of combinations given the number of items are the length of a single combination
    param n: total number of items
    param r: number of items which form one combination
    return: the value of nCr (n Choose r)
    """
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)
