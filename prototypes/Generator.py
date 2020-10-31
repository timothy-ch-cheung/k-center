def get_num():
    num = 0
    while True:
        yield num
        num += 1


nums = get_num()

print(nums)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
