import random

import scipy.stats as st
import scipy as sp
import numpy as np
import scikit_posthocs


def quade_test(*args):
    """
        Performs a Quade ranking test.
        Tests the hypothesis that in a set of k dependent samples groups (where k >= 2) at least two of the groups represent populations with different median values.
        The difference with a friedman test is that it uses the median for each sample to wiehgt the ranking.

        Parameters
        ----------
        sample1, sample2, ... : array_like
            The sample measurements for each group.

        Returns
        -------
        F-value : float
            The computed F-value of the test.
        p-value : float
            The associated p-value from the F-distribution.
        rankings : array_like
            The ranking for each group.
        pivots : array_like
            The pivotal quantities for each group.

        References
        ----------
        D. Quade, Using weighted rankings in the analysis of complete blocks with additive block effects, Journal of the American Statistical Association 74 (1979) 680–683.
    """
    k = len(args)
    if k < 2: raise ValueError('Less than 2 levels')
    n = len(args[0])
    if len(set([len(v) for v in args])) != 1: raise ValueError('Unequal number of samples')

    rankings = []
    ranges = []
    for i in range(n):
        row = [col[i] for col in args]
        ranges.append(max(row) - min(row))
        row_sort = sorted(row)
        rankings.append([row_sort.index(v) + 1 + (row_sort.count(v) - 1) / 2. for v in row])

    ranges_sort = sorted(ranges)
    ranking_cases = [ranges_sort.index(v) + 1 + (ranges_sort.count(v) - 1) / 2. for v in ranges]

    S = []
    W = []
    for i in range(n):
        S.append([ranking_cases[i] * (r - (k + 1) / 2.) for r in rankings[i]])
        W.append([ranking_cases[i] * r for r in rankings[i]])

    Sj = [np.sum(row[j] for row in S) for j in range(k)]
    Wj = [np.sum(row[j] for row in W) for j in range(k)]

    rankings_avg = [w / (n * (n + 1) / 2.) for w in Wj]
    rankings_cmp = [r / sp.sqrt(k * (k + 1) * (2 * n + 1) * (k - 1) / (18. * n * (n + 1))) for r in rankings_avg]

    A = sp.sum(S[i][j] ** 2 for i in range(n) for j in range(k))
    B = sp.sum(s ** 2 for s in Sj) / float(n)
    F = (n - 1) * B / (A - B)

    p_value = 1 - st.f.cdf(F, k - 1, (k - 1) * (n - 1))

    return F, p_value, rankings_avg, rankings_cmp


index = [1, 2, 3, 4, 5]
vns = [127, 98, 93.14, 76.21, 48.46, 84, 64.15, 59.39, 46.87, 31.21, 59, 51.89, 44.47, 38.59, 30.23, 47, 40.71, 37.95,
       29.32, 27.05, 40, 40.06, 32.02, 25.38, 22.62, 38, 33.96, 26.78, 23.43, 21.18, 30, 30.37, 23.76, 22.42, 30.01,
       29.37, 24.07, 29, 25.08, 21.81]
grasp = [127, 98, 93.54, 74.02, 48, 84, 64, 55.54, 37.01, 20.01, 59, 51.41, 36.94, 26.85, 18, 47, 39, 29.41, 19.13, 14,
         40, 38.94, 23.21, 16, 11.89, 38, 32, 19, 13.68, 10, 30, 29.62, 16.28, 11.56, 30, 27.65, 16, 29, 23.98, 14]

vns_grasp = [vns, grasp]
vns_vns_grasp = [vns, [x + 0.01 for x in vns], grasp, [x + 0.01 for x in grasp]]

triples = []
for a, b, c in zip(vns, grasp, [x + random.uniform(-1, 1) for x in vns]):
    triples.append([a,b,c])

print("QUADE")
print(scikit_posthocs.posthoc_quade(triples))
print()

print(quade_test(vns,[x + random.uniform(-1, 1) for x in vns], [x + 0.01 for x in vns]))
# print(st.wilcoxon(vns, grasp))
# print()
# print(quade_test(vns, grasp))
