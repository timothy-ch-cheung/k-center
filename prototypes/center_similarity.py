import math

# Graph

# a b c d
# e f g h
# i j k l
# m n o p

a = (0, 3)
b = (1, 3)
c = (2, 3)
d = (3, 3)
e = (0, 2)
f = (1, 2)
g = (2, 2)
h = (3, 2)
i = (0, 1)
j = (1, 1)
k = (2, 1)
l = (3, 1)
m = (0, 0)
n = (1, 0)
o = (2, 0)
p = (3, 0)

grid = [
    [a, e, i, m],
    [b, f, j, n],
    [c, g, k, o],
    [m, n, o, p]
]


# a = (0, 300)
# b = (100, 300)
# c = (200, 300)
# d = (300, 300)
# e = (0, 200)
# f = (100, 200)
# g = (200, 200)
# h = (300, 200)
# i = (0, 100)
# j = (100, 100)
# k = (200, 100)
# l = (300, 100)
# m = (0, 0)
# n = (100, 0)
# o = (200, 0)
# p = (300, 0)


def dist(a, b):
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


def normalise(A, B):
    def max_point(S):
        return max([x[0] for x in S]), max([x[1] for x in S])

    def min_point(S):
        return min([x[0] for x in S]), min([x[1] for x in S])

    def tup_diff(a, b):
        return a[0] - b[0], a[1] - b[1]

    def tup_div(a, b):
        return a[0] / (b[0] if b[0] != 0 else 1), a[1] / (b[1] if b[1] != 0 else 1)

    def apply_normalise(s):
        return {tup_div(tup_diff(x, min_value), tup_diff(max_value, min_value)) for x in s}

    max_value = max_point(A.union(B))
    min_value = min_point(A.union(B))
    max_value = (3, 3)
    min_value = (0, 0)

    A = apply_normalise(A)
    B = apply_normalise(B)
    return A, B


def sim(A, B):
    A, B = normalise(A, B)
    print(A, B, end=" :")
    score = 0
    for x in A:
        min_center = None
        min_dist = float("inf")
        for y in B:
            d = dist(x, y)
            if d < min_dist:
                min_center = y
                min_dist = d
        B.remove(min_center)
        score += min_dist
    return round((score/(len(A))/math.sqrt(2)), 2)


sol_one = {a, b}
sol_two = {c, d}
sol_three = {m, n}
sol_four = {o, p}

for i in range(len(grid)):
    for j in range(len(grid)-1):
        compared_set = {grid[i][j], grid[i][j + 1]}
        print(sim(sol_one, compared_set), f"[{grid[i][j]}, {grid[i][j + 1]}]")
