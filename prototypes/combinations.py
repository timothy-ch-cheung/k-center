nums = [1, 2, 3, 4, 5]


def combinations(nums, k, combo=[]):
    if k < 1:
        print(combo)
        return

    for i, val in enumerate(nums):
        next_permutations = list(combo)
        next_permutations.append(val)
        combinations(nums[i+1:], k - 1, next_permutations)


combinations(nums, 3)
