import math


def binary_guess_search(array, element, nodes):
    left = 0
    right = len(array)
    max_iterations = math.ceil(math.sqrt(math.log(nodes, 2)))
    iteration = 0
    last_guess = 0

    while left <= right:
        if iteration > max_iterations:
            break
        else:
            iteration += 1
        mid = (left + right) // 2
        last_guess = array[mid]

        if element == array[mid]:
            return array[mid], max_iterations

        if element < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return last_guess, max_iterations


arr = []
for i in range(5000):
    sub_arr = []
    counter = 0
    for j in range(5000):
        sub_arr.append(i + counter)
        counter += 0.0001
    arr += sub_arr
nodes = 5000
print(binary_guess_search(arr, 1574, nodes))
