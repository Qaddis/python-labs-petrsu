from random import randint


def get_random_nums(length: int) -> dict[int]:
    return [randint(0, 10) for i in range(length)]


nums = get_random_nums(int(input("N: ")))

sr = sum(nums) / len(nums)

print(sr)
print(sum([(n - sr) ** 2 for n in nums]) ** 0.5)
